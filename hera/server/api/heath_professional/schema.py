from pydantic import BaseModel

class HealthProfessionalPydantic(BaseModel):
    name: str

    class Config:
        orm_mode = True
