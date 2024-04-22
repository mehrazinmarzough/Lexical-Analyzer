class Token:
    def __init__(self, lexeme, token):
        self.lexeme = lexeme
        self.token = token

    def display(self):
        print(f'({self.lexeme}, {self.token})')


def get_keywords(Input: str):
    index = -1
    state = 0
    while index != Input.__len__():
        index += 1
        if state == 0:
            if KW.__contains__(Input):
                state = 1
            else:
                return None
        elif state == 1:
            return Token(Input, f'T_{Input.capitalize()}')
        else:
            return None


def get_ids(Input: str):
    index = -1
    state = 0
    while index != Input.__len__():
        index += 1
        if state == 0:
            if letter_.__contains__(Input[index]):
                state = 1
            else:
                return None
        elif state == 1:
            if index == Input.__len__():
                return Token(Input, "T_Id")
            elif letter_digit.__contains__(Input[index]):
                state = 1
            else:
                return None
        else:
            return None


def get_notations(Input: str):
    index = -1
    state = 0
    while index != Input.__len__():
        index += 1
        if state == 0:
            if notations.__contains__(Input[index]):
                state = 1
        elif state == 1:
            c = Input[index-1]
            if c == "(":
                t = "LP"
            elif c == ")":
                t = "RP"
            elif c == "{":
                t = "LC"
            elif c == "}":
                t = "RC"
            elif c == "[":
                t = "LB"
            elif c == "]":
                t = "RB"
            elif c == ";":
                t = "Semicolon"
            elif c == ",":
                t = "Comma"
            else:
                return None
            if index == Input.__len__():
                return Token(Input, f'T_{t}')
            else:
                return None
        else:
            return None


def get_comment(Input: str):
    index = -1
    state = 0
    while index != Input.__len__():
        index += 1
        if state == 0:
            if Input[index] == "/":
                state = 1
            else:
                return None
        elif state == 1:
            if Input[index] == "/":
                state = 2
            else:
                return None
        elif state == 2:
            if Input[index] != "\n":
                state = 2
            else:
                state = 3
        elif state == 3:
            if index == Input.__len__():
                return Token(Input, "T_Comment")
            else:
                return None


def get_numbers(Input: str):
    index = -1
    state = 0
    while index != Input.__len__():
        index += 1
        if state == 0:
            if Input[index] == "-":
                state = 0
            elif Input[index] == "0":
                state = 2
            elif digit.__contains__(Input[index]):
                state = 1
            else:
                return None
        elif state == 1:
            if index == Input.__len__():
                return Token(Input, "T_Decimal")
            elif digit.__contains__(Input[index]):
                state = 1
            else:
                return None
        elif state == 2:
            if Input[index] == "x":
                state = 3
            else:
                return None
        elif state == 3:
            if hex_digit.__contains__(Input[index]):
                state = 4
            else:
                return None
        elif state == 4:
            if index == Input.__len__():
                return Token(Input, "T_Hexadecimal")
            elif hex_digit.__contains__(Input[index]):
                state = 4
            else:
                return None


def get_operators(Input: str):
    index = -1
    state = 0
    while index != Input.__len__():
        index += 1
        if state == 0:
            c = Input[index]
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
                state = 6
            elif c == "<":
                state = 7
            elif c == "!":
                state = 10
            elif c == "=":
                state = 12
            elif c == "&":
                state = 14
            elif c == "|":
                state = 16
            else:
                return None
        elif state == 1:
            if index == Input.__len__():
                return Token(Input, "AOp_PL")
            else:
                return None
        elif state == 2:
            if index == Input.__len__():
                return Token(Input, "AOp_MN")
            else:
                return None
        elif state == 3:
            if index == Input.__len__():
                return Token(Input, "AOp_ML")
            else:
                return None
        elif state == 4:
            if index == Input.__len__():
                return Token(Input, "AOp_DV")
            else:
                return None
        elif state == 5:
            if index == Input.__len__():
                return Token(Input, "AOp_RM")
            else:
                return None
        elif state == 6:
            if index == Input.__len__():
                return Token(Input, "AOp_G")
            elif program[index] == "=":
                state = 8
            else:
                return None
        elif state == 7:
            if index == Input.__len__():
                return Token(Input, "AOp_L")
            else:
                return None
        elif state == 8:
            if index == Input.__len__():
                return Token(Input, "AOp_GE")
            else:
                return None
        elif state == 9:
            if index == Input.__len__():
                return Token(Input, "AOp_LE")
            else:
                return None
        elif state == 10:
            if index == Input.__len__():
                return Token(Input, "AOp_NOT")
            else:
                return None
        elif state == 11:
            if index == Input.__len__():
                return Token(Input, "AOp_NE")
            else:
                return None
        elif state == 12:
            if index == Input.__len__():
                return Token(Input, "AOp_Assign")
            elif Input[index] == "/":
                state = 13
            else:
                return None
        elif state == 13:
            if index == Input.__len__():
                return Token(Input, "AOp_E")
            else:
                return None
        elif state == 14:
            if Input[index] == "&":
                state = 15
            else:
                return None
        elif state == 15:
            if index == Input.__len__():
                return Token(Input, "AOp_AND")
            else:
                return None
        elif state == 16:
            if Input[index] == "|":
                state = 17
            else:
                return None
        elif state == 17:
            if index == Input.__len__():
                return Token(Input, "AOp_OR")
            else:
                return None
        else:
            return None


def get_whitespace(Input: str):
    if Input == " ":
        return Token("whitespace (space character)", "T_Whitespace")
    elif Input == "\t":
        return Token("whitespace (tab)", "T_Whitespace")
    elif Input == "\n":
        return Token("whitespace (newline)", "T_Whitespace")
    else:
        return None


def perform(i,j):
    ret_token = program[i:j]
    print(ret_token)
    a = get_keywords(ret_token)
    b = get_ids(ret_token)
    c = get_comment(ret_token)
    d = get_numbers(ret_token)
    e = get_operators(ret_token)
    if a is not None:
        a.display()
    elif b is not None:
        b.display()
    elif c is not None:
        c.display()
    elif d is not None:
        d.display()
    elif e is not None:
        e.display()


KW = {"bool", "break", "char", "continue", "else", "false", "for", "if", "int", "print", "return", "true"}
digit = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}
hex_digit = digit.union({"A", "B", "C", "D", "E", "F"})
WS = {" ", "\t", "\n"}
letter_ = set()
for i in range(65, 91):
    letter_.add(chr(i))
for i in range(97, 123):
    letter_.add(chr(i))
letter_.add(chr(95))
letter_digit = letter_.union(digit)
notations = {"{", "}", "(", ")", "[", "]", ",", ";"}
operators = {"+", "-", "*", "/", "%", ">", "<", "=", "!", "&", "|"}
arithmetic_operators = {"+", "-", "*", "/", "%"}
delimiter = WS.union(notations).union(operators)


program = input()
token_list = list()

i = 0
j = 0

while 1:
    k = j
    can_perform = False
    while delimiter.__contains__(program[k]):
        can_perform = True
        if WS.__contains__(program[k]):
            get_whitespace(program[k]).display()
        elif notations.__contains__(program[k]):
            get_notations(program[k]).display()

        k += 1

    while operators.__contains__(program[k]):
        can_perform = True
        k += 1

    if j != 0 and can_perform:
        perform(i, j)
        i = k
        j = i + 1
    else:
        j += 1


