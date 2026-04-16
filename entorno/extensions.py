from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flasgger import Swagger
from flask_jwt_extended import JWTManager   

db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()   


swagger_template = {
    "swagger": "2.0",
    "info": {
        "title": "Api",
        "description": "api del 83",
        "version": "1.0"
    },
    "securityDefinitions": {
        "BearerAuth": {
            "type": "apiKey",
            "name": "Authorization",
            "in": "header",
            "description": "Aqui va Bearer <TOKEN>"
        }
    }
}

swagger = Swagger(template=swagger_template)