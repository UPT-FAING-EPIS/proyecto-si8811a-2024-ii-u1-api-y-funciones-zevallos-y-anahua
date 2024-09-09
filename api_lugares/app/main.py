from fastapi import FastAPI, HTTPException
from .schemas import LugarCreate, DireccionCreate, CategoriaCreate
from .crud import (create_lugar, get_lugares, get_lugar, create_direccion, get_direcciones, 
                   create_categoria, get_categorias)
from .config import setup_db

app = FastAPI()

# Configuración inicial de la base de datos
setup_db()

# Endpoints para Lugares
@app.post("/lugares/")
async def create_new_lugar(lugar: LugarCreate):
    return create_lugar(lugar)

@app.get("/lugares/")
async def get_all_lugares():
    return get_lugares()

@app.get("/lugares/{id_lugar}")
async def get_single_lugar(id_lugar: str):
    lugar = get_lugar(id_lugar)
    if not lugar:
        raise HTTPException(status_code=404, detail="Lugar no encontrado")
    return lugar

# Endpoints para Direcciones
@app.post("/direcciones/")
async def create_new_direccion(direccion: DireccionCreate):
    return create_direccion(direccion)

@app.get("/direcciones/")
async def get_all_direcciones():
    return get_direcciones()

# Endpoints para Categorías
@app.post("/categorias/")
async def create_new_categoria(categoria: CategoriaCreate):
    return create_categoria(categoria)

@app.get("/categorias/")
async def get_all_categorias():
    return get_categorias()
