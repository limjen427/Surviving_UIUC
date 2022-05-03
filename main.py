from template.screen import Screen


def main():
    is_playing = True
    phase = 0
    GameScreen = Screen()
    GameScreen.makeScreen()
    while is_playing:
        print(GameScreen.screen)

        if not GameScreen.name:
            userInput = input("Please type your name: ")
            GameScreen.updateName(userInput)

        if not GameScreen.grade:
            userInput = input("Please type your grade (Example: Sophomore): ")
            GameScreen.updateGrade(userInput)

        endGame = input("Press q to end game.")
        if endGame == "q":
            break


if __name__ == '__main__':
    main()
