from models.user import User
from entorno.extensions import db

class UserRepository:
    @staticmethod 
    def create( email, password):
        user = User(
        email=email
    )

        user.set_password(password)  

        db.session.add(user)
        db.session.commit()
        return user

    @staticmethod
    def find_user_by_id(id):
        return User.query.get(id)
    
    @staticmethod
    def find_by_user(email):
        return User.query.filter_by(email=email).first()
    
    @staticmethod
    def find_by_email(email):
        return User.query.filter_by(email=email).first()