from pydantic import BaseModel

class PacientPydantic(BaseModel):
    _id: int
    health_professional_id: int
    name: str

    class Config:
        orm_mode = True