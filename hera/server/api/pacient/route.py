from typing import List, Annotated

from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import InterfaceError

from hera.server.api.pacient.schema import PacientPydantic
from hera.server.api.pacient.model import PacientSQL

from hera.server.database import get_db

router = APIRouter(prefix="/patients")

@router.post("")
async def create_patient(patient: PacientPydantic, db: AsyncSession = Depends(get_db)):

    db_patient = PacientSQL(**patient.model_dump())
    db.add(db_patient)

    await db.commit()
    await db.refresh(db_patient)

    return db_patient

@router.get("/{patient_id}", response_model=PacientPydantic)
async def read_patient(patient_id: int, db: AsyncSession = Depends(get_db)):

    statement = select(PacientSQL).filter_by(id=patient_id)
    patient = await db.scalar(statement)

    if patient is None:
        raise HTTPException(status_code=404, detail="Patient not found")

    return patient

@router.delete("/{patient_id}", response_model=PacientPydantic)
async def delete_patient(patient_id: int, db: AsyncSession = Depends(get_db)):

    statement = select(PacientSQL).filter_by(id=patient_id)
    patient = await db.scalar(statement)

    if patient is None:
        raise HTTPException(status_code=404, detail="Patient not found")

    await db.delete(patient)
    await db.commit()

    return patient