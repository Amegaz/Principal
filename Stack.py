class Stack:
    def __init__(self):
        self.items = []

    def push(self,x):
        self.items.append(x)

    def pop(self):
        try:
            return self.items.pop()
        except IndexError:
            raise ValueError("Pila vacia")

    def top(self):
        self.value = int(self.items[-1])
        return (self.value)

    def clear(self):
        self.items = []

    def see(self,sen=""):
        for i in self.items:
            print(sen + str(i.val))

class ElementoPila:
    def __init__(self,x):
        self.val = x

class Terminal(ElementoPila):
    def __init__(self,x):
        ElementoPila.__init__(self,x)

class NoTerminal(ElementoPila):
    def __init__(self,x):
        ElementoPila.__init__(self,x)

class Estado(ElementoPila):
    def __init__(self,x):
        ElementoPila.__init__(self,x)
