from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Response
from app.routers import ads
from app.models import Base
from sqlalchemy import create_engine
from prometheus_client import Counter, Histogram, generate_latest

# Настраиваем базу данных
DATABASE_URL = "postgresql://user:password@db:5432/advertising"
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(bind=engine)

# Инициализируем приложение
app = FastAPI(title="Ad Management Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://frontend.local"],  # или указать нужные домены
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Создаем метрики
ads_created_counter = Counter(
    'ads_created_total', 
    'Total number of ads created'
)

ad_creation_latency = Histogram(
    'ad_creation_latency_seconds', 
    'Latency for creating an ad'
)

# Подключаем роуты объявлений
app.include_router(ads.router, prefix="/ads", tags=["Ads"])

# Добавляем endpoint /metrics в main.py
@app.get("/metrics")
def metrics():
    # Возвращаем все собранные метрики в формате, который понимает Prometheus
    return Response(generate_latest(), media_type="text/plain")
