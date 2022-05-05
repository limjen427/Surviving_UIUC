from template.screen import Screen
from quiz import Quiz
from transcript import Transcript


def main():
    is_playing = True
    phase = 0
    GameScreen = Screen()
    GameScreen.makeScreen()

    quiz = Quiz()
    transcript = Transcript()
    research_score = 0
    internship_score = 0

    doing_research = 0
    doing_internship = 0

    task_queue = []
    while is_playing:
        GameScreen.updateGrade(transcript.gpa)
        task = None
        if task_queue:
            task = task_queue.pop(0)

            GameScreen.updateDialogue(task['question'])
            options = [option['option'] for option in task['options']]
            GameScreen.updateChoices(options)
        else:
            phase += 1
            if phase == 1:  # 100 200 lv problems
                task_queue += quiz.l100
                task_queue += quiz.l200
            elif phase == 2:
                if float(transcript.gpa) >= 3.0:
                    GameScreen.updateDialogue("High GPA. You can choose to do internship or research")
                    GameScreen.updateChoices(["research", 'internship', ' '])
                else:
                    GameScreen.updateDialogue("Low GPA. You didn't get to do anything this summer.")
                    GameScreen.updateChoices([])
            elif phase == 3:
                task_queue += quiz.l300
                task_queue += quiz.l400
                task = task_queue.pop(0)

                GameScreen.updateDialogue(task['question'])
                options = [option['option'] for option in task['options']]
                GameScreen.updateChoices(options)
            elif phase == 4:
                if float(transcript.gpa) >= 3.0:
                    GameScreen.updateDialogue("High GPA. You can choose to do internship or research")
                    GameScreen.updateChoices(["research", 'internship', '한국가서 놀기 ㅋㅋ'])
                else:
                    GameScreen.updateDialogue("Low GPA. You didn't get to do anything this summer.")
                    GameScreen.updateChoices([])
                pass
            elif phase == 5:
                GameScreen.updateDialogue(
                    f"GPA: {transcript.gpa}, internship score: {internship_score}, research score: {research_score}")

                future = "Unemployed :'("
                if float(transcript.gpa) >= 3.0:
                    if research_score > internship_score:
                        future = "Grad School!"
                    else:
                        future = "Full Time Job!"
                GameScreen.updateFuture(future)
                GameScreen.updateChoices([])

        print(GameScreen.screen)

        if not GameScreen.name:
            userInput = input("Please type your name: ")
            GameScreen.updateName(userInput)

        # grade 는 학년 대신 GPA로 교체!
        # if not GameScreen.grade:
        #     userInput = input("Please type your grade (Example: Sophomore): ")
        #     GameScreen.updateGrade(userInput)

        user_input = input("Press q to end game. Choose option to hit Enter proceed.\n").strip()
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
                if user_input == '1':
                    if phase == 2:
                        task_queue += quiz.research_1
                    else:
                        task_queue += quiz.research_2
                    doing_research = 1
                elif user_input == '2':
                    if phase == 2:
                        task_queue += quiz.internship_1
                    else:
                        task_queue += quiz.internship_2
                    doing_internship = 1
                elif user_input == '3':
                    pass
        else:
            print("Invalid option.")
            exit(1)


if __name__ == '__main__':
    main()
