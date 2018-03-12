import Types
import Lexico
import Stack
import Sintactico
global sen
file = open("sentences.txt")
otro = file.read()
sentences = otro.split('\n')
tipo = Types.Types()
lexico = Lexico.Lexico()
stack = Stack.Stack()
sintactico = Sintactico.Sintactico()

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
            typeDate = lexico.valLexico(word[i], typeDate)
            print(word[i],end='')
            i+=1
        print("\t" + tipo.printType(typeDate))
        sen += str(sintactico.asig(typeDate))
    sen += '2'
    print(sen)
    stack.push(2)
    stack.push(0)
    for leer in sen:
        sintactico.re(leer,stack)
    sintactico.re(leer,stack)
file.close()
