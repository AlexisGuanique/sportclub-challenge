from flask import Blueprint, jsonify, request
from datetime import datetime

from .db import crear_usuario, obtener_usuarios, eliminar_usuario, actualizar_usuario, db


usuario_bp = Blueprint('usuario_bp', __name__)


#! Ruta para obtener todos los registros
@usuario_bp.route('/usuarios', methods=['GET'])
def obtener_todos_los_usuarios():
    usuarios = db.session.query(db.usuarios).all()
    usuarios_dict = []
    for usuario in usuarios:
        usuarios_dict.append({
        'id': usuario.id,
        'nombre': usuario.nombre,
        'apellido': usuario.apellido,
        'dni': usuario.dni,
        'fecha_nacimiento':usuario.fecha_nacimiento,
        'localidad_gba': usuario.localidad_gba
        })
    return jsonify({'usuarios': usuarios_dict})
    
    
    usuarios = obtener_usuarios()
    return jsonify({'usuarios': usuarios})

#! Ruta para crear un nuevo usuario
@usuario_bp.route('/usuarios', methods=['POST'])
def crear_nuevo_usuario():
    data = request.json
    nuevo_usuario = crear_usuario(
        data['nombre'],
        data['apellido'],
        data['dni'],
        data['fecha_nacimiento'],
        data['localidad_gba'],
        request
    )
    return jsonify({'usuario': nuevo_usuario}), 201

#! Ruta para obtener los registros filtrados obteniendo los parametros
@usuario_bp.route('/usuarios/filtrar', methods=['GET'])
def filtrar_usuarios():
    nombre = request.args.get('nombre')
    apellido = request.args.get('apellido')
    dni = request.args.get('dni')
    fecha_desde = request.args.get('fecha_desde')
    fecha_hasta = request.args.get('fecha_hasta')
    localidad_gba = request.args.get('localidad_gba')

    consulta = db.usuarios.select()

    if nombre:
        consulta = consulta.where(db.usuarios.c.nombre == nombre)
    if apellido:
        consulta = consulta.where(db.usuarios.c.apellido == apellido)
    if dni:
        consulta = consulta.where(db.usuarios.c.dni == dni)
    if fecha_desde:
        fecha_desde_obj = datetime.strptime(fecha_desde, '%Y-%m-%d')
        consulta = consulta.where(db.usuarios.c.fecha_nacimiento >= fecha_desde_obj)
    if fecha_hasta:
        fecha_hasta_obj = datetime.strptime(fecha_hasta, '%Y-%m-%d')
        consulta = consulta.where(db.usuarios.c.fecha_nacimiento <= fecha_hasta_obj)
    if localidad_gba is not None:
        localidad_gba_bool = str(localidad_gba).lower() in ['true', '1']
        consulta = consulta.where(db.usuarios.c.localidad_gba == localidad_gba_bool)

    resultados = db.session.execute(consulta).fetchall()

    usuarios_filtrados = [
        {
            'id': usuario.id, 
            'nombre': usuario.nombre, 
            'apellido': usuario.apellido, 
            'dni': usuario.dni, 
            'fecha_nacimiento': usuario.fecha_nacimiento, 
            'localidad_gba': usuario.localidad_gba
        } for usuario in resultados
    ]

    return jsonify({'usuarios': usuarios_filtrados})



#! Ruta para modificar un usuario por medio de su id
@usuario_bp.route('/usuarios/<int:usuario_id>', methods=['PUT'])
def actualizar_un_usuario(usuario_id):
    data = request.json

    if not all(key in data for key in ('nombre', 'apellido', 'dni', 'fecha_nacimiento', 'localidad_gba')):
        return jsonify({'mensaje': 'Datos faltantes'}), 400

    try:
        fecha_nacimiento_obj = datetime.strptime(data['fecha_nacimiento'], '%Y-%m-%d')

        actualizar_usuario(
            usuario_id,
            data['nombre'],
            data['apellido'],
            data['dni'],
            fecha_nacimiento_obj,
            data['localidad_gba']
        )

        return jsonify({'mensaje': 'Usuario actualizado exitosamente'}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500



#! Ruta para eliminar un registro a travez del id
@usuario_bp.route('/usuarios/<int:usuario_id>', methods=['DELETE'])
def eliminar_un_usuario(usuario_id):
    resultado = eliminar_usuario(usuario_id)
    return jsonify(resultado)