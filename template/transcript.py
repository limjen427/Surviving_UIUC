class Transcript:
    def __init__(self):
        self.maximum_possible_score = 0
        self.total_earned_score = 0

    def add_record(self, earned_credit, full_credit):
        self.maximum_possible_score += full_credit
        self.total_earned_score += earned_credit

    @property
    def gpa(self):
        if self.maximum_possible_score == 0:
            return 4.0
        return (self.total_earned_score / self.maximum_possible_score) * 4
