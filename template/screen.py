class Screen:
    def __init__(self, name="", grade="", future="", dialogue="", choices=""):
        super(Screen, self).__init__()
        self.screen = ""
        self.name = name
        self.grade = grade
        self.future = future
        self.dialogue = dialogue
        self.choices = choices

    def updateName(self, name):
        self.name = name
        self.makeScreen()

    def updateGrade(self, grade):
        self.grade = grade
        self.makeScreen()

    def updateFuture(self, future):
        self.future = future
        self.makeScreen()

    def updateDialogue(self, dialogue):
        self.dialogue = dialogue
        self.makeScreen()

    def updateChoices(self, choices):
        self.choices = choices
        self.makeScreen()

    def makeScreen(self) -> str:
        lines = []

        for line_num in range(30):
            lines.append(self.fillLines(line_num))

        self.screen = "".join(lines)

    def fillLines(self, line_num: int) -> str:
        match line_num:
            case 0 | 29:
                return makeBoarderLine()
            case 1:
                if len(self.name) > 0:
                    name_string = f"name: {self.name}"
                    return makeLineAtStart(name_string)
                else:
                    return makeDefaultLine()
            case 2:
                if len(self.grade) > 0:
                    grade_string = f"grade: {self.grade}"
                    return makeLineAtStart(grade_string)
                else:
                    return makeDefaultLine()
            case 3:
                if len(self.future) > 0:
                    future_string = f"future: {self.future}"
                    return makeLineAtStart(future_string)
                else:
                    return makeDefaultLine()
            case 13:
                if len(self.dialogue) > 0:
                    return makeLineAtMiddle(self.dialogue)
                else:
                    return makeDefaultLine()
            case 15:
                if len(self.choices) > 0:
                    choice_string = f"1: {self.choices[0]}"
                    return makeLineAtMiddle(choice_string)
                else:
                    return makeDefaultLine()
            case 16:
                if len(self.choices) > 0:
                    choice_string = f"3: {self.choices[1]}"
                    return makeLineAtMiddle(choice_string)
                else:
                    return makeDefaultLine()
            case 17:
                if len(self.choices) > 0:
                    choice_string = f"3: {self.choices[2]}"
                    return makeLineAtMiddle(choice_string)
                else:
                    return makeDefaultLine()
            case _:
                return makeDefaultLine()


def makeLineAtStart(s):
    len_ = len(s)
    line = ""
    for row in range(80):
        if row == 0 or row == 79:
            line += "|"
        elif row == 1:
            line += s
        elif row <= len_:
            continue
        else:
            line += " "
    line += "\n"
    return line


def makeLineAtMiddle(s):
    len_ = len(s)
    pivot = 40 - len_ // 2 - 1
    line = ""
    for row in range(80):
        if row == 0 or row == 79:
            line += "|"
        elif row == pivot:
            line += s
        elif pivot < row < len_ + pivot:
            continue
        else:
            line += " "
    line += "\n"
    return line


def makeDefaultLine():
    line = ""
    for row in range(80):
        if row == 0 or row == 79:
            line += "|"
        else:
            line += " "
    line += "\n"
    return line


def makeBoarderLine():
    line = ""
    for row in range(80):
        line += "-"
    line += "\n"
    return line


# screen = Screen("Wan", "Sophomore", "Not good", "What class will you take?", [
#                 "what is my name?", "what is your name?", "I am smart!"])
# screen.makeScreen()
# print(screen.screen)
