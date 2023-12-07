from typing import List, Annotated

from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import InterfaceError

from hera.server.api.heath_professional.schema import HealthProfessionalPydantic
from hera.server.api.heath_professional.model import HealthProfessionalSQL

from hera.server.database import get_db

router = APIRouter(prefix="/alarms")

@router.post("/health_professionals/")
async def create_health_professional(health_professional: HealthProfessionalPydantic, db: AsyncSession = Depends(get_db)):
    db_health_professional = HealthProfessionalSQL(**health_professional.dict())
    db.add(db_health_professional)
    db.commit()
    db.refresh(db_health_professional)
    return db_health_professional

# Endpoint to retrieve a health professional by ID
@router.get("/health_professionals/{health_professional_id}", response_model=HealthProfessionalPydantic)
async def read_health_professional(health_professional_id: int, db: AsyncSession = Depends(get_db)):
    health_professional = db.query(HealthProfessionalSQL).filter(HealthProfessionalSQL.id == health_professional_id).first()
    if health_professional is None:
        raise HTTPException(status_code=404, detail="Health Professional not found")
    return health_professional

# Endpoint to delete a health professional by ID
@router.delete("/health_professionals/{health_professional_id}", response_model=HealthProfessionalPydantic)
async def delete_health_professional(health_professional_id: int, db: AsyncSession = Depends(get_db)):
    health_professional = db.query(HealthProfessionalSQL).filter(HealthProfessionalSQL.id == health_professional_id).first()
    if health_professional is None:
        raise HTTPException(status_code=404, detail="Health Professional not found")
    db.delete(health_professional)
    db.commit()
    return health_professional