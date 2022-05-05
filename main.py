from template.screen import Screen
from template.quiz import *


def main():
    is_playing = True
    phase = 0
    GameScreen = Screen()
    GameScreen.makeScreen()

    internship_score = 0
    research_score = 0
    point = 0

    while is_playing:
        print(GameScreen.screen)
        match phase:
            case 0:
                if not GameScreen.name:
                    userInput = input("Please type your name: ")
                    GameScreen.updateName(userInput)

                if not GameScreen.major:
                    userInput = input("Please type your major (example CS): ")
                    GameScreen.updateMajor(userInput)

                GameScreen.updateGrade("Freshman")

                GameScreen.updategpa(4.0)

                GameScreen.makeScreen()

                phase += 1
                continue
            case 1:
                GameScreen.updateDialogue("You are a Freshman!")

                GameScreen.makeScreen()

                print(GameScreen.screen)

                userInput = input("press any key to continue")

                GameScreen.updateDialogue("What course are you going to take?")
                choices = [f"{GameScreen.major} 125",
                           f"{GameScreen.major} 100",
                           f"{GameScreen.major} 165"]
                GameScreen.updateChoices(choices)

                GameScreen.makeScreen()
                print(GameScreen.screen)

                userInput = int(input("press 1, 2, or 3 to choose: "))

                GameScreen.updateChoices(None)
                GameScreen.updateDialogue(
                    f"Welcome to course {choices[userInput-1]}!"
                )

                GameScreen.makeScreen()
                print(GameScreen.screen)

                GameScreen.updateDialogue("Its midterm quiz time!")

                GameScreen.makeScreen()
                print(GameScreen.screen)

                userInput = input("press any key to continue")

                Qs = []
                Q_c = []
                Q_s = []

                for key, val in l100.items():
                    Qs.append(key)
                    for v in val.values():
                        Q_c.append(v[0])
                        Q_s.append(v[1])

                GameScreen.updateDialogue(Qs[0])
                GameScreen.updateChoices(Q_c[:3])

                GameScreen.makeScreen()
                print(GameScreen.screen)

                userInput = int(input("Choose the Correct Answer!: "))

                point += Q_s[userInput-1]

                GameScreen.updateDialogue(
                    f"You got {Q_s[userInput-1]} points!")
                GameScreen.updateChoices(None)

                GameScreen.makeScreen()
                print(GameScreen.screen)

                userInput = input("Press any key to continue")

                GameScreen.updateDialogue("Its final quiz time!")

                GameScreen.makeScreen()
                print(GameScreen.screen)

                userInput = input("press any key to continue")

                GameScreen.updateDialogue(Qs[1])
                GameScreen.updateChoices(Q_c[3:])

                GameScreen.makeScreen()
                print(GameScreen.screen)

                userInput = int(input("Choose the Correct Answer!: ")) * 2

                point += Q_s[userInput-1]

                GameScreen.updateDialogue(
                    f"You got {Q_s[userInput-1]} points!")
                GameScreen.updateChoices(None)

                GameScreen.makeScreen()
                print(GameScreen.screen)

                userInput = input("Press any key to continue")

                GameScreen.updategpa(chooseGrade(point))

                GameScreen.updateDialogue("Congrats on end of Freshman!")

                GameScreen.makeScreen()
                print(GameScreen.screen)

                userInput = input("Press any key to continue")

                phase += 1
                continue
            case 2:
                GameScreen.updateGrade("Sophomore")
                GameScreen.updateDialogue("You are a Sophomore!")

                GameScreen.makeScreen()

                print(GameScreen.screen)

                userInput = input("press any key to continue")

                GameScreen.updateDialogue("What course are you going to take?")
                choices = [f"{GameScreen.major} 255",
                           f"{GameScreen.major} 231",
                           f"{GameScreen.major} 374"]
                GameScreen.updateChoices(choices)

                GameScreen.makeScreen()
                print(GameScreen.screen)

                userInput = int(input("press 1, 2, or 3 to choose: "))

                GameScreen.updateChoices(None)
                GameScreen.updateDialogue(
                    f"Welcome to course {choices[userInput-1]}!")

                GameScreen.makeScreen()
                print(GameScreen.screen)

                GameScreen.updateDialogue("Its midterm quiz time!")

                GameScreen.makeScreen()
                print(GameScreen.screen)

                userInput = input("press any key to continue")

                Qs = []
                Q_c = []
                Q_s = []

                for key, val in l200.items():
                    Qs.append(key)
                    for v in val.values():
                        Q_c.append(v[0])
                        Q_s.append(v[1])

                GameScreen.updateDialogue(Qs[0])
                GameScreen.updateChoices(Q_c[:3])

                GameScreen.makeScreen()
                print(GameScreen.screen)

                userInput = int(input("Choose the Correct Answer!: "))

                point += Q_s[userInput-1]

                GameScreen.updateDialogue(
                    f"You got {Q_s[userInput-1]} points!")
                GameScreen.updateChoices(None)

                GameScreen.makeScreen()
                print(GameScreen.screen)

                userInput = input("Press any key to continue")

                GameScreen.updateDialogue("Its final quiz time!")

                GameScreen.makeScreen()
                print(GameScreen.screen)

                userInput = input("press any key to continue")

                GameScreen.updateDialogue(Qs[1])
                GameScreen.updateChoices(Q_c[3:])

                GameScreen.makeScreen()
                print(GameScreen.screen)

                userInput = int(input("Choose the Correct Answer!: ")) * 2

                point += Q_s[userInput-1]

                GameScreen.updateDialogue(
                    f"You got {Q_s[userInput-1]} points!")
                GameScreen.updateChoices(None)

                GameScreen.makeScreen()
                print(GameScreen.screen)

                userInput = input("Press any key to continue")

                point /= 2
                GameScreen.updategpa(chooseGrade(point))

                GameScreen.updateDialogue("Congrats on end of Sophomore!")

                GameScreen.makeScreen()
                print(GameScreen.screen)

                userInput = input("Press any key to continue")

                phase += 1
                continue
            case 3:
                GameScreen.updateGrade("Junior")
                GameScreen.updateDialogue("You are a Junior!")

                GameScreen.makeScreen()

                print(GameScreen.screen)

                userInput = input("press any key to continue")

                GameScreen.updateDialogue("What course are you going to take?")
                choices = [f"{GameScreen.major} 411",
                           f"{GameScreen.major} 241",
                           f"{GameScreen.major} 351"]
                GameScreen.updateChoices(choices)

                GameScreen.makeScreen()
                print(GameScreen.screen)

                userInput = int(input("press 1, 2, or 3 to choose: "))

                GameScreen.updateChoices(None)
                GameScreen.updateDialogue(
                    f"Welcome to course {choices[userInput-1]}!")

                GameScreen.makeScreen()
                print(GameScreen.screen)

                GameScreen.updateDialogue("Its midterm quiz time!")

                GameScreen.makeScreen()
                print(GameScreen.screen)

                userInput = input("press any key to continue")

                Qs = []
                Q_c = []
                Q_s = []

                for key, val in l300.items():
                    Qs.append(key)
                    for v in val.values():
                        Q_c.append(v[0])
                        Q_s.append(v[1])

                GameScreen.updateDialogue(Qs[0])
                GameScreen.updateChoices(Q_c[:3])

                GameScreen.makeScreen()
                print(GameScreen.screen)

                userInput = int(input("Choose the Correct Answer!: "))

                point += Q_s[userInput-1]

                GameScreen.updateDialogue(
                    f"You got {Q_s[userInput-1]} points!")
                GameScreen.updateChoices(None)

                GameScreen.makeScreen()
                print(GameScreen.screen)

                userInput = input("Press any key to continue")

                GameScreen.updateDialogue("Its final quiz time!")

                GameScreen.makeScreen()
                print(GameScreen.screen)

                userInput = input("press any key to continue")

                GameScreen.updateDialogue(Qs[1])
                GameScreen.updateChoices(Q_c[3:])

                GameScreen.makeScreen()
                print(GameScreen.screen)

                userInput = int(input("Choose the Correct Answer!: ")) * 2

                point += Q_s[userInput-1]

                GameScreen.updateDialogue(
                    f"You got {Q_s[userInput-1]} points!")
                GameScreen.updateChoices(None)

                GameScreen.makeScreen()
                print(GameScreen.screen)

                userInput = input("Press any key to continue")

                point /= 2
                GameScreen.updategpa(chooseGrade(point))

                GameScreen.updateDialogue("Congrats on end of Junior!")

                GameScreen.makeScreen()
                print(GameScreen.screen)

                userInput = input("Press any key to continue")

                phase += 1
                continue
            case 4:
                GameScreen.updateGrade("Senior")
                GameScreen.updateDialogue("You are a Senior!")

                GameScreen.makeScreen()

                print(GameScreen.screen)

                userInput = input("press any key to continue")

                GameScreen.updateDialogue("What course are you going to take?")
                choices = [f"{GameScreen.major} 415",
                           f"{GameScreen.major} 430",
                           f"{GameScreen.major} 441"]
                GameScreen.updateChoices(choices)

                GameScreen.makeScreen()
                print(GameScreen.screen)

                userInput = int(input("press 1, 2, or 3 to choose: "))

                GameScreen.updateChoices(None)
                GameScreen.updateDialogue(
                    f"Welcome to course {choices[userInput-1]}!"
                )

                GameScreen.makeScreen()
                print(GameScreen.screen)

                GameScreen.updateDialogue("Its midterm quiz time!")

                GameScreen.makeScreen()
                print(GameScreen.screen)

                userInput = input("press any key to continue")

                Qs = []
                Q_c = []
                Q_s = []

                for key, val in l400.items():
                    Qs.append(key)
                    for v in val.values():
                        Q_c.append(v[0])
                        Q_s.append(v[1])

                GameScreen.updateDialogue(Qs[0])
                GameScreen.updateChoices(Q_c[:3])

                GameScreen.makeScreen()
                print(GameScreen.screen)

                userInput = int(input("Choose the Correct Answer!: "))

                point += Q_s[userInput-1]

                GameScreen.updateDialogue(
                    f"You got {Q_s[userInput-1]} points!")
                GameScreen.updateChoices(None)

                GameScreen.makeScreen()
                print(GameScreen.screen)

                userInput = input("Press any key to continue")

                GameScreen.updateDialogue("Its final quiz time!")

                GameScreen.makeScreen()
                print(GameScreen.screen)

                userInput = input("press any key to continue")

                GameScreen.updateDialogue(Qs[1])
                GameScreen.updateChoices(Q_c[3:])

                GameScreen.makeScreen()
                print(GameScreen.screen)

                userInput = int(input("Choose the Correct Answer!: ")) * 2

                point += Q_s[userInput-1]

                GameScreen.updateDialogue(
                    f"You got {Q_s[userInput-1]} points!")
                GameScreen.updateChoices(None)

                GameScreen.makeScreen()
                print(GameScreen.screen)

                userInput = input("Press any key to continue")

                point /= 2
                GameScreen.updategpa(chooseGrade(point))

                GameScreen.updateDialogue("Congrats on end of Senior!")

                GameScreen.makeScreen()
                print(GameScreen.screen)

                userInput = input("Press any key to continue")

                phase += 1
                continue
            case 5:
                if GameScreen.gpa == "F":
                    GameScreen.updateDialogue("You have failed to graduate!")
                else:
                    GameScreen.updateDialogue(
                        f"You have graduated with {GameScreen.gpa}!")

                GameScreen.makeScreen()
                print(GameScreen.screen)

                userInput = input("Press any key to close the game.")
                break

        endGame = input("Press q to end game.")
        if endGame == "q":
            break


def chooseGrade(point):
    if point >= 170:
        return "A"
    elif point >= 150:
        return "B"
    elif point >= 100:
        return "C"
    elif point >= 50:
        return "D"
    else:
        return "F"


if __name__ == '__main__':
    main()
