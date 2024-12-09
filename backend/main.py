from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from app.routers import ads
from app.models import Base
from sqlalchemy import create_engine

DATABASE_URL = "postgresql://user:password@db:5432/advertising"
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Ad Management Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://frontend.local"],  # или указать нужные домены
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(ads.router, prefix="/ads", tags=["Ads"])
