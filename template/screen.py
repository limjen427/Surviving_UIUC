class Screen:
    def __init__(self, name, grade, future, dialogue):
        super(Screen, self).__init__()
        self.screen = ""
        self.name = name
        self.grade = grade
        self.future = future
        self.dialogue = dialogue

    def makeScreen(self) -> str:
        lines = []

        for line_num in range(30):
            lines.append(self.fillLines(line_num))

        self.screen = "".join(lines)

    def fillLines(self, line_num: int) -> str:
        match line_num:
            case 0 | 29:
                line = ""
                for row in range(80):
                    line += "-"
                line += "\n"
                return line
            case 1:
                name_string = f"name: {self.name}"
                name_len = len(name_string)
                line = ""
                for row in range(80):
                    if row == 0 or row == 79:
                        line += "|"
                    elif row == 1:
                        line += name_string
                    elif row <= name_len:
                        continue
                    else:
                        line += " "
                line += "\n"
                return line
            case 2:
                grade_string = f"grade: {self.grade}"
                grade_len = len(grade_string)
                line = ""
                for row in range(80):
                    if row == 0 or row == 79:
                        line += "|"
                    elif row == 1:
                        line += grade_string
                    elif row <= grade_len:
                        continue
                    else:
                        line += " "
                line += "\n"
                return line
            case 3:
                future_string = f"future: {self.future}"
                future_len = len(future_string)
                line = ""
                for row in range(80):
                    if row == 0 or row == 79:
                        line += "|"
                    elif row == 1:
                        line += future_string
                    elif row <= future_len:
                        continue
                    else:
                        line += " "
                line += "\n"
                return line
            case _:
                line = ""
                for row in range(80):
                    if row == 0 or row == 79:
                        line += "|"
                    else:
                        line += " "
                line += "\n"
                return line


screen = Screen("Wan", "Sophomore", "Not good", "True")
screen.makeScreen()
print(screen.screen)
