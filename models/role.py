from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from core.utils.database import Base

class Role(Base):
    __tablename__ = "roles"

    r_id = Column(Integer, primary_key=True, index=True)
    role = Column(String, unique=True, index=True)
    e_id = Column(String, ForeignKey('users.e_id'), index=True)
    permissions = Column(String)
    
    users = relationship("User", back_populates="role")