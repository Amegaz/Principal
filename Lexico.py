file = open("sentences.txt")
otro = file.read()
sentences = otro.split('\n')

def valLexico(letter, state):
    if state == 'Inicial':
        state = valMinus(letter)
    elif state == 'Identificador':
        state = valCero(letter)
    elif state == 'Entero':
        state = valOne(letter)
    elif state == 'Real':
        state = valTwo(letter)
    elif state == 'int':
        state = valFourInt(letter)
    elif state == 'i':
        state = valNineten(letter)
    elif state == 'float1':
        state = valFourF(letter)
    elif state == 'float2':
        state = valFourFl(letter)
    elif state == 'float3':
        state = valFourFlo(letter)
    elif state == 'float4':
        state = valFourFloa(letter)
    elif state == 'float':
        state = valCero(letter)
    elif state == 'void1':
        state = valFourV(letter)
    elif state == 'void2':
        state = valFourVo(letter)
    elif state == 'void3':
        state = valFourVoi(letter)
    elif state == 'void':
        state = valCero(letter)
    elif state == 'OpSuma' or state == 'OpMul' or state == 'OpOr' or state == 'OpAnd' or state == 'if':
        state = 'Cadena'
    elif state == state == ';' or state == ',' or state == '(' or state == ')' or state == '{' or state == '}':
        state = 'Cadena'
    elif state == 'OpRelac':
        state = valSeven(letter)
    elif state == 'OpOr1':
        state = valEight(letter)
    elif state == 'OpAnd1':
        state = valNine(letter)
    elif state == 'OpNot':
        state = valCero(letter)
    elif state == 'while1':
        state = valTwentyW(letter)
    elif state == 'while2':
        state = valTwentyWh(letter)
    elif state == 'while3':
        state = valTwentyWhi(letter)
    elif state == 'while4':
        state = valTwentyWhil(letter)
    elif state == 'while':
        state = valCero(letter)
    elif state == 'return1':
        state = valTwentyoneR(letter)
    elif state == 'return2':
        state = valTwentyoneRe(letter)
    elif state == 'return3':
        state = valTwentyoneRet(letter)
    elif state == 'return4':
        state = valTwentyoneRetu(letter)
    elif state == 'return5':
        state = valTwentyoneRetur(letter)
    elif state == 'return':
        state = valCero(letter)
    elif state == 'else1':
        state = valTwentytwoE(letter)
    elif state == 'else2':
        state = valTwentytwoEl(letter)
    elif state == 'else3':
        state = valTwentytwoEls(letter)
    elif state == 'else':
        state = valCero(letter)
    return state

def valTwentytwoEls(letter):
    if letter == 'e':
        return 'else'
    else:
        return valCero(letter)

def valTwentytwoEl(letter):
    if letter == 's':
        return 'else3'
    else:
        return valCero(letter)

def valTwentytwoE(letter):
    if letter == 'l':
        return 'else2'
    else:
        return valCero(letter)

def valTwentyoneRetur(letter):
    if letter == 'n':
        return 'return'
    else:
        return valCero(letter)
def valTwentyoneRetu(letter):
    if letter == 'r':
        return 'return5'
    else:
        return valCero(letter)
def valTwentyoneRet(letter):
    if letter == 'u':
        return 'return4'
    else:
        return valCero(letter)
    
def valTwentyoneRe(letter):
    if letter == 't':
        return 'return3'
    else:
        return valCero(letter)
def valTwentyoneR(letter):
    if letter == 'e':
        return 'return2'
    else:
        return valCero(letter)

def valTwentyWhil(letter):
    if letter == 'e':
        return 'while'
    else:
        return valCero(letter)

def valTwentyWhi(letter):
    if letter == 'l':
        return 'while4'
    else:
        return valCero(letter)

def valTwentyWh(letter):
    if letter == 'i':
        return 'while3'
    else:
        return valCero(letter)

def valTwentyW(letter):
    if letter == 'h':
        return 'while2'
    else:
        return valCero(letter)

def valNineten(letter):
    if letter == 'f':
        return 'if'
    elif letter == 'n':
        return 'int'
    else:
        return valCero(letter)

def valSeven(letter):
    if letter == '=' and len(sentence) == 2:
        return 'OpRelac'
    else:
        return valCero(letter)

def valEight(letter):
    if letter == '|':
        return 'OpOr'
    else:
        return valCero(letter)

def valNine(letter):
    if letter == '&':
        return 'OpAnd'
    else:
        return valCero(letter)

def valFourVoi(letter):
    if letter == 'd':
        return 'void'
    else:
        return valCero(letter)

def valFourVo(letter):
    if letter == 'i':
        return 'void3'
    else:
        return valCero(letter)

def valFourV(letter):
    if letter == 'o':
        return 'void2'
    else:
        return valCero(letter)

def valFourFloa(letter):
    if letter == 't':
        return 'float'
    else:
        return valCero(letter)

def valFourFlo(letter):
    if letter == 'a':
        return 'float4'
    else:
        return valCero(letter)

def valFourFl(letter):
    if letter == 'o':
        return 'float3'
    else:
        return valCero(letter)

def valFourF(letter):
    if letter == 'l':
        return 'float2'
    else:
        return valCero(letter)

def valFourInt(letter):
    if letter == 't' and len(sentence) == 3:
        return 'int'
    else:
        return valCero(letter)

def valTwo(letter):
    if letter.isdigit():
        return 'Real'
    else:
        return 'Cadena'

def valOne(letter):
    if letter.isdigit():
        return 'Entero'
    elif letter == '.':
        return 'Real'
    else:
        return 'Cadena'

def valCero(letter):
    if letter.isalpha() or letter.isdigit():
        return 'Identificador'
    elif letter == '+' or letter == '-' or letter == '*' or letter == '/' or letter == ';' or letter == ',' or letter == '.' or letter == '(' or letter == ')' or letter == '{' or letter == '}' or letter == '<' or letter == '>' or letter == '=' or letter == '!':
        return 'Cadena'
    else:
        return 'No reconocido'

def valMinus(letter):
    if letter == 'i':
        return 'i'
    elif letter == 'f':
        return 'float1'
    elif letter == 'v':
        return 'void1'
    elif letter == 'w':
        return 'while1'
    elif letter == 'r':
        return 'return1'
    elif letter == 'e':
        return 'else1'
    elif letter.isalpha():
        return 'Identificador'
    elif letter.isdigit():
        return 'Entero'
    elif letter == '.':
        return 'Real'
    elif letter == '+':
        return 'OpSuma'
    elif letter == '-':
        return 'OpSuma'
    elif letter == '*':
        return 'OpMul'
    elif letter == '/':
        return 'OpMul'
    elif letter == '<':
        return 'OpRelac'
    elif letter == '>':
        return 'OpRelac'
    elif letter == '|':
        return 'OpOr1'
    elif letter == '&':
        return 'OpAnd1'
    elif letter == '!':#Se comparte con es distinto de !=
        return 'OpNot'
    elif letter == '=':
        return 'OpIgualdad'#Se comparte con el de igualar =
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
        return 'No reconocido'

def valChar(letter, state):
    if letter.isalpha():
        return 'Identificador'
    elif letter.isdigit():
        if state!='Real':
            return 'Entero'
        else:
            return 'Real'
    elif letter == '.':
        return 'Real'

for sentence in sentences:
    i = 0
    typeDate = 'Inicial'
    while i < len(sentence):
        typeDate = valLexico(sentence[i], typeDate)
        #typeDate = valChar(sentence[i], typeDate)
        print(sentence[i], typeDate)
        i+=1
    print(typeDate + "\n")
file.close()
