[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/vK6WBQ1t)
[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=15560954)

## API de Lugares

Esta API permite gestionar lugares, direcciones y categorías utilizando FastAPI y CouchDB como base de datos.

## Requisitos

- **Python 3.7+**
- **CouchDB**: Se requiere tener CouchDB corriendo para poder almacenar y recuperar la información de los lugares, direcciones y categorías.
- **FastAPI**: Framework web para construir APIs rápidas y eficientes.
- **Uvicorn**: Servidor ASGI para correr la aplicación de FastAPI.

## Estructura del Proyecto

```plaintext
api_lugares/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── crud.py
│   ├── models.py
│   ├── schemas.py
│   ├── config.py
│
└── requirements.txt
```

## Instalación

1. Clonar el repositorio:

   ```bash
   git clone https://github.com/UPT-FAING-EPIS/proyecto-si8811a-2024-ii-u1-api-y-funciones-zevallos-y-anahua.git
   ```

2. Navegar al directorio del proyecto:

   ```bash
   cd proyecto-si8811a-2024-ii-u1-api-y-funciones-zevallos-y-anahua/api_lugares
   ```

3. Crear un entorno virtual e instalar las dependencias:

   ```bash
   python -m venv env

   .\env\Scripts\activate

   pip install -r requirements.txt
   ```

4. Configurar las variables de entorno:

   El archivo `config.py` obtiene la URL de CouchDB de las variables de entorno. Debe seguir el formato:

   ```bash
   export COUCHDB_URL=http://usuario:contrasena@localhost:5984
   ```

5. Iniciar el servidor:

   ```bash
   uvicorn main:app --reload
   ```

### Endpoints

- **Lugares**

  - `GET /lugares/`: Obtener todos los lugares.
  - `POST /lugares/`: Crear un nuevo lugar.
  - `GET /lugares/{id_lugar}`: Obtener un lugar por su ID.

- **Direcciones**

  - `GET /direcciones/`: Obtener todas las direcciones.
  - `POST /direcciones/`: Crear una nueva dirección.

- **Categorías**
  - `GET /categorias/`: Obtener todas las categorías.
  - `POST /categorias/`: Crear una nueva categoría.

## Diagrama de Clases

```mermaid

classDiagram
    class Lugar {
        +int id_lugar
        +string nombre_lugar
        +int direccion_id
        +int capacidad
        +string descripcion
        +float latitud
        +float longitud
        +int id_categoria
    }

    class Direccion {
        +int direccion_id
        +string calle
        +string numero
        +string ciudad
        +string codigo_postal
        +string pais
    }

    class Categoria {
        +int id_categoria
        +string nombre_categoria
    }

    Lugar --> Direccion : tiene
    Lugar --> Categoria : pertenece

```

Este diagrama de clases ilustra la relación entre las entidades principales de la API. Cada **Lugar** está asociado con una **Dirección** y una **Categoría**.

## Pruebas

Puedes acceder a la documentación generada por Swagger en la ruta `/docs`. Esta interfaz permite probar los diferentes endpoints directamente desde el navegador. Para acceder, abre `http://localhost:8000/docs`.

![alt text](assets/image.png)

![alt text](assets/image-1.png)

![alt text](assets/image-2.png)

![alt text](assets/image-3.png)

## Comandos

| **Comando**                     | **Descripción**                                                                   |
| ------------------------------- | --------------------------------------------------------------------------------- |
| `python -m venv env`            | Crea un entorno virtual en Python.                                                |
| `.\env\Scripts\activate`        | Activa el entorno virtual en Windows.                                             |
| `deactivate`                    | Desactiva el entorno virtual.                                                     |
| `pip install fastapi uvicorn`   | Instala FastAPI y Uvicorn en el entorno actual.                                   |
| `pip install couchdb`           | Instala la librería de Python para interactuar con CouchDB.                       |
| `pip freeze > requirements.txt` | Guarda una lista de las dependencias instaladas en un archivo `requirements.txt`. |
| `uvicorn main:app --reload`     | Ejecuta el servidor FastAPI con recarga automática en caso de cambios.            |
