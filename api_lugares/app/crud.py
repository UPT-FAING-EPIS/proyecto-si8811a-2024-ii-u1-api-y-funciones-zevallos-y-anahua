import couchdb
from uuid import uuid4
from .config import setup_db
from .models import Lugar, Direccion, Categoria

# Conectar con CouchDB y asegurarse de que las bases de datos existen
couch = setup_db()

# Acceso a las bases de datos
lugares_db = couch['lugares']
direcciones_db = couch['direcciones']
categorias_db = couch['categorias']

# CRUD Lugares
def create_lugar(lugar):
    lugar_data = lugar.dict()
    lugar_data['_id'] = str(uuid4())  # Genera un identificador único
    lugares_db.save(lugar_data)
    return lugar_data

def get_lugares():
    return [lugar for lugar in lugares_db]

def get_lugar(id_lugar):
    lugar_id = str(id_lugar)
    try:
        return lugares_db[lugar_id]
    except couchdb.http.ResourceNotFound:
        return None

# CRUD Direcciones
def create_direccion(direccion):
    direccion_data = direccion.dict()
    direccion_data['_id'] = str(uuid4())  # Genera un identificador único
    direcciones_db.save(direccion_data)
    return direccion_data

def get_direcciones():
    return [direccion for direccion in direcciones_db]

# CRUD Categorías
def create_categoria(categoria):
    categoria_data = categoria.dict()
    categoria_data['_id'] = str(uuid4())  # Genera un identificador único
    categorias_db.save(categoria_data)
    return categoria_data

def get_categorias():
    return [categoria for categoria in categorias_db]
