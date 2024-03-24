from src.models.user_model import UserModel
from src.repositories.file_access_repo import FileAccessRepo
from constants import Constants


class UserService():    
    def __init__(self) -> None:
        self.__file_access = FileAccessRepo(Constants.USER_FILE_LOCATION)