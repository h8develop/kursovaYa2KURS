from fastapi import FastAPI
from app.routers import ads
from app.models import Base
from sqlalchemy import create_engine

DATABASE_URL = "postgresql://user:password@db:5432/advertising"

engine = create_engine(DATABASE_URL)

# Создание таблиц
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Ad Management Backend")

app.include_router(ads.router, prefix="/ads", tags=["Ads"])
