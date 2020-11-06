ALPHA = "ABCDEFGHI"
class Cell:
    def __init__(self,index,value):
        self.relations = []
        self.domain = []
        #self.relations REAZLLY depends on the implementation of the board
        
        col = index[0]
        row = index[1]
        subCol = 3*((ord(col)- ord("A"))//3)
        subRow = 3*((int(row)-1)//3)
        for i in range(9):
            if col+str(i+1)!=index:
                self.relations.append(col+str(i+1))
        for i in range(9):
            if ALPHA[i]+row!=index:
                self.relations.append(ALPHA[i]+row)
        for i in range(3):
            for n in range(3):
                temp = ALPHA[subCol+i] + str(subRow+1+n)
                if temp!=index and temp not in self.relations:
                    self.relations.append(temp)
        if value == ".":
            self.domain = ['1','2','3','4','5','6','7','8','9']
        else:
            self.domain = [value]
            
    def constrain(self,other):
        if len(other.domain)==1:
            if other.domain[0] in self.domain:
                self.domain.remove(other.domain[0])
                return True
            
        return True
        
        
class Constraint:
    def __init__(self,cellA,cellB):
        self.current = cellA
        self.other = cellB
    def arc_consist(self):
        return self.current.constrain(self.other)

temp = Cell("A1","2")
temp1 = Cell("I9",".")



#print(temp.relations)
#print(temp.domain)