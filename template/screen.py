LINEWIDTH = 80
LINEHEIGHT = 25


class Screen:
    def __init__(self, dialogue="Welcome to Surviving UIUC!"):
        super(Screen, self).__init__()
        self.screen = ""
        self.dialogue = dialogue
        self.name = None
        self.grade = None
        self.gpa = None
        self.major = None
        self.choices = None

    def updateName(self, name):
        self.name = name

    def updateGrade(self, grade):
        self.grade = grade

    def updategpa(self, gpa):
        self.gpa = gpa

    def updateMajor(self, major):
        self.major = major

    def updateDialogue(self, dialogue):
        self.dialogue = dialogue

    def updateChoices(self, choices):
        self.choices = choices

    def makeScreen(self) -> str:
        lines = []

        for line_num in range(LINEHEIGHT):
            lines.append(self.fillLines(line_num))

        self.screen = "".join(lines)

    def fillLines(self, line_num: int) -> str:
        match line_num:
            case 0 | 24:
                return makeBoarderLine()
            case 1:
                if self.name:
                    name_string = f"name: {self.name}"
                    return makeLineAtStart(name_string)
                else:
                    return makeDefaultLine()
            case 2:
                if self.grade:
                    grade_string = f"grade: {self.grade}"
                    return makeLineAtStart(grade_string)
                else:
                    return makeDefaultLine()
            case 3:
                if self.gpa:
                    gpa_string = f"gpa: {self.gpa}"
                    return makeLineAtStart(gpa_string)
                else:
                    return makeDefaultLine()

            case 4:
                if self.major:
                    self.major = self.major.upper()
                    major_string = f"major: {self.major}"
                    return makeLineAtStart(major_string)
                else:
                    return makeDefaultLine()

            case 13:
                if len(self.dialogue) > 0:
                    return makeLineAtMiddle(self.dialogue)
                else:
                    return makeDefaultLine()
            case 15:
                if self.choices:
                    choice_string = f"1: {self.choices[0]}"
                    return makeLineAtMiddle(choice_string)
                else:
                    return makeDefaultLine()
            case 16:
                if self.choices:
                    choice_string = f"2: {self.choices[1]}"
                    return makeLineAtMiddle(choice_string)
                else:
                    return makeDefaultLine()
            case 17:
                if self.choices:
                    choice_string = f"3: {self.choices[2]}"
                    return makeLineAtMiddle(choice_string)
                else:
                    return makeDefaultLine()
            case _:
                return makeDefaultLine()


def makeLineAtStart(s):
    len_ = len(s)
    line = ""
    for row in range(LINEWIDTH):
        if row == 0 or row == LINEWIDTH-1:
            line += ""
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
    pivot = (LINEWIDTH//2) - len_ // 2 - 1
    line = ""
    for row in range(LINEWIDTH):
        if row == 0 or row == LINEWIDTH-1:
            line += ""
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
    for row in range(LINEWIDTH):
        if row == 0 or row == LINEWIDTH-1:
            line += ""
        else:
            line += " "
    line += "\n"
    return line


def makeBoarderLine():
    line = ""
    for _ in range(LINEWIDTH):
        line += "-"
    line += "\n"
    return line