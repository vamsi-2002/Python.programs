class car:
    def __init__(self,modelname,year):
        self.modelname = modelname
        self.year = year
    def display(self):
        print(self.modelname,self.year)
C1 = car("bmw",2016)
C2 = car("audi",2019)
C3 = car("bently",2023)
C1.display()
C2.display()
C3.display()

