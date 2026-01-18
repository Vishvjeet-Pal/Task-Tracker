from pydantic import BaseModel

class RoleCreate(BaseModel):
    r_id: int
    role: str
    permissions: str

class RoleResponse(BaseModel):
    r_id: int
    role: str
    permissions: str

    class Config:
        from_attributes = True
