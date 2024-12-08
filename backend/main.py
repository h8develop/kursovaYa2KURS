from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Ad Management System"}

# Импортируйте роутеры микросервисов
from auth.router import router as auth_router
from ads.router import router as ads_router
from forecasting.router import router as forecasting_router

app.include_router(auth_router, prefix="/auth", tags=["Authentication"])
app.include_router(ads_router, prefix="/ads", tags=["Ads Management"])
app.include_router(forecasting_router, prefix="/forecasting", tags=["Traffic Forecasting"])
