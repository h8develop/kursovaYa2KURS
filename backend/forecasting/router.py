from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

router = APIRouter()

class TrafficData(BaseModel):
    date: str  # Формат YYYY-MM-DD
    visitors: int

@router.post("/predict")
def predict_traffic(data: List[TrafficData]):
    # Пример простой логики прогнозирования
    predicted = [int(d.visitors * 1.1) for d in data]
    return {"predicted_traffic": predicted}
