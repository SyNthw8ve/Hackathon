from sqlalchemy import Column, Integer, String
from hera.server.database import Base

class HealthProfessionalSQL(Base):
    __tablename__ = 'healthprofessional'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)