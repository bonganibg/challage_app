from src.models.challenge_model import ChallengeModel
from src.controllers.challenge_controller import ChallengeController

class ChallengeView():
    def __init__(self, username: str) -> None:
        self.__challenge_controller = ChallengeController()
        self.__username = username

    def display_menu(self):
        if (self.__username == 'admin'):
            self.admin_menu()
        else:
            self.general_user_menu()

        self.display_choice()

    def admin_menu(self):
        print('\n'.join([
            '1. Register Challenger',
            '2. Generate Report',
            '3. Delete Challenger',
            '4. View Challenges'
        ]))

    def general_user_menu(self):
        print( '\n'.join([
            '1. View My Challenges',
            '2. Create new challenge',
            '3. View Challenges made to me'            
        ]))

    def display_choice(self):
        choice = input('-> ')

        if (choice == '1'):
            self.display_challenges(
                self.__challenge_controller.get_mine(self.__username))

    def display_challenges(self, challenges: list[ChallengeModel]):
        for challenge in challenges:
            print(challenge)      

    


