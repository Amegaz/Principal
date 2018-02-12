file = open("sentences.txt")
otro = file.read()
sentences = otro.split('\n')

def valLexico(letter, state):
    if state == 'Inicial':
        return valMinus(letter)
    elif state == 'Identificador' or state == 'if' or state == 'while' or state == 'return' or state == 'else' or state == 'tipo':
        return valZero(letter)
    elif state == 'Entero':
        return valOne(letter)
    elif state == 'Real':
        return valTwo(letter)
    elif state == 'CadenaIncompleta':
        return valThree(letter)
    elif state == 'OpRelac':
        return valSeven(letter)
    elif state == 'OpOrIncompleto':
        return valEight(letter)
    elif state == 'OpAndIncompleto':
        return valNine(letter)
    elif state == '=' or state == 'OpNot':
        return valEleven(letter)
    elif state == '-i':
        return valI(letter)
    elif state == '-w':
        return valW(letter)
    elif state == '-wh':
        return valWh(letter)
    elif state == '-whi':
        return valWhi(letter)
    elif state == '-whil':
        return valWhil(letter)
    elif state == '-r':
        return valR(letter)
    elif state == '-re':
        return valRe(letter)
    elif state == '-ret':
        return valRet(letter)
    elif state == '-retu':
        return valRetu(letter)
    elif state == '-retur':
        return valRetur(letter)
    elif state == '-e':
        return valE(letter)
    elif state == '-el':
        return valEl(letter)
    elif state == '-els':
        return valEls(letter)
    elif state == '-in':
        return valIn(letter)
    elif state == '-f':
        return valF(letter)
    elif state == '-fl':
        return valFl(letter)
    elif state == '-flo':
        return valFlo(letter)
    elif state == '-floa':
        return valFloa(letter)
    elif state == '-v':
        return valV(letter)
    elif state == '-vo':
        return valVo(letter)
    elif state == '-voi':
        return valVoi(letter)
    else:
        return 'Invalido'

def valI(letter):
    if letter == 'f':
        return '-if'
    elif letter == 'n':
        return '-in'
    else:
        return valZero(letter)

def valIn(letter):
    if letter == 't':
        return 'tipo'
    else:
        return valZero(letter)

def valF(letter):
    if letter == 'l':
        return '-fl'
    else:
        return valZero(letter)

def valFl(letter):
    if letter == 'o':
        return '-flo'
    else:
        return valZero(letter)

def valFlo(letter):
    if letter == 'a':
        return '-floa'
    else:
        return valZero(letter)

def valFloa(letter):
    if letter == 't':
        return 'tipo'
    else:
        return valZero(letter)

def valV(letter):
    if letter == 'o':
        return '-vo'
    else:
        return valZero(letter)

def valVo(letter):
    if letter == 'i':
        return '-voi'
    else:
        return valZero(letter)

def valVoi(letter):
    if letter == 'd':
        return 'tipo'
    else:
        return valZero(letter)

def valW(letter):
    if letter == 'h':
        return '-wh'
    else:
        return valZero(letter)

def valWh(letter):
    if letter == 'i':
        return '-whi'
    else:
        return valZero(letter)

def valWhi(letter):
    if letter == 'l':
        return '-whil'
    else:
        return valZero(letter)
    
def valWhil(letter):
    if letter == 'e':
        return 'while'
    else:
        return valZero(letter)

def valR(letter):
    if letter == 'e':
        return '-re'
    else:
        return valZero(letter)

def valRe(letter):
    if letter == 't':
        return '-ret'
    else:
        return valZero(letter)

def valRet(letter):
    if letter == 'u':
        return '-retu'
    else:
        return valZero(letter)

def valRetu(letter):
    if letter == 'r':
        return '-retur'
    else:
        return valZero(letter)

def valRetur(letter):
    if letter == 'n':
        return 'return'
    else:
        return valZero(letter)

def valE(letter):
    if letter == 'l':
        return '-el'
    else:
        return valZero(letter)

def valEl(letter):
    if letter == 's':
        return '-els'
    else:
        return valZero(letter)

def valEls(letter):
    if letter == 'e':
        return 'else'
    else:
        return valZero(letter)

def valZero(letter):
    if letter.isalpha() or letter.isdigit():
        return 'Identificador'
    else:
        return 'Invalido'

def valOne(letter):
    if letter.isdigit():
        return 'Entero'
    elif letter == '.':
        return 'Real'
    else:
        return 'Invalido'

def valTwo(letter):
    if letter.isdigit():
        return 'Real'
    else:
        return 'Invalido'

def valThree(letter):
    if letter == '"':
        return 'Cadena'
    else:
        return 'CadenaIncompleta'

def valSeven(letter):
    if letter == '=':
        return 'OpRelac'
    else:
        return 'Invalido'

def valEight(letter):
    if letter == '|':
        return 'OpOr'
    else:
        return 'Invalido'
    
def valNine(letter):
    if letter == '&':
        return 'OpAnd'
    else:
        return 'Invalido'

def valEleven(letter):
    if letter == '=':
        return 'OpIgualdad'
    else:
        return 'Invalido'
    
def valMinus(letter):
    if letter == 'i':
        return '-i'
    if letter == 'w':
        return '-w'
    if letter == 'r':
        return '-r'
    if letter == 'e':
        return '-e'
    if letter == 'f':
        return '-f'
    if letter == 'v':
        return '-v'
    elif letter.isalpha() or letter == '_':
        return 'Identificador'
    elif letter.isdigit():
        return 'Entero'
    elif letter == '.':
        return 'Real'
    elif letter == '"':
        return 'CadenaIncompleta'
    elif letter == '+' or letter == '-':
        return 'OpSuma'
    elif letter == '*' or letter == '/':
        return 'OpMul'
    elif letter == '<' or letter == '>':
        return 'OpRelac'
    elif letter == '|':
        return 'OpOrIncompleto'
    elif letter == '&':
        return 'OpAndIncompleto'
    elif letter == '!':
        return 'OpNot'
    elif letter == '=':
        return '='
    elif letter == ';':
        return ';'
    elif letter == ',':
        return ','
    elif letter == '(':
        return '('
    elif letter == ')':
        return ')'
    elif letter == '{':
        return '{'
    elif letter == '}':
        return '}'
    elif letter == '$':
        return '$'
    else:
        return 'Error'

for sentence in sentences:
    flag = False
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
    for word in words:
        if '\n' in word:
            word = word.replace("\n"," ")
        i = 0
        typeDate = 'Inicial'
        while i < len(word):
            typeDate = valLexico(word[i], typeDate)
            i+=1
        if '-' in typeDate:
            typeDate = 'Identificador'
        print(word + "\t\t\t" + typeDate)
file.close()
