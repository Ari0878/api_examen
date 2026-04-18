from repository.userRepository import UserRepository
from flask_jwt_extended import create_access_token

class authService:

    @staticmethod
    def register(email, password):
        user = UserRepository.create(email, password)
        return user

    @staticmethod
    def find_by_id(id):
        return UserRepository.find_user_by_id(id)

    @staticmethod
    def login(email, password):
        user = UserRepository.find_by_email(email)

        if not user:
            return None

        if not user.check_password(password):
            return None

        access_token = create_access_token(identity=user.id)
        if isinstance(access_token, bytes):
            access_token = access_token.decode('utf-8')

        return {
            'access_token': access_token,
            'user': user.to_dict()
        }