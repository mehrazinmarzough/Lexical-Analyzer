class Token:
    def __init__(self, lexeme, token):
        self.lexeme = lexeme
        self.token = token

    def display(self):
        print(f'{self.lexeme} -> {self.token}')


def get_ids_or_keywords(m: int):
    index = m
    state = 0
    while 1:
        if state == 0:
            if letter_.__contains__(program[index]):
                state = 1
            else:
                return None, None
        elif state == 1:
            if letter_digit.__contains__(program[index]):
                state = 1
            else:
                state = 2
        elif state == 2:
            index -= 1
            token = program[m:index]
            if KW.__contains__(token):
                return Token(token, f'T_{token.capitalize()}'), index
            else:
                return Token(token, "T_Id"), index
        index += 1


def get_notations(m: int):
    index = m
    state = 0
    while 1:
        if state == 0:
            if program[index] == "{":
                state = 1
            elif program[index] == "}":
                state = 2
            elif program[index] == "(":
                state = 3
            elif program[index] == ")":
                state = 4
            elif program[index] == "[":
                state = 5
            elif program[index] == "]":
                state = 6
            elif program[index] == ",":
                state = 7
            elif program[index] == ";":
                state = 8

        elif state == 1:
            return Token("{", "T_LC"), index
        elif state == 2:
            return Token("}", "T_RC"), index
        elif state == 3:
            return Token("(", "T_LP"), index
        elif state == 4:
            return Token(")", "T_RP"), index
        elif state == 5:
            return Token("[", "T_LB"), index
        elif state == 6:
            return Token("]", "T_RB"), index
        elif state == 7:
            return Token(",", "T_Comma"), index
        elif state == 8:
            return Token(";", "T_Semicolon"), index
        else:
            return None, None
        index += 1


def get_comments(m: int):
    index = m
    state = 0
    while 1:
        if state == 0:
            if program[index] == "/":
                state = 1
            else:
                return None, None
        elif state == 1:
            if program[index] == "/":
                state = 2
            else:
                return None, None
        elif state == 2:
            if program[index] != "\n":
                state = 2
            else:
                state = 3
        elif state == 3:
            token = program[m:index]
            return Token(token, "T_Comment"), index
        else:
            return None, None
        index += 1


def get_numbers(m: int):
    index = m
    state = 0
    while 1:
        if state == 0:
            if digit_but_0.__contains__(program[index]):
                state = 6
            elif program[index] == "0":
                state = 1
            else:
                return None, None
        elif state == 1:
            if program[index] == "x":
                state = 3
            else:
                state = 2
        elif state == 2:
            index -= 1
            token = Token(program[m:index], "T_Decimal")
            return token, index
        elif state == 3:
            if hex_digit.__contains__(program[index]):
                state = 4
            else:
                return None, None
        elif state == 4:
            if hex_digit.__contains__(program[index]):
                state = 4
            else:
                state = 5
        elif state == 5:
            index -= 1
            token = Token(program[m:index], "T_Hexadecimal")
            return token, index
        elif state == 6:
            if digit.__contains__(program[index]):
                state = 6
            else:
                state = 7
        elif state == 7:
            index -= 1
            token = Token(program[m:index], "T_Decimal")
            return token, index
        else:
            return None, None
        index += 1


def get_literals(m: int):
    index = m
    state = 0
    while 1:
        if state == 0:
            if program[index] == "'":
                state = 1
            elif program[index == "\""]:
                state = 5
            else:
                return None, None
        elif state == 1:
            if program[index] == "\\":
                state = 4
            elif program[index].isascii() and program[index] != "'":
                state = 2
            else:
                return None
        elif state == 2:
            if program[index] == "'":
                state = 3
            else:
                return None
        elif state == 3:
            token = Token(program[m:index], "T_Character")
            return token, index
        elif state == 4:
            if program[index] == "'" or program[index] == "\\":
                state = 2
            else:
                return None, None
        elif state == 5:
            if program[index].isascii() and program[index] == "\"" and program[index] == "\\":
                state = 5
            elif program[index] == "\"":
                state = 6
            elif program[index] == "\\":
                state = 7
            else:
                return None, None
        elif state == 6:
            token = Token(program[m:index], "T_String")
            return token, index
        elif state == 7:
            if program[index].isascii() and program[index] != "\\":
                state = 5
            else:
                return None, None
        else:
            return None, None
        index += 1


KW = {"bool", "break", "char", "continue", "else", "false", "for", "if", "int", "print", "return", "true"}
digit = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}
hex_digit = digit.union({"A", "B", "C", "D", "E", "F"})
digit_but_0 = {"1", "2", "3", "4", "5", "6", "7", "8", "9"}
WS = {" ", "\t", "\n"}
letter_ = set()
for i in range(65, 91):
    letter_.add(chr(i))
for i in range(97, 123):
    letter_.add(chr(i))
letter_.add(chr(95))
letter_digit = letter_.union(digit)


lines = []
while True:
    line = input()
    if line == "END":
        break
    lines.append(line)

program = '\n'.join(lines)
