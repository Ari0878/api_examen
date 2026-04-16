from models.alumnos import Alumno
from entorno.extensions import db
from datetime import datetime

class AlumnoRepository:

    @staticmethod
    def create(nombre, apellido_paterno, apellido_materno, matricula, correo):
        alumno = Alumno(
            nombre=nombre,
            apellido_paterno=apellido_paterno,
            apellido_materno=apellido_materno,
            matricula=matricula,
            correo=correo
        )

        db.session.add(alumno)
        db.session.commit()
        return alumno

    @staticmethod
    def get_all():
        return Alumno.query.all()

    @staticmethod
    def find_by_id(id):
        return Alumno.query.get(id)

    @staticmethod
    def find_by_matricula(matricula):
        return Alumno.query.filter_by(matricula=matricula).first()

    @staticmethod
    def get_by_fecha_range(fecha_inicio, fecha_fin):
        return Alumno.query.filter(
            Alumno.fecha_alta.between(fecha_inicio, fecha_fin)
        ).all()
    
    @staticmethod
    def delete(alumno):
        db.session.delete(alumno)
        db.session.commit()