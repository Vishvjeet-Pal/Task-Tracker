from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from core.utils.database import Base

class Comment(Base):
    __tablename__="comments"

    task_id = Column(Integer, ForeignKey('tasks.task_id'))
    e_id = Column(Integer, ForeignKey('users.e_id'))
    content = Column(String)
    timestamp = Column(DateTime)

    task = relationship("Task")
    user = relationship("User")