class ChallengeModel():
    def __init__(self, challenger, name, rules, challenging,
                 created_on, deadline, accepted, winner) -> None:
        
        self.challenger = challenger
        self.name = name
        self.rules = rules
        self.challenging = challenging
        self.created_on = created_on
        self.deadline = deadline
        self.accepted = accepted
        self.winner = winner

    def update_overdue(self):
        pass

    def is_overdue(self):
        pass

    def accept_challenge(self):
        pass

    def reject_challenge(self):
        pass

    def set_winner(self):
        pass
    
    def __str__(self) -> str:
        return '\n'.join([
            f'Challenger: {self.challenger}',
            f'Challenge: {self.name}',
            f'Accepted: {self.accepted}'
        ])