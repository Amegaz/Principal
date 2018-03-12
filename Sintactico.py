class Sintactico:
    t = [[0,0,0,0,0] for i in range(5)]
    s = [[0,0,0,0,0] for i in range(5)]    
    
    def __init__(self):
        self.s[0][0] = 2
        self.s[0][1] = 0
        self.s[0][2] = 0
        self.s[0][3] = 1

        self.s[1][0] = 0
        self.s[1][1] = 0
        self.s[1][2] = -1
        self.s[1][3] = 0

        self.s[2][0] = 0
        self.s[2][1] = 3
        self.s[2][2] = 0
        self.s[2][3] = 0

        self.s[3][0] = 4
        self.s[3][1] = 0
        self.s[3][2] = 0
        self.s[3][3] = 0

        self.s[4][0] = 0
        self.s[4][1] = 0
        self.s[4][2] = -2
        self.s[4][3] = 0

        self.t[0][0] = 2
        self.t[0][1] = 0
        self.t[0][2] = 0
        self.t[0][3] = 1

        self.t[1][0] = 0
        self.t[1][1] = 0
        self.t[1][2] = -1
        self.t[1][3] = 0

        self.t[2][0] = 0
        self.t[2][1] = 3
        self.t[2][2] = -3
        self.t[2][3] = 0

        self.t[3][0] = 2
        self.t[3][1] = 0
        self.t[3][2] = 0
        self.t[3][3] = 4

        self.t[4][0] = 0
        self.t[4][1] = 0
        self.t[4][2] = -2
        self.t[4][3] = 0        

    def asig(self,x):
        if x < 3:
            return 0
        elif x == 5:
            return 1
        elif x == 23:
            return 2
        else:
            return 3

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
