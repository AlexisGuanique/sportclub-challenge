# Sportclub Challenge

## Descripcion de proyecto:

La aplicación Sport Club Challenge es una aplicación que nos permite visualizar una lista de clientes, en la cual se observan los campos: nombre, apellido, DNI, fecha de nacimiento.

Además nos permite filtrar dicha tabla por fecha de nacimiento y si es de GBA o no.

El challenge cuenta también con un backend creado para poder interactuar con la API a través de varias rutas definidas. Además cuenta con una base de datos usuarios que tiene los campos: nombre, apellido, DNI, fecha_nacimiento y localidad_gba

Cabe destacar también que la aplicación cuenta con su CRUD para la tabla usuarios, está dockerizada y mantiene la paleta de colores de la aplicación web oficial de Sport Club.

## Tecnologias utilizadas:

Para el Backend utilicé el lenguaje Python con su framework Flask; además para la construcción de la base de datos utilicé la ORM que nos proporciona SQLAlchemy y la base de datos está creada con SQLite.

Para el frontend utilicé el lenguaje JavaScript con su Librería React, para las peticiones HTTP utilicé axios. Para los estilos utilicé Material UI.

Ambas aplicaciones están Dockerizadas, ambas con su respectivo Dockerfile para la imagen de cada una y luego cada contenedor está administrado con un docker-compose.yml.

Lista de tecnologías por versiones:

- Backend:

    - Python = v3.10.11
    - Flask = 3.0.0
    - SQLAlchemy = 22.0.33


- Frontend:

    - React = v18.2.0
    - vite = 5.0.0
    - Material UI = v5.14.20
    - axios = v1.6.2

Node = v20.8.1
Docker = v24.0.6

## Ejecucion:

### Con Docker:

Requerimiento: Debes tener Docker instalado en tu PC.

Pasos para ejecución del proyecto:

1 . Clonar el repositorio desde GitHub:


```
    git clone https://github.com/AlexisGuanique/sportclub-challenge.git

```
2 . Navega hasta el repositorio raíz del proyecto a la altura del docker-compose.yml y ejecuta el siguiente comando:

```
    docker-compose up --build
```

Una vez realizado los comandos que se especifican anteriormente podrás acceder a la aplicación de manera local. 

Al frontend desde el puerto 5002 de la siguiente manera:

http://localhost:5002

Y al backend desde el puerto 5000 de la siguiente manera:

http://localhost:5000/usuarios

### Sin Docker, de manera individual (opcional, recomiendo hacer todo de la manera dockerizada):


### Backend:

1 . Clonar el repositorio desde GitHub:

```
    git clone https://github.com/AlexisGuanique/sportclub-challenge.git

```

2 . Navega hasta el directorio backend y crea un entorno virtual con el siguiente comando:

```
    python -m venv <nombre de tu entorno>

```

3 . Una vez creado el entorno, actívalo e instala las dependencias necesarias para correr tu aplicación con los siguientes comandos (dichas dependencias están en el requirements.txt):


```
    source <nombre del entorno>/Scripts/activate
    pip install -r requirements.txt

```

4 . Seguida mente indícale a Flask el nombre del ejecutable que corre tu aplicación como una variable de entorno y luego corre tu aplicación con los siguientes comandos:

```
    export FLASK_APP=__init__
    flask run
```

Con estos pasos deberías poder visualizar tu backend de manera local en el puerto 5000 con la siguiente URL: http://localhost:5000/usuarios (Por defecto Flask muestra siempre en el puerto 5000, verificar si tu caso es el mismo)

### Frontend:

1 . Clonar el repositorio desde GitHub:

```
    git clone https://github.com/AlexisGuanique/sportclub-challenge.git

```

2 . Navega hasta el directorio frontend instala las dependencias necesarias para tu frontend y corre tu aplicación con los siguientes comandos:

```
    npm install
    npm run dev

```

Con estos pasos podrás visualizar tu aplicación de manera local en el puerto que vite te asigne.


# Características principales de la aplicación:

- La aplicación cuenta con su CRUD.
- La aplicación está dockerizada.
- La aplicación cuenta con su readme bien detallado.
- La aplicación mantiene el diseño y paleta de colores de la página oficial de sport club. 
- Se utiliza la herramienta swagger para realizar documentacion de la API (se ingresa a la misma a travez de la url: http://localhost:5000/swagger)



Alexis Guanique. 
