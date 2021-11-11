from fastapi import FastAPI
from . import  models
from .database import engine
from .routers import user,image,authentication
from fastapi.staticfiles import StaticFiles

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.mount("/static", StaticFiles(directory="Image/static"), name="static")

app.include_router(authentication.router)
app.include_router(user.router)
app.include_router(image.router)
