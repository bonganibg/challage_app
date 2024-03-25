from src.repositories.file_access_repo import FileAccessRepo
from src.models.challenge_model import ChallengeModel
from constants import Constants

class ChallengeService():
    def __init__(self):
        self.__file_repo = FileAccessRepo(Constants.CHALLENGES_FILE_LOCATION)

        self.__all_challenges: list[ChallengeModel] = []

        for challenge in self.__file_repo.read():
            self.__all_challenges.append(
                self.__convert_line_to_challenge_objects(challenge))

    def __convert_line_to_challenge_objects(self, line: str) -> ChallengeModel:
        line = tuple(line.split(';'))
        return ChallengeModel(*line)

    def get_mine(self, username: str) -> list:
        output = []

        for challenge in self.__all_challenges:
            if challenge.challenger == username:
                output.append(challenge)

        return output
