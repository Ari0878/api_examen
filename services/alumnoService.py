from repository.AlumnoRepository import AlumnoRepository
from entorno.extensions import db
from datetime import datetime

class AlumnoService:

    @staticmethod
    def create(data):
        return AlumnoRepository.create(
            data['nombre'],
            data['apellido_paterno'],
            data['apellido_materno'],
            data['matricula'],
            data['correo']
        ).to_dict()

    @staticmethod
    def get_all():
        alumnos = AlumnoRepository.get_all()
        return [a.to_dict() for a in alumnos]

    @staticmethod
    def get_by_id(id):
        alumno = AlumnoRepository.find_by_id(id)
        if not alumno:
            return {"error": "Alumno no encontrado"}
        return alumno.to_dict()

    @staticmethod
    def update(id, data):
        alumno = AlumnoRepository.find_by_id(id)

        if not alumno:
            return {"error": "Alumno no encontrado"}

        if "nombre" in data:
            alumno.nombre = data["nombre"]
        if "apellido_paterno" in data:
            alumno.apellido_paterno = data["apellido_paterno"]
        if "apellido_materno" in data:
            alumno.apellido_materno = data["apellido_materno"]
        if "matricula" in data:
            alumno.matricula = data["matricula"]
        if "correo" in data:
            alumno.correo = data["correo"]

        db.session.commit()

        return alumno.to_dict()

    @staticmethod
    def delete(id):
        alumno = AlumnoRepository.find_by_id(id)

        if not alumno:
            return {"error": "Alumno no encontrado"}

        AlumnoRepository.delete(alumno)
        return {"message": "Alumno eliminado"}

    @staticmethod
    def get_by_fecha_range(fecha_inicio, fecha_fin):
        alumnos = AlumnoRepository.get_by_fecha_range(fecha_inicio, fecha_fin)
        return [a.to_dict() for a in alumnos]