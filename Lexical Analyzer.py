class Token:
    def __init__(self, lexeme, token):
        self.lexeme = lexeme
        self.token = token

    def display(self):
        print(f'{self.lexeme} -> {self.token}')


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


lines = []
while True:
    line = input()
    if line == "END":
        break
    lines.append(line)

program = '\n'.join(lines)
