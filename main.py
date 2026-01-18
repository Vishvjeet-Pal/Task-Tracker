from fastapi import FastAPI
from core.utils.database import engine, Base
import models  
from routes.user import router as user_router
from routes.role import router as role_router

app = FastAPI(title="Task Tracker")

Base.metadata.create_all(bind=engine)

app.include_router(user_router)
app.include_router(role_router)