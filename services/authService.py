from repository.userRepository import UserRepository

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

        return user.to_dict()