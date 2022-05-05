from template.screen import Screen


def main():
    is_playing = True
    phase = 0
    GameScreen = Screen()
    GameScreen.makeScreen()
    while is_playing:
        print(GameScreen.screen)
        match phase:
            case 0:
                if not GameScreen.name:
                    userInput = input("Please type your name: ")
                    GameScreen.updateName(userInput)

                GameScreen.updateGrade("Freshman")

                phase += 1
                continue
            case 1:
                pass
            case 2:
                pass
            case 3:
                pass

        endGame = input("Press q to end game.")
        if endGame == "q":
            break


if __name__ == '__main__':
    main()
