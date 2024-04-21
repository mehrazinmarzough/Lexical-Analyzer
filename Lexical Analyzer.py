class Token:
    def __init__(self, lexeme, token):
        self.lexeme = lexeme
        self.token = token

    def display(self):
        print(f'({self.lexeme}, {self.token})')


def get_keywords(Input: str):
    index = 0
    state = 0
    while index != Input.__len__():
        if state == 0:
            state = 1
        elif state == 1:
            if KW.__contains__(Input):
                return Token(Input, f'T_{Input.capitalize()}')
        else:
            return None
        index += 1


def get_ids(Input: str):
    index = 0
    state = 0
    while index != Input.__len__():
        if state == 0:
            if letter_.__contains__(Input[index]):
                state = 1
            else:
                return None
        elif state == 1:
            if index == Input.__len__() - 1:
                return Token(Input, "T_Id")
            elif letter_digit.__contains__(Input[index]):
                state = 1
            else:
                return None
        else:
            return None
        index += 1


def get_notations(Input: str):
    index = 0
    state = 0
    while index != Input.__len__():
        if state == 0:
            if notations.__contains__(Input[index]):
                state = 1
        elif state == 1:
            c = Input[index]
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
            return Token(Input, f'T_{t}')
        else:
            return None
        index += 1


def get_numbers(Input: str):
    index = 0
    state = 0
    while index != Input.__len__():
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
            if index == Input.__len__() - 1:
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
            if index == Input.__len__() - 1:
                return Token(Input, "T_Hexadecimal")
            elif hex_digit.__contains__(Input[index]):
                state = 4
            else:
                return None
        index += 1


def get_whitespace(Input: str):
    if Input == " ":
        return Token("whitespace (space character)", "T_Whitespace")
    elif Input == "\t":
        return Token("whitespace (tab)", "T_Whitespace")
    elif Input == "\n":
        return Token("whitespace (newline)", "T_Whitespace")
    else:
        return None


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


program = input()
token_list = list()

i = 0
j = 1

while 1:
    if WS.__contains__(program[j]):
        get_whitespace(program[j])
    elif notations.__contains__(program[j]):
        get_notations(program[j])

    j -= 1
    ret_token = program[i:j]
    get_keywords(ret_token)
    get_ids(ret_token)
    i = j + 2
    j = i + 1
