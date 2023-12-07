from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from hera.server.database import Base

class PacientSQL(Base):
    __tablename__ = 'pacient'

    id = Column(Integer, primary_key=True, autoincrement=True)
    health_professional_id = Column(Integer, ForeignKey('healthprofessional.id'))
    name = Column(String)

    health_professional = relationship('HealthProfessionalSQL', back_populates='patients', lazy='selectin')