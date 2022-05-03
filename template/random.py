'''
확률계산기: 오퍼받을 확률
gpa(0-4.0), internship(0-100), research(0-100)

'''
import random


def decision(isJob, gpa, internship, research):
    num = 0
    result = False
    if isJob:
        # job: gpa -> 30%
        num = (gpa / 4.0) * 0.3 + (internship / 100)
        result = random_calculator(num)
    else:
        # grad school: gpa -> 60%
        num = (gpa / 4.0) * 0.6 + (research / 100)
        result = random_calculator(num)

    if result and isJob == "job":
        return "Congrats! You get your deam job!"
    elif result and not isJob == "grad":
        return "Congrats! You made your deam grad school!"
    return "There were several applications submitted for this position, and after careful review, unfortunately, we have decided to pursue a different candidate whose experience and skills more closely meet the needs of this particular role."


def random_calculator(prob):
    # random.random() -> [0,1)
    # prob가 크면 클수록 random.random() 숫자가 true나오는 숫자 범위가 커진다
    return random.random() < prob
