from fastapi import FastAPI
from api import user_routes,tiffin_routes
from db.database import engine
from models import user, tiffin_service

user.Base.metadata.create_all(bind=engine)
tiffin_service.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(user_routes.router)
app.include_router(tiffin_routes.router)