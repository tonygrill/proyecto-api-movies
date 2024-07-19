from fastapi import FastAPI, Body, Path, Query 
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List

# creamos la instancia de fastAPI

app = FastAPI()
app.title = 'Mi Aplicación con FastAPI'
app.version = '0.0.1'

class Movie(BaseModel):
    id: Optional[int] = None
    title: str = Field(min_length=1, max_length=30)
    overview: str = Field(min_length=1, max_length=100)
    year: int = Field(le=2024)
    rating: float = Field(ge=1, le=10)
    category: str = Field(min_length=1, max_length=20)


    class Config:
        json_schema_extra = {
            'example':{
                'id': 1,
                'title': 'Nombre',
                'overview': 'Descripción de la pelicula',
                'year': 2020,
                'rating': 9,
                'category': 'Acción'
            }
        }


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

# Nuestro primer endpoint
@app.get('/', tags=['home'])
def message():
    return HTMLResponse('<h1>Hellow world</h1>')

@app.get('/movies', tags=['movies'], response_model=List[Movie], status_code=200)
def get_movies() -> List[Movie]:
    return JSONResponse(status_code=200, content=movies)

@app.get('/movies/{id}', tags=['movies'], response_model=Movie)
def get_movie(id: int = Path(ge=1, le=2000)) -> Movie:
    for item in movies:
        if item["id"] == id:
            return JSONResponse(content=item)
    return JSONResponse(status_code=404, content=[])

@app.get('/movies/category/{category}', tags=['movies'], response_model=List[Movie])
def get_movie_by_category(category: str = Path(min_length=1, max_length=20)) -> List[Movie]:
    data = [item for item in movies if item['category'].lower() == category.lower()]
    return JSONResponse(content=data)

# Método POST
@app.post('/movies', tags=['movies'], response_model=dict, status_code=201)
def create_movie(movie: Movie) -> dict:
    movies.append(movie)
    return JSONResponse(status_code=201, content={'message':'Se ha registrado la película'})

@app.put('/movies/{id}', tags=['movies'], response_model=dict, status_code=200)
def update_movie(id: int, movie: Movie) -> dict:
    for item in movies:
        if item["id"] == id:
            item['title'] = movie.title
            item['overview'] = movie.overview
            item['year'] = movie.year
            item['rating'] = movie.rating
            item['category'] = movie.category
            return JSONResponse(status_code=200, content={'message':'Se ha modificado la película'})

@app.delete('/movies/{id}', tags=['movies'], response_model=dict, status_code=200)
def delete_movies(id: int) -> dict:
    for item in movies:
        if item['id'] == id:
            movies.remove(item)
            return JSONResponse(status_code=200, content={'message':'Se ha eliminado la película'})