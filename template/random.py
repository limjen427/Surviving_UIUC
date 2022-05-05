'''
Probability Calculator
gpa(0-4.0), internship(0-100), research(0-100)

'''
import random


def decision(phase, isJob, gpa, internship, research):
    num = 0
    result = False

    if phase == 1:
        # after Sophomore, checking intership/research eligibility
        return gpa >= 3.5

    elif phase == 2:
        # after Senior, checking intership/research eligibility with internship & research points
        if isJob:
            # job: gpa -> 45%
            num = (gpa / 4.0) * 0.45 + (internship / 100)
            return random_calculator(num)
        else:
            # grad school: gpa -> 75%
            num = (gpa / 4.0) * 0.75 + (research / 100)
            return random_calculator(num)

    elif phase == 3:
        # after graduate, calculating total score
        if isJob:
            # job: gpa -> 30%
            num = (gpa / 4.0) * 0.3 + (internship / 100)
            result = random_calculator(num)
        else:
            # grad school: gpa -> 60%
            num = (gpa / 4.0) * 0.6 + (research / 100)
            result = random_calculator(num)


    if result and isJob:
        return "Congrats! You get your deam job!"
    elif result and not isJob:
        return "Congrats! You made your deam grad school!"
    return "There were several applications submitted for this position, and after careful review, unfortunately, we have decided to pursue a different candidate whose experience and skills more closely meet the needs of this particular role."


def random_calculator(prob):
    # random.random() -> [0,1)
    return random.random() < prob
