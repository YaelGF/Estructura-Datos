class Pila():    
    def __init__(self):
        self.lista = []
        self.tope = 0
        self.size = 0
    
    def empty(self):
        if self.tope == 0:
            return True
        else:
            return False
    
    def push(self,dato):
        if self.tope < self.size:
            self.lista += [dato]
            self.tope += 1
        else:
            self.size += 5
            self.lista +=[dato]
            self.tope += 1

    def pop(self):
        if self.empty():
            print("La pila esta vacia")
        else:
            self.tope -= 1
            self.lista = [self.lista[x] for x in range(self.tope)]

    def show(self):
        i = self.tope -1
        while i > -1:
            print("[%d]  => %d"%(i, self.lista[i]))
            i -= 1

    def Size(self):
        return self.tope
    
    def Top(self):
        return self.lista[-1]