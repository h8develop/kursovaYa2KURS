from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.schemas import AdCreate, AdRead
from app.models import Ad
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from backend.main import ads_created_counter, ad_creation_latency  # импортируем метрики

DATABASE_URL = "postgresql://user:password@db:5432/advertising"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=AdRead)
def create_ad(ad: AdCreate, db: Session = Depends(get_db)):
    with ad_creation_latency.time():
        db_ad = Ad(title=ad.title, description=ad.description)
        db.add(db_ad)
        db.commit()
        db.refresh(db_ad)
        # Увеличиваем счетчик после успешного создания
        ads_created_counter.inc()
        return db_ad

@router.get("/", response_model=list[AdRead])
def read_ads(db: Session = Depends(get_db)):
    ads = db.query(Ad).all()
    return ads

@router.get("/{ad_id}", response_model=AdRead)
def read_ad(ad_id: int, db: Session = Depends(get_db)):
    ad = db.query(Ad).filter(Ad.id == ad_id).first()
    if ad is None:
        raise HTTPException(status_code=404, detail="Ad not found")
    return ad

@router.put("/{ad_id}", response_model=AdRead)
def update_ad(ad_id: int, ad: AdCreate, db: Session = Depends(get_db)):
    db_ad = db.query(Ad).filter(Ad.id == ad_id).first()
    if db_ad is None:
        raise HTTPException(status_code=404, detail="Ad not found")
    db_ad.title = ad.title
    db_ad.description = ad.description
    db.commit()
    db.refresh(db_ad)
    return db_ad

@router.delete("/{ad_id}")
def delete_ad(ad_id: int, db: Session = Depends(get_db)):
    db_ad = db.query(Ad).filter(Ad.id == ad_id).first()
    if db_ad is None:
        raise HTTPException(status_code=404, detail="Ad not found")
    db.delete(db_ad)
    db.commit()
    return {"detail": "Ad deleted"}
