from pydantic import BaseModel

class HealthProfessionalPydantic(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True
