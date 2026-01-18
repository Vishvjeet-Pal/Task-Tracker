from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from core.utils.deps import get_db
from schemas.user import UserCreate, UserResponse
from services.user_service import create_user, get_all_users

router=APIRouter(prefix="/users", tags=["Users"])

@router.post("/", response_model=UserResponse)
def add_user(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user)

@router.get("/", response_model=list[UserResponse])
def list_users(db: Session = Depends(get_db)):
    return get_all_users(db)