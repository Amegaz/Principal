import Stack
global sen
file = open("sentences.txt")
otro = file.read()
sentences = otro.split('\n')

def valLexico(letter, state):
    if state == -1:
        return valMinus(letter)
    elif state == 0 or state == 19 or state == 20 or state == 21 or state == 22 or state == 4:
        return valZero(letter,state)
    elif state == 1:
        return valOne(letter,state)
    elif state == 2 or state == 2.5:
        return valTwo(letter,state)
    elif state == 3.5:
        return valThree(letter,state)
    elif state == 7:
        return val(letter,state,'=',7)
    elif state == 8.5:
        return val(letter,state,'|',8)
    elif state == 9.5:
        return val(letter,state,'&',9)
    elif state == 18 or state == 10:
        return val(letter,state,'=',11)
    elif state == 4.11:
        return valI(letter)
    elif state == 20.11:
        return val(letter,state,'h',20.12)
    elif state == 20.12:
        return val(letter,state,'i',20.13)
    elif state == 20.13:
        return val(letter,state,'l',20.14)
    elif state == 20.14:
        return val(letter,state,'e',20.15)
    elif state == 21.11:
        return val(letter,state,'e',21.12)
    elif state == 21.12:
        return val(letter,state,'t',21.13)
    elif state == 21.13:
        return val(letter,state,'u',21.14)
    elif state == 21.14:
        return val(letter,state,'r',21.15)
    elif state == 21.15:
        return val(letter,state,'n',21)
    elif state == 22.11:
        return val(letter,state,'l',22.12)
    elif state == 22.12:
        return val(letter,state,'s',22.13)
    elif state == 22.13:
        return val(letter,state,'e',22)
    elif state == 4.12:
        return val(letter,state,'t',4)
    elif state == 4.21:
        return val(letter,state,'l',4.22)
    elif state == 4.22:
        return val(letter,state,'o',4.23)
    elif state == 4.23:
        return val(letter,state,'a',4.24)
    elif state == 4.24:
        return val(letter,state,'t',4)
    elif state == 4.31:
        return val(letter,state,'o',4.32)
    elif state == 4.32:
        return val(letter,state,'i',4.33)
    elif state == 4.33:
        return val(letter,state,'d',4)
    else:
        return changeOperator(letter,state)

def changeOperator(letter,state):
    print('\t' + printType(state))
    sen += str(asig(state))
    return valMinus(letter)

def val(letter,state,compare,ret):
    if letter == compare:
        return ret
    else:
        return changeOperator(letter,state)

def valI(letter):
    if letter == 'f':
        return 19
    elif letter == 'n':
        return 4.12
    else:
        return valZero(letter)

def valZero(letter,state):
    if letter.isalpha() or letter.isdigit():
        return 0
    else:
        return changeOperator(letter,state)

def valOne(letter,state):
    if letter.isdigit():
        return 1
    elif letter == '.':
        return 2.5
    else:
        return changeOperator(letter,state)

def valTwo(letter,state):
    if letter.isdigit():
        return 2
    else:
        return changeOperator(letter,state)

def valThree(letter,state):
    if letter == '"':
        return 3
    else:
        return 3.5
    
def valMinus(letter):
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

def printType(x):
    if x == 0 or (x<5 and x>4) or (x<21 and x>20) or (x<22 and x>21) or (x<23 and x>22):
        return 'Identificador'
    elif x == 1:
        return 'Entero'
    elif x == 2:
        return 'Real'
    elif x == 3:
        return 'Cadena'
    elif x == 4:
        return 'Tipo'
    elif x == 5:
        return 'OpSuma'
    elif x == 6:
        return 'OpMul'
    elif x == 7:
        return 'OpRelac'
    elif x == 8:
        return 'OpOr'
    elif x == 9:
        return 'OpAnd'
    elif x == 10:
        return 'OpNot'
    elif x == 11:
        return 'OpIgualdad'
    elif x == 12:
        return ';'
    elif x == 13:
        return ','
    elif x == 14:
        return '('
    elif x == 15:
        return ')'
    elif x == 16:
        return '{'
    elif x == 17:
        return '}'
    elif x == 18:
        return '='
    elif x == 19:
        return 'if'
    elif x == 20:
        return 'while'
    elif x == 21:
        return 'return'
    elif x == 22:
        return 'else'
    elif x == 23:
        return '$'
    else:
        return 'Invalido'

def asig(x):
    if x < 3:
        return 0
    elif x == 5:
        return 1
    elif x == 23:
        return 2
    else:
        return 3
def re(leer):
    print("Entrada: ",leer)
    estado = s[stack.top()][int(leer)]
    print("Salida: ",estado)
    if estado == 2:
        stack.push(int(leer))
        stack.push(2)
    elif estado == 3:
        stack.push(int(leer))
        stack.push(3)
    elif estado == 4:
        stack.push(int(leer))
        stack.push(4)
    elif estado == -3:
        stack.pop()
        stack.pop()
        stack.push(3)
        stack.push(1)
    elif estado == -2:
        print("E->ind+ind")
        for x in range(0,6):
            print("Se desapilo: ",stack.pop())
        estado = s[stack.top()][3]
        stack.push(3)
        stack.push(estado)
    elif estado == -1:
        print("Aceptado")
    else:
        print("Error al validar")

s = [[0,0,0,0,0] for i in range(5)]
s[0][0] = 2
s[0][1] = 0
s[0][2] = 0
s[0][3] = 1

s[1][0] = 0
s[1][1] = 0
s[1][2] = -1
s[1][3] = 0

s[2][0] = 0
s[2][1] = 3
s[2][2] = 0
s[2][3] = 0

s[3][0] = 4
s[3][1] = 0
s[3][2] = 0
s[3][3] = 0

s[4][0] = 0
s[4][1] = 0
s[4][2] = -2
s[4][3] = 0

t = [[0,0,0,0,0] for i in range(5)]
t[0][0] = 2
t[0][1] = 0
t[0][2] = 0
t[0][3] = 1

t[1][0] = 0
t[1][1] = 0
t[1][2] = -1
t[1][3] = 0

t[2][0] = 0
t[2][1] = 3
t[2][2] = -3
t[2][3] = 0

t[3][0] = 2
t[3][1] = 0
t[3][2] = 0
t[3][3] = 4

t[4][0] = 0
t[4][1] = 0
t[4][2] = -2
t[4][3] = 0

for sentence in sentences:
    flag = False
    typeSentence = 'Valido'
    if '"' in sentence:
        srr = ''
        for n in sentence:
            if n == '"' and flag:
                flag = False
            if n == '"':
                flag = True
            if n == ' ' and flag:
                n = '\n'
            srr += n
        sentence = srr
    words = sentence.split(' ')
    sen = ''
    for word in words:
        if '\n' in word:
            word = word.replace("\n"," ")
            sentence = ''
        i = 0
        typeDate = -1
        while i < len(word):
            typeDate = valLexico(word[i], typeDate)
            print(word[i],end='')
            i+=1
        print("\t" + printType(typeDate))
        sen += str(asig(typeDate))
    sen += '2'
    print(sen)
    stack = Stack.Stack()
    stack.push(2)
    stack.push(0)
    for leer in sen:
        re(leer)
    re(leer)
file.close()
