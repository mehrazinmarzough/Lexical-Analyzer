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
                return None
        elif state == 1:
            if letter_digit.__contains__(program[index]):
                state = 1
            else:
                state = 2
        elif state == 2:
            index -= 1
            token = program[m:index]
            index += 1
            if KW.__contains__(token):
                return Token(token, f'T_{token.capitalize()}'), index
            else:
                return Token(token, "T_Id"), index


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

lines = []
while True:
    line = input()
    if line == "END":
        break
    lines.append(line)

program = '\n'.join(lines)
