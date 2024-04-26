class Token:
    def __init__(self, lexeme, token):
        self.lexeme = lexeme
        self.token = token

    def display(self):
        print(f'{self.lexeme} -> {self.token}')


def get_ids_or_keywords(m: int):
    index = m
    state = 0
    while index != program.__len__()+1:
        if index < program.__len__():
            c = program[index]
        if state == 0:
            if letter_.__contains__(c):
                state = 1
            else:
                return None, None
        elif state == 1:
            if letter_digit.__contains__(c):
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
    return None, None


def get_notations(m: int):
    index = m
    state = 0
    while index != program.__len__()+1:
        if index < program.__len__():
            c = program[index]
        if state == 0:
            if c == "{":
                state = 1
            elif c == "}":
                state = 2
            elif c == "(":
                state = 3
            elif c == ")":
                state = 4
            elif c == "[":
                state = 5
            elif c == "]":
                state = 6
            elif c == ",":
                state = 7
            elif c == ";":
                state = 8
            else:
                return None, None

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
    return None, None


def get_comments(m: int):
    index = m
    state = 0
    while index != program.__len__()+1:
        if index < program.__len__():
            c = program[index]
        if state == 0:
            if c == "/":
                state = 1
            else:
                return None, None
        elif state == 1:
            if c == "/":
                state = 2
            else:
                return None, None
        elif state == 2:
            if c != "\n":
                state = 2
            else:
                state = 3
        elif state == 3:
            index -= 1
            token = program[m:index]
            return Token(token, "T_Comment"), index
        else:
            return None, None
        index += 1
    return None, None


def get_numbers(m: int):
    index = m
    state = 0
    while index != program.__len__()+1:
        if index < program.__len__():
            c = program[index]
        if state == 0:
            if digit_but_0.__contains__(c):
                state = 6
            elif c == "0":
                state = 1
            else:
                return None, None
        elif state == 1:
            if c == "X" or c == "x":
                state = 3
            else:
                state = 2
        elif state == 2:
            index -= 1
            token = Token(program[m:index], "T_Decimal")
            return token, index
        elif state == 3:
            if hex_digit.__contains__(c):
                state = 4
            else:
                return None, None
        elif state == 4:
            if hex_digit.__contains__(c):
                state = 4
            else:
                state = 5
        elif state == 5:
            index -= 1
            token = Token(program[m:index], "T_Hexadecimal")
            return token, index
        elif state == 6:
            if digit.__contains__(c):
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
    return None, None


def get_literals(m: int):
    index = m
    state = 0
    while index != program.__len__()+1:
        if index < program.__len__():
            c = program[index]
        if state == 0:
            if c == "'":
                state = 1
            elif c == "\"":
                state = 5
            else:
                return None, None
        elif state == 1:
            if c == "\\":
                state = 4
            elif c.isascii() and c != "'":
                state = 2
            else:
                return None, None
        elif state == 2:
            if c == "'":
                state = 3
            else:
                return None, None
        elif state == 3:
            token = Token(program[m:index], "T_Character")
            return token, index
        elif state == 4:
            if c == "'" or c == "\\":
                state = 2
            else:
                return None, None
        elif state == 5:
            if c.isascii() and c != "\"" and c != "\\":
                state = 5
            elif c == "\"":
                state = 6
            elif c == "\\":
                state = 7
            else:
                return None, None
        elif state == 6:
            token = Token(program[m:index], "T_String")
            return token, index
        elif state == 7:
            if c.isascii():
                state = 5
            else:
                return None, None
        else:
            return None, None
        index += 1
    return None, None


def get_operators(m: int):
    index = m
    state = 0
    while index != program.__len__()+1:
        if index < program.__len__():
            c = program[index]
        if state == 0:
            if c == "+":
                state = 1
            elif c == "-":
                state = 2
            elif c == "*":
                state = 3
            elif c == "/":
                state = 4
            elif c == "%":
                state = 5
            elif c == ">":
                state = 10
            elif c == "<":
                state = 13
            elif c == "=":
                state = 16
            elif c == "!":
                state = 19
            elif c == "&":
                state = 22
            elif c == "|":
                state = 24
            else:
                return None, None
        elif state == 1:
            if digit.__contains__(c):
                state = 6
            else:
                state = 8
        elif state == 2:
            if digit.__contains__(c):
                state = 6
            else:
                state = 9
        elif state == 3:
            token = Token(program[m:index], "T_AOp_ML")
            return token, index
        elif state == 4:
            token = Token(program[m:index], "T_AOp_DV")
            return token, index
        elif state == 5:
            token = Token(program[m:index], "T_AOp_RM")
            return token, index
        elif state == 6:
            if digit.__contains__(c):
                state = 6
            else:
                state = 7
        elif state == 7:
            index -= 1
            token = Token(program[m:index], "T_Decimal")
            return token, index
        elif state == 8:
            index -= 1
            token = Token(program[m:index], "T_AOp_PL")
            return token, index
        elif state == 9:
            index -= 1
            token = Token(program[m:index], "T_AOp_MN")
            return token, index
        elif state == 10:
            if c == "=":
                state = 11
            else:
                state = 12
        elif state == 11:
            token = Token(program[m:index], "T_ROp_GE")
            return token, index
        elif state == 12:
            index -= 1
            token = Token(program[m:index], "T_ROp_G")
            return token, index
        elif state == 13:
            if c == "=":
                state = 14
            else:
                state = 15
        elif state == 14:
            token = Token(program[m:index], "T_ROp_LE")
            return token, index
        elif state == 15:
            index -= 1
            token = Token(program[m:index], "T_ROp_L")
            return token, index
        elif state == 16:
            if c == "=":
                state = 17
            else:
                state = 18
        elif state == 17:
            token = Token(program[m:index], "T_ROp_E")
            return token, index
        elif state == 18:
            index -= 1
            token = Token(program[m:index], "T_Assign")
            return token, index
        elif state == 19:
            if c == "=":
                state = 20
            else:
                state = 21
        elif state == 20:
            token = Token(program[m:index], "T_ROp_NE")
            return token, index
        elif state == 21:
            index -= 1
            token = Token(program[m:index], "T_LOp_NOT")
            return token, index
        elif state == 22:
            if c == "&":
                state = 23
            else:
                return None, None
        elif state == 23:
            token = Token(program[m:index], "T_LOp_AND")
            return token, index
        elif state == 24:
            if c == "|":
                state = 25
            else:
                return None, None
        elif state == 25:
            token = Token(program[m:index], "T_LOp_OR")
            return token, index
        else:
            return None, None
        index += 1
    return None, None


def get_whitespace(m: int):
    index = m
    state = 0
    while index != program.__len__()+1:
        if index < program.__len__():
            c = program[index]
        if state == 0:
            if WS.__contains__(c):
                state = 1
            else:
                return None, None
        elif state == 1:
            if WS.__contains__(c):
                state = 1
            else:
                state = 2
        elif state == 2:
            index -= 1
            token = Token("whitespace", "T_Whitespace")
            return token, index
        else:
            return None, None
        index += 1
    return None, None


KW = {"bool", "break", "char", "continue", "else", "false", "for", "if", "int", "print", "return", "true"}
digit = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}
hex_digit = digit.union({"A", "B", "C", "D", "E", "F", "a", "b", "c", "d", "e", "f"})
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

i = 0
while i != program.__len__():
    A, a = get_ids_or_keywords(i)
    B, b = get_notations(i)
    C, c = get_comments(i)
    D, d = get_numbers(i)
    E, e = get_literals(i)
    F, f = get_operators(i)
    G, g = get_whitespace(i)

    if A is not None:
        print(f'{i}: ', end="")
        i = a
        A.display()
    elif B is not None:
        print(f'{i}: ', end="")
        i = b
        B.display()
    elif C is not None:
        print(f'{i}: ', end="")
        i = c
        C.display()
    elif D is not None:
        print(f'{i}: ', end="")
        i = d
        D.display()
    elif E is not None:
        print(f'{i}: ', end="")
        i = e
        E.display()
    elif F is not None:
        print(f'{i}: ', end="")
        i = f
        F.display()
    elif G is not None:
        print(f'{i}: ', end="")
        i = g
        G.display()
    else:
        i += 1
