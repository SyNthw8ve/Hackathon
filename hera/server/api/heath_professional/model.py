from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from hera.server.database import Base
from hera.server.api.pacient.model import PacientSQL

class HealthProfessionalSQL(Base):
    __tablename__ = 'healthprofessional'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    patients = relationship('PacientSQL', back_populates='health_professional', lazy='selectin')