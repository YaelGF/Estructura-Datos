class Cola():    
    def __init__(self):
        self.cola = []
        self.size = 0
    
    def empty(self):
        return len(self.cola) == 0
    
    def push(self,dato):
        self.cola += [dato]
        self.size += 1

    def popi(self):
        if self.empty():
            print("La cola esta vacia")
        else:
            self.cola = [self.cola[x] for x in range(1,self.size)]
            self.size -= 1

    def show(self):
        n = self.size -1
        while n > -1:
            print("[%d]  => %d"%(n, self.cola[n]))
            n -= 1

    def Size(self):
        return self.tope
    
    def front(self):
        if self.empty():
            print("La cola esta vacia")
        else:
            print("primer dato: %d"%(self.cola[0]))