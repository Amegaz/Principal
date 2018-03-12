class Lexico:
    def __init__(self):
        item = 0

    def valMinus(self,letter):
        if letter == 'i':
            return 4.11
        if letter == 'w':
            return 20.11
        if letter == 'r':
            return 21.11
        if letter == 'e':
            return 22.11
        if letter == 'f':
            return 4.21
        if letter == 'v':
            return 4.31
        elif letter.isalpha() or letter == '_':
            return 0
        elif letter.isdigit():
            return 1
        #elif letter == '.':
        #    return 2
        elif letter == '"':
            return 3.5
        elif letter == '+' or letter == '-':
            return 5
        elif letter == '*' or letter == '/':
            return 6
        elif letter == '<' or letter == '>':
            return 7
        elif letter == '|':
            return 8.5
        elif letter == '&':
            return 9.5
        elif letter == '!':
            return 10
        elif letter == '=':
            return 18
        elif letter == ';':
            return 12
        elif letter == ',':
            return 13
        elif letter == '(':
            return 14
        elif letter == ')':
            return 15
        elif letter == '{':
            return 16
        elif letter == '}':
            return 17
        elif letter == '$':
            return 23
        else:
            return -10

    def valLexico(self,letter, state):
        if state == -1:
            return self.valMinus(letter)
        elif state == 0 or state == 19 or state == 20 or state == 21 or state == 22 or state == 4:
            return self.valZero(letter,state)
        elif state == 1:
            return self.valOne(letter,state)
        elif state == 2 or state == 2.5:
            return self.valTwo(letter,state)
        elif state == 3.5:
            return self.valThree(letter,state)
        elif state == 7:
            return self.val(letter,state,'=',7)
        elif state == 8.5:
            return self.val(letter,state,'|',8)
        elif state == 9.5:
            return self.val(letter,state,'&',9)
        elif state == 18 or state == 10:
            return self.val(letter,state,'=',11)
        elif state == 4.11:
            return self.valI(letter)
        elif state == 20.11:
            return self.val(letter,state,'h',20.12)
        elif state == 20.12:
            return self.val(letter,state,'i',20.13)
        elif state == 20.13:
            return self.val(letter,state,'l',20.14)
        elif state == 20.14:
            return self.val(letter,state,'e',20.15)
        elif state == 21.11:
            return self.val(letter,state,'e',21.12)
        elif state == 21.12:
            return self.val(letter,state,'t',21.13)
        elif state == 21.13:
            return self.val(letter,state,'u',21.14)
        elif state == 21.14:
            return self.val(letter,state,'r',21.15)
        elif state == 21.15:
            return self.val(letter,state,'n',21)
        elif state == 22.11:
            return self.val(letter,state,'l',22.12)
        elif state == 22.12:
            return self.val(letter,state,'s',22.13)
        elif state == 22.13:
            return self.val(letter,state,'e',22)
        elif state == 4.12:
            return self.val(letter,state,'t',4)
        elif state == 4.21:
            return self.val(letter,state,'l',4.22)
        elif state == 4.22:
            return self.val(letter,state,'o',4.23)
        elif state == 4.23:
            return self.val(letter,state,'a',4.24)
        elif state == 4.24:
            return self.val(letter,state,'t',4)
        elif state == 4.31:
            return self.val(letter,state,'o',4.32)
        elif state == 4.32:
            return self.val(letter,state,'i',4.33)
        elif state == 4.33:
            return self.val(letter,state,'d',4)
        else:
            return self.changeOperator(letter,state)

    def changeOperator(self,letter,state):
        print('\t' + tipo.printType(state))
        sen += str(asig(state))
        return self.valMinus(letter)

    def val(self,letter,state,compare,ret):
        if letter == compare:
            return ret
        else:
            return self.changeOperator(letter,state)

    def valI(self,letter):
        if letter == 'f':
            return 19
        elif letter == 'n':
            return 4.12
        else:
            return self.valZero(letter)

    def valZero(self,letter,state):
        if letter.isalpha() or letter.isdigit():
            return 0
        else:
            return self.changeOperator(letter,state)

    def valOne(self,letter,state):
        if letter.isdigit():
            return 1
        elif letter == '.':
            return 2.5
        else:
            return self.changeOperator(letter,state)

    def valTwo(self,letter,state):
        if letter.isdigit():
            return 2
        else:
            return self.changeOperator(letter,state)

    def valThree(self,letter,state):
        if letter == '"':
            return 3
        else:
            return 3.5
