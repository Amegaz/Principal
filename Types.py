class Types:
    def __init__(self):
        item = 0

    def printType(self,x):
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
