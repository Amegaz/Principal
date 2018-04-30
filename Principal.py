import Files
import Types
import Lexico
import Stack
import Sintactico
global sen
file = Files.Files("sentences.txt")
sentences = file.readSentences()
tipo = Types.Types()
lexico = Lexico.Lexico()
stack = Stack.Stack()
cadena = Stack.Stack()
sintactico = Sintactico.Sintactico()

def compilador():
    for sentence in sentences:
        if sentence == "":
            continue
        if '"' in sentence:
            flag = False
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
            i = 0
            typeDate = -1
            while i < len(word):
                typeDate = lexico.valLexico(word[i], typeDate,cadena)
                print(word[i],end='')
                i+=1
            print("\t" + tipo.printType(typeDate))
            cadena.push(typeDate)
        cadena.push(23)
        #print("Cadena:" + str(cadena.items))
        stack.push(23)
        stack.push(0)
        #print("Stack:" + str(stack.items))
        for leer in cadena.items:
            print("Cadena:" + str(cadena.items))
            print("Stack:" + str(stack.items))
            sintactico.sintact(leer,stack)
        print("Cadena:" + str(cadena.items))
        print("Stack:" + str(stack.items))
        stack.clear()
        cadena.clear()
        
compilador()
