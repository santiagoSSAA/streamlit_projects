from db.user_repository import create_users_table, add_user as db_add_user, verify_user as db_verify_user
from utils.security import hash_password

class UserService:
    @staticmethod
    def create_users_table():
        create_users_table()

    @staticmethod
    def add_user(username, password):
        hashed_password = hash_password(password)
        return db_add_user(username, hashed_password)

    @staticmethod
    def verify_user(username, password):
        hashed_password = hash_password(password)
        return db_verify_user(username, hashed_password) 