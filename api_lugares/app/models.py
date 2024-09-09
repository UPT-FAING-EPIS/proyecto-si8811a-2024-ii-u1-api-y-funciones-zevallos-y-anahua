from pydantic import BaseModel
from uuid import uuid4

class Lugar(BaseModel):
    id_lugar: str
    nombre_lugar: str
    direccion_id: str
    capacidad: int
    descripcion: str
    latitud: float
    longitud: float
    id_categoria: str

class Direccion(BaseModel):
    direccion_id: str
    calle: str
    numero: str
    ciudad: str
    codigo_postal: str
    pais: str | None = None  # Campo opcional

class Categoria(BaseModel):
    id_categoria: str
    nombre_categoria: str
