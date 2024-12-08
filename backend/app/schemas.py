from pydantic import BaseModel

class AdBase(BaseModel):
    title: str
    description: str

class AdCreate(AdBase):
    pass

class AdRead(AdBase):
    id: int

    class Config:
        orm_mode = True
