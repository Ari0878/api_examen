from services.authService import authService
from flask import Blueprint, jsonify, request
from flasgger import swag_from

auth_bp = Blueprint('auth', __name__, url_prefix='/api/auth')



@auth_bp.route('/register', methods=['POST'])
@swag_from({
    'tags': ["Auth"],
    'consumes': ['application/json'],
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'email': {'type': 'string'},
                    'password': {'type': 'string'},
                },
                'required': ['email', 'password']
            }
        }
    ],
    'responses': {
        201: {'description': 'Usuario creado'}
    }
})
def register():
    data = request.get_json()

    if not data:
        return jsonify({"message": "No se enviaron datos"}), 400

    if not data.get("email") or not data.get("password"):
        return jsonify({"message": "Faltan campos obligatorios"}), 400

    user = authService.register(
        data['email'],
        data['password']
    )

    return jsonify(user.to_dict()), 201



@auth_bp.route('/register/<int:id>', methods=['GET'])
def get_user_by_id(id):
    user = authService.find_by_id(id)

    if not user:
        return jsonify({"message": "Usuario no encontrado"}), 404

    return jsonify(user.to_dict()), 200



@auth_bp.route('/login', methods=['POST'])
@swag_from({
    'tags': ["Auth"],
    'consumes': ['application/json'],
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'email': {'type': 'string'},
                    'password': {'type': 'string'},
                },
                'required': ['email', 'password']
            }
        }
    ],
    'responses': {
        200: {'description': 'Login exitoso'},
        401: {'description': 'Credenciales inválidas'}
    }
})
def login():
    data = request.get_json()

    if not data:
        return jsonify({"message": "No se enviaron datos"}), 400

    if not data.get("email") or not data.get("password"):
        return jsonify({"message": "Faltan credenciales"}), 400

    result = authService.login(
        data['email'],
        data['password']
    )

    if not result:
        return jsonify({"message": "Credenciales inválidas"}), 401

    return jsonify({
        "message": "Login exitoso",
        "user": result
    }), 200