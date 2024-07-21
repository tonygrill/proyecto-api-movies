from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel
from utils.jwt_manager import create_token
from config.database import engine, Base
from middlewares.error_handler import ErrorHandler
from routers.movie import movie_router
from routers.user import user_router


# creamos la instancia de fastAPI

app = FastAPI()
app.title = 'Mi Aplicación con FastAPI'
app.version = '0.0.1'

app.add_middleware(ErrorHandler)
app.include_router(movie_router)
app.include_router(user_router)

Base.metadata.create_all(bind=engine)

movies = [
    {
        "id": 1,
        "title": 'Avatar',
        "overview": 'una descripción',
        "year": 2009,
        "rating": 8,
        "category": "Accion"
    },
    {
         "id": 2,
        "title": 'Avatar',
        "overview": 'una descripción',
        "year": 2009,
        "rating": 8,
        "category": "ficcion"
    }
]

@app.get('/', tags=['home'])
def message():
    return HTMLResponse('<h1>Hellow world</h1>')


