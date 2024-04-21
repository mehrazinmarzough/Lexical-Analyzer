class Token:
    def __init__(self, lexeme, token):
        self.lexeme = lexeme
        self.token = token

    def display(self):
        print(f'({self.lexeme}, {self.token})')


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
WS = {" ","\t","\n"}


program = input()
token_list = list()

i = 0
j = 1

while 1:
    if WS.__contains__(program[j]):
        get_whitespace(program[j])
        j -= 1
        #program[i:j]

        i = j + 2
        j = i + 1



