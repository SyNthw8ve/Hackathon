from sqlalchemy import Column, Integer, String
from hera.server.database import Base

class HealthProfessionalSQL(Base):
    __tablename__ = 'HealthProfessional'

    id = Column(Integer, primary_key=True)
    name = Column(String)