from sqlalchemy.orm import Session
from models.role import Role
from schemas.role import RoleCreate

def create_role(db: Session, role_data: RoleCreate):
    role = Role(**role_data.model_dump())
    db.add(role)
    db.commit()
    db.refresh(role)
    return role

def get_all_roles(db: Session):
    return db.query(Role).all()
