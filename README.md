# Mi Aplicación con FastAPI

## Descripción

Esta es una API para la gestión de películas desarrollada con FastAPI. Permite realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre una base de datos de películas, además de gestionar la autenticación de usuarios mediante JWT.

## Tecnologías Utilizadas

- **FastAPI**: Framework para construir APIs web rápidas y robustas con Python.
- **SQLAlchemy**: ORM para manejar la base de datos SQLite.
- **Pydantic**: Para la validación de datos.
- **JWT**: Para la autenticación y generación de tokens.
- **Uvicorn**: Servidor ASGI para ejecutar la aplicación FastAPI.

## Requisitos

- Python 3.8+
- `pip` (Python package installer)

## Instalación

1. Clona este repositorio:
   ```bash
   git clone https://github.com/tonygrill/proyecto-api-movies.git

2. Crea un entorno virtual:
    ```bash
    python -m venv venv

 En Linux usa:
`source venv/bin/activate`  

 En Windows usa:
    `venv\Scripts\activate`

3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt

4. Ejecuta la aplicación
   ```bash
   uvicorn main:app --reload --port 5000

5. Abre tu navegador y escribe
http://localhost:5000/docs


## Uso

### Endpoints Disponibles

#### Autenticación

- **Inicio de sesión:** Permite a los usuarios autenticarse y obtener un token JWT.

#### Películas

- **Obtener todas las películas:** Recupera una lista de todas las películas en la base de datos. Requiere autenticación JWT.
- **Obtener una película por ID:** Recupera la información de una película específica utilizando su ID.
- **Obtener películas por categoría:** Recupera una lista de películas que pertenecen a una categoría específica.
- **Crear una nueva película:** Agrega una nueva película a la base de datos.
- **Actualizar una película existente:** Actualiza la información de una película específica.
- **Eliminar una película:** Elimina una película de la base de datos.

### Estructura del Proyecto

```bash
.
├── config
│   └── database.py
├── middlewares
│   ├── error_handler.py
│   └── jwt_bearer.py
├── models
│   └── movie.py
├── routers
│   ├── movie.py
│   └── user.py
├── schemas
│   ├── movie.py
│   └── user.py
├── services
│   └── movie.py
├── utils
│   └── jwt_manager.py
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

### Contacto
- Autor: Antonio Miguel Moreno Martínez
- Correo: antomore353@hotmail.com
- LinkedIn: https://www.linkedin.com/in/antonio-miguel-moreno-mart%C3%ADnez-473a162a2/