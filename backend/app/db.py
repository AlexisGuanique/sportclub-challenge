from flask import jsonify
from flask_sqlalchemy import SQLAlchemy
import os
from datetime import datetime


db = SQLAlchemy()

#! Iniciar nuestra tabla y crearla
def init_db(app):
    #? Vamos a utilizar SQLite
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)


    db.usuarios = db.Table('usuarios',
        db.Column('id', db.Integer, primary_key=True),
        db.Column('nombre', db.String(50), nullable=False),
        db.Column('apellido', db.String(50), nullable=False),
        db.Column('dni', db.Integer, unique=True, nullable=False),
        db.Column('fecha_nacimiento', db.Date, nullable=False),
        db.Column('localidad_gba', db.Boolean, nullable=False)
    )

    if not os.path.exists('site.db'):
        with app.app_context():
            db.create_all()
            print('Base de datos creada')
            pass


#! Funcion que  nos permite crear un nuevo usuario
def crear_usuario(nombre, apellido, dni, fecha_nacimiento, localidad_gba, request):

    fecha_nacimiento_string = request.get_json()["fecha_nacimiento"]
    fecha_nacimiento_obj = datetime.strptime(fecha_nacimiento_string, '%Y-%m-%d')

    #? Insertar el usuario en la base de datos
    with db.session.begin():
        db.session.execute(
            db.usuarios.insert().values(nombre=nombre, apellido=apellido, dni=dni, fecha_nacimiento=fecha_nacimiento_obj, localidad_gba=localidad_gba)
        )

    #? Devolver el usuario creado
    return {'id': db.session.query(db.usuarios).filter_by(dni=dni).first().id, 'nombre': nombre, 'apellido': apellido, 'dni': dni, 'fecha_nacimiento': fecha_nacimiento, 'localidad_gba': localidad_gba}




#! Obtener todos los usuarios de mi base de datos
def obtener_usuarios():
    usuarios = db.session.query(db.metadata.tables['usuarios']).all()
    return usuarios



#! Modificar un usuario ya existente
def actualizar_usuario(usuario_id, nombre, apellido, dni, fecha_nacimiento, localidad_gba):

    if isinstance(fecha_nacimiento, str):
        fecha_nacimiento_obj = datetime.strptime(fecha_nacimiento, '%Y-%m-%d')
    else:
        fecha_nacimiento_obj = fecha_nacimiento

    with db.session.begin():
        usuario = db.session.query(db.usuarios).filter(db.usuarios.c.id == usuario_id).first()
        
        if usuario is None:
            return {'mensaje': 'Usuario no encontrado'}

        db.session.execute(
            db.usuarios.update().values(
                nombre=nombre,
                apellido=apellido,
                dni=dni,
                fecha_nacimiento=fecha_nacimiento_obj,
                localidad_gba=localidad_gba
            ).where(db.usuarios.c.id == usuario_id)
        )
    
    return {'mensaje': 'Usuario actualizado exitosamente'}



#! Eliminar un usuario
def eliminar_usuario(usuario_id):
    with db.session.begin():
        db.session.execute(db.usuarios.delete().where(db.usuarios.c.id == usuario_id))

    return {'mensaje': 'Usuario eliminado exitosamente'}




