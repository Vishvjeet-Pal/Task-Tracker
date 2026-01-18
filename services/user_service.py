from sqlalchemy.orm import Session
from models.user import User
from schemas.user import UserCreate

def create_user(db: Session, user_data: UserCreate):
    user = User(**user_data.model_dump())
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_user_by_id(db: Session, e_id: int):
    return db.query(User).filter(User.e_id == e_id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def get_all_users(db: Session):
    return db.query(User).all()
