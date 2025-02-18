# FastAPI
## Product and Task system

Es un API de un Sistema de tareas, usando FastApi con Python.
El siguiente sistema de transacciones contiene:

- Tareas


## BASE DE DATOS

Es necesario realizar la creación de la base de datos llamada 
"fastapi_product". Para crear ingresamos por terminal y ejecutamos los siguientes comandos

```
tuusuario:$ sudo su postgres
postgres:$ createdb fastapi_product
postgres:$ exit
```

Para poder borrar una base de datos existente, utilizaremos el siguiente comando
```
tuusuario:$ sudo su postgres
postgres:$ dropdb fastapi_product
postgres:$ exit
```

## Instalación
CLONAR EL PROYECTO
Iniciamos con la clonación del proyecto, en la carpeta que utilice para desarrollo
```
$ git@github.com:henrytaby/fastapi-product.git
```
INGRESAR AL PROYECTO

Ingresamos a la carpeta del proyecto
```
tuusuario:$ cd fastapi-product
```
Abrimos Visual Studio Code en el proyecto

```
tuusuario:/fastapi-product/$ code .
```
En Visual Studio Code, ingresamos a la terminal.

CREANDO ENTORNO VIRTUAL

Ahora que tenemos el proyecto en nuestra máquina local, debemos inicializar un entorno virtual de python con el siguiente comando:
```
tuusuario:/fastapi-product/$ python3 -m venv env
```
ACTIVANDO EL ENTORNO VIRTUAL

Ahora que tenemos el entorno virtual de python, debemos activarlo con el siguiente comando:
```
tuusuario:/fastapi-product/$ source env/bin/activate
```

Se darán cuenta que esta activado el entorno virtual de python cuando vean al inicio de la línea de comando “(env)”, esto significa que tu terminal ya está corriendo en un entorno virtual.

INSTALACIÓN DE LIBRERÍAS NECESARIAS DE PYTHON

Para realizar la ejecución de la aplicación y después de haber creado el entorno virtual de python, es necesario realizar la instalación de librerías necesarias.
```
tuusuario:/fastapi-product/$ pip install -r requirements.txt
```

CONFIGURACIÓN DE CONEXIÓN A LA BASE DE DATOS

Ya contamos con la base de datos creada, y procedemos a crear el archivo ".env", que contiene la configuración de la base de datos. 

```
tuusuario:/fastapi-product/$ cp .env.example .env
```
Editaremos el archivo .env creado y cambiaremos el valor de "DATABASE_URL"


*DATABASE_URL = "postgresql://user:password@localhost/fastapi_product"*

## Ejecutar en modo desarrollo

Ya que tenemos todo configurado, realizamos la ejecución en modo desarrollo de nuestro API
```
fastapi dev app/main.py
```
## INGRESAR

El sistema correrá en el puerto 8000 por defecto.

Para probar también puede ingresar a la documentación con Swagger generado por FastAPI, en la siguiente dirección.

http://localhost:8000/docs

Para poder visualizar la documentación puedes ingresar a

http://localhost:8000/redoc 

## BIBLIOGRAFÍA
- https://fastapi.tiangolo.com
- https://fastapi.tiangolo.com/es/tutorial/first-steps/
- https://sqlmodel.tiangolo.com/
- https://sqlmodel.tiangolo.com/tutorial/
- https://docs.pydantic.dev/latest/
- https://docs.pydantic.dev/latest/api/pydantic_settings/
- https://docs.sqlalchemy.org/
- https://docs.sqlalchemy.org/en/20/
- https://www.uvicorn.org/
- https://restfulapi.net/
- https://learn.openapis.org/


## License

MIT