from template.screen import Screen
from template.quiz import Quiz
from template.transcript import Transcript


def main():
    is_playing = True
    phase = -1
    GameScreen = Screen()
    GameScreen.makeScreen()

    quiz = Quiz()
    transcript = Transcript()
    research_score = 0
    internship_score = 0

    doing_research = 0
    doing_internship = 0

    task_queue = []
    ignore_input = False
    while is_playing:
        GameScreen.updategpa(transcript.gpa)
        task = None
        if task_queue:
            task = task_queue.pop(0)

            GameScreen.updateDialogue(task['question'])
            options = [option['option'] for option in task['options']]
            GameScreen.updateChoices(options)
        else:
            phase += 1
            match phase:
                case 0:
                    pass
                case 1:
                    GameScreen.updateGrade("Freshman")
                    GameScreen.updateDialogue("It's Freshman year! What course are you going to take?")
                    choices = [f"{GameScreen.major} 125",
                               f"{GameScreen.major} 100",
                               f"{GameScreen.major} 165"]
                    GameScreen.updateChoices(choices)
                    ignore_input = True
                case 2:
                    task_queue += quiz.l100
                    task = task_queue.pop(0)
                    GameScreen.updateDialogue(task['question'])
                    options = [option['option'] for option in task['options']]
                    GameScreen.updateChoices(options)
                case 3:
                    if transcript.gpa >= 3.0:
                        GameScreen.updateDialogue(
                            "HIGH GPA! You can choose to do internship or research"
                        )
                        GameScreen.updateChoices(["research", 'internship', '한국가서 놀기 ㅋㅋ'])
                    else:
                        GameScreen.updateDialogue(
                            "LOW GPA... You didn't get to do anything this summer."
                        )
                        GameScreen.updateChoices([])
                case 4:
                    GameScreen.updateGrade("Sophomore")
                    GameScreen.updateDialogue("It's Sophomore year! What course are you going to take?")
                    choices = [f"{GameScreen.major} 255",
                               f"{GameScreen.major} 231",
                               f"{GameScreen.major} 374"]
                    GameScreen.updateChoices(choices)
                    ignore_input = True
                case 5:
                    task_queue += quiz.l200
                    task = task_queue.pop(0)
                    GameScreen.updateDialogue(task['question'])
                    options = [option['option'] for option in task['options']]
                    GameScreen.updateChoices(options)
                case 6:
                    if transcript.gpa >= 3.0:
                        GameScreen.updateDialogue(
                            "HIGH GPA! You can choose to do internship or research"
                        )
                        GameScreen.updateChoices(["research", 'internship', '한국가서 놀기 ㅋㅋ'])
                    else:
                        GameScreen.updateDialogue(
                            "LOW GPA... You didn't get to do anything this summer."
                        )
                        GameScreen.updateChoices([])
                case 7:
                    GameScreen.updateGrade("Junior")
                    GameScreen.updateDialogue("It's Junior year! What course are you going to take?")
                    choices = [f"{GameScreen.major} 411",
                               f"{GameScreen.major} 241",
                               f"{GameScreen.major} 351"]
                    GameScreen.updateChoices(choices)
                    ignore_input = True
                case 8:
                    task_queue += quiz.l300
                    task = task_queue.pop(0)
                    GameScreen.updateDialogue(task['question'])
                    options = [option['option'] for option in task['options']]
                    GameScreen.updateChoices(options)
                case 9:
                    if transcript.gpa >= 3.0:
                        GameScreen.updateDialogue(
                            "HIGH GPA! You can choose to do internship or research"
                        )
                        GameScreen.updateChoices(["research", 'internship', '한국가서 놀기 ㅋㅋ'])
                    else:
                        GameScreen.updateDialogue(
                            "LOW GPA... You didn't get to do anything this summer."
                        )
                        GameScreen.updateChoices([])
                case 10:
                    GameScreen.updateGrade("Senior")
                    GameScreen.updateDialogue("It's Senior year! What course are you going to take?")
                    choices = [f"{GameScreen.major} 415",
                               f"{GameScreen.major} 430",
                               f"{GameScreen.major} 441"]
                    GameScreen.updateChoices(choices)
                    ignore_input = True
                case 11:
                    task_queue += quiz.l400
                    task = task_queue.pop(0)
                    GameScreen.updateDialogue(task['question'])
                    options = [option['option'] for option in task['options']]
                    GameScreen.updateChoices(options)
                case 12:
                    future = "Seriously..? Below 3.0?! You are unemployed :'("
                    if not research_score and not internship_score:
                        future = "You wasted all 3 Summers! You are unemployed :'("
                    elif transcript.gpa >= 3.0:
                        if research_score > internship_score:
                            future = "Good GPA and Good Research portfolio :) Off to Grad School!"
                        else:
                            future = "Good GPA and Good Internship experience :) You got a Fulltime JOB!"

                    GameScreen.updateDialogue(
                        future
                    )
                    GameScreen.updateChoices([])
                    is_playing = False

        GameScreen.makeScreen()
        print(GameScreen.screen)

        if not GameScreen.name:
            userInput = input("Please type your name: ")
            GameScreen.updateName(userInput)

        if not GameScreen.major:
            userInput = input("Please type your major (example CS): ")
            GameScreen.updateMajor(userInput)

        user_input = input("Press q to end game. Choose answer or hit Enter to proceed.\n").strip()
        if not user_input:
            continue
        if user_input == "q":
            break
        elif user_input == '1' or user_input == '2' or user_input == '3':
            if task:
                idx = int(user_input) - 1
                options = task['options']
                max_score = max(options[0]['score'], options[1]['score'], options[2]['score'])
                score = options[idx]['score']
                if doing_research:
                    research_score += score
                    doing_research -= 1
                elif doing_internship:
                    internship_score += score
                    doing_internship -= 1
                else:
                    transcript.add_record(score, max_score)
            else:
                if ignore_input:
                    ignore_input = False
                    continue

                if user_input == '1':
                    if phase == 3:
                        task_queue += quiz.research_1
                    elif phase == 6:
                        task_queue += quiz.research_2
                    elif phase == 9:
                        task_queue += quiz.research_3
                    doing_research = 1

                elif user_input == '2':
                    if phase == 3:
                        task_queue += quiz.internship_1
                    elif phase == 6:
                        task_queue += quiz.internship_2
                    elif phase == 9:
                        task_queue += quiz.internship_3
                    doing_internship = 1
                elif user_input == '3':
                    pass
        else:
            print("Invalid option.")
            exit(1)


if __name__ == '__main__':
    main()
