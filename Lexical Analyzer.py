class Token:
    def __init__(self, lexeme, token):
        self.lexeme = lexeme
        self.token = token

    def display(self):
        print(f'({self.lexeme}, {self.token})')


def getNumbers(Input: str):
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


KW = {"bool", "break", "char", "continue", "else", "false", "for", "if", "int", "print", "return", "true"}
digit = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}
hex_digit = digit.union({"A", "B", "C", "D", "E", "F"})


program = input()
token_list = list()

i = 0
j = 1

