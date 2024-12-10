from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Response
from app.routers import ads
from app.app.models import Base  # Убедитесь, что путь правильный
from sqlalchemy import create_engine
from prometheus_client import generate_latest
from app.metrics import ads_created_counter, ad_creation_latency  # Импорт метрик

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

# Подключаем роуты объявлений
app.include_router(ads.router, prefix="/ads", tags=["Ads"])

# Endpoint /metrics
@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type="text/plain")
