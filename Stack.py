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
