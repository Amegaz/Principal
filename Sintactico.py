class Sintactico:
    w = [0]
    
    def __init__(self):
        fi = open("compilador.lr").read().split("\n")
        #print(fi[0])
        #for i in range(int(fi[0])):
        #    print(fi[i+1])
        #print(fi[int(fi[0])+1])
        size = fi[int(fi[0])+1].split("\t")
        self.w = [0] * int(size[1])
        self.w = [self.w] * int(size[0])
        j = 0
        for i in range(int(fi[0])+2,int(size[0])+int(fi[0])+2):
            self.w[j] = fi[i].split("\t")
            #print(self.w[j])
            j+=1

    def re(self,leer,stack):
        print("Entrada: ",leer)
        estado = self.s[stack.top()][int(leer)]
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
            estado = self.s[stack.top()][3]
            stack.push(3)
            stack.push(estado)
        elif estado == -1:
            print("Aceptado")
        else:
            print("Error al validar")

    def sintact(self,leer,stack):
        print("Entrada: ",leer)
        estado = int(self.w[stack.top()][leer])
        print("Salida: ",estado)
        stack.push(leer)
        stack.push(estado)
        if estado > 0:
            print("Error al validar")
        elif estado < -1:
            #reduction()
            if estado == -8:
                stack.clear()
                stack.push(23)
                stack.push(0)
                stack.push(27)
                stack.push(7)
        else:
            print("Aceptado")
