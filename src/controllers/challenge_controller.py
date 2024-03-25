from src.models.challenge_model import ChallengeModel
from src.services.challenge_service import ChallengeService


class ChallengeController():
    '''
    write what you need to write
    '''
    
    def __init__(self):
        self.challenge_service = ChallengeService()

    def get_mine(self, username: str) -> list:
        return self.challenge_service.get_mine(username)
