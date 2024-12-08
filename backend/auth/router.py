from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel

router = APIRouter()

# Модель пользователя
class User(BaseModel):
    username: str
    password: str

@router.post("/login")
def login(user: User):
    # Логика аутентификации
    return {"message": "User logged in"}

@router.post("/register")
def register(user: User):
    # Логика регистрации
    return {"message": "User registered"}
