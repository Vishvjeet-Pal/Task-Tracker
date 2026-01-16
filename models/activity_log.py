from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from core.utils.database import Base

class ActivityLog(Base):
    __tablename__="activity_logs"

    activity_id = Column(Integer, primary_key=True, index=True)
    e_id = Column(Integer, ForeignKey('users.e_id'))
    category = Column(String)
    timestamp = Column(String)

    user = relationship("User")