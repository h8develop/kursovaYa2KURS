from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class Ad(BaseModel):
    title: str
    content: str
    budget: float

@router.post("/")
def create_ad(ad: Ad):
    # Логика создания рекламы
    return {"message": "Ad created", "ad": ad}

@router.get("/{ad_id}")
def get_ad(ad_id: int):
    # Логика получения рекламы
    return {"ad_id": ad_id, "message": "Ad details"}

@router.put("/{ad_id}")
def update_ad(ad_id: int, ad: Ad):
    # Логика обновления рекламы
    return {"message": f"Ad {ad_id} updated", "ad": ad}

@router.delete("/{ad_id}")
def delete_ad(ad_id: int):
    # Логика удаления рекламы
    return {"message": f"Ad {ad_id} deleted"}
