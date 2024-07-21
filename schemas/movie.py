from pydantic import BaseModel, Field
from typing import Optional

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
