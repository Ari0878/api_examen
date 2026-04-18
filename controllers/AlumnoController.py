from services.alumnoService import AlumnoService
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from flasgger import swag_from

alumno_bp = Blueprint('alumnos', __name__)

# 🔐 SOLO protegemos las rutas que modifican datos

@alumno_bp.route('', methods=['POST'])
@jwt_required()
@swag_from({
    'tags': ["Alumnos"],
    'security': [{'BearerAuth': []}],
    'consumes': ['application/json'],
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'nombre': {'type': 'string'},
                    'apellido_paterno': {'type': 'string'},
                    'apellido_materno': {'type': 'string'},
                    'matricula': {'type': 'string'},
                    'correo': {'type': 'string'}
                },
                'required': ['nombre', 'apellido_paterno', 'apellido_materno', 'matricula', 'correo']
            }
        }
    ],
    'responses': {
        201: {'description': 'Alumno creado'},
        400: {'description': 'Error en datos'}
    }
})
def create_alumno():
    data = request.get_json()

    if not data:
        return jsonify({"message": "No se enviaron datos"}), 400

    result = AlumnoService.create(data)

    if isinstance(result, dict) and "error" in result:
        return jsonify(result), 400

    return jsonify(result), 201


# 🔓 GET sin token
@alumno_bp.route('', methods=['GET'])
@swag_from({
    'tags': ["Alumnos"],
    'parameters': [
        {
            'name': 'fecha_inicio',
            'in': 'query',
            'type': 'string',
            'required': False,
            'description': 'Fecha de inicio en formato YYYY-MM-DD'
        },
        {
            'name': 'fecha_fin',
            'in': 'query',
            'type': 'string',
            'required': False,
            'description': 'Fecha de fin en formato YYYY-MM-DD'
        }
    ],
    'responses': {
        200: {'description': 'Lista de alumnos'},
        400: {'description': 'Error en fechas'}
    }
})
def get_all_alumnos():
    fecha_inicio = request.args.get('fecha_inicio')
    fecha_fin = request.args.get('fecha_fin')

    if fecha_inicio or fecha_fin:
        if not fecha_inicio or not fecha_fin:
            return jsonify({"message": "Se requieren fecha_inicio y fecha_fin"}), 400

        result = AlumnoService.get_by_fecha_range(fecha_inicio, fecha_fin)

        if isinstance(result, dict) and "error" in result:
            return jsonify(result), 400

        return jsonify(result), 200

    result = AlumnoService.get_all()
    return jsonify(result), 200


@alumno_bp.route('/<int:id>', methods=['GET'])
@swag_from({
    'tags': ["Alumnos"],
    'parameters': [
        {
            'name': 'id',
            'in': 'path',
            'type': 'integer',
            'required': True
        }
    ],
    'responses': {
        200: {'description': 'Alumno encontrado'},
        404: {'description': 'Alumno no encontrado'}
    }
})
def get_alumno_by_id(id):
    result = AlumnoService.get_by_id(id)

    if isinstance(result, dict) and "error" in result:
        return jsonify(result), 404

    return jsonify(result), 200


# 🔐 PROTEGIDO
@alumno_bp.route('/<int:id>', methods=['PUT'])
@jwt_required()
@swag_from({
    'tags': ["Alumnos"],

    'security': [{'BearerAuth': []}],
    'consumes': ['application/json'],
    'parameters': [
        {
            'name': 'id',
            'in': 'path',
            'type': 'integer',
            'required': True
        },
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'nombre': {'type': 'string'},
                    'apellido_paterno': {'type': 'string'},
                    'apellido_materno': {'type': 'string'},
                    'matricula': {'type': 'string'},
                    'correo': {'type': 'string'}
                }
            }
        }
    ],
    'responses': {
        200: {'description': 'Alumno actualizado'},
        404: {'description': 'Alumno no encontrado'}
    }
})
def update_alumno(id):
    data = request.get_json()

    if not data:
        return jsonify({"message": "No se enviaron datos"}), 400

    result = AlumnoService.update(id, data)

    if isinstance(result, dict) and "error" in result:
        return jsonify(result), 404

    return jsonify(result), 200


# 🔐 PROTEGIDO
@alumno_bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
@swag_from({
    'tags': ["Alumnos"],
<<<<<<< HEAD
    'security': [{'BearerAuth': []}],
=======
>>>>>>> 1806d9d17eb9cc09e406ac8eba99297eeee751b1
    'parameters': [
        {
            'name': 'id',
            'in': 'path',
            'type': 'integer',
            'required': True
        }
    ],
    'responses': {
        200: {'description': 'Alumno eliminado'},
        404: {'description': 'Alumno no encontrado'}
    }
})
def delete_alumno(id):
    result = AlumnoService.delete(id)

    if isinstance(result, dict) and "error" in result:
        return jsonify(result), 404

    return jsonify({"message": "Alumno eliminado correctamente"}), 200