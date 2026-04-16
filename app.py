from flask import Flask
from controllers.AuthController import auth_bp
from controllers.AlumnoController import alumno_bp
from entorno.extensions import db, migrate, swagger, jwt
from entorno.config import Config


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    swagger.init_app(app)
    jwt.init_app(app)

    from models.user import User
    from models.alumnos import Alumno

    app.register_blueprint(auth_bp)
    app.register_blueprint(alumno_bp)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)