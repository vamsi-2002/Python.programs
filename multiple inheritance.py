#class parent:
 #   def methord(self):
  #      print("methord1 from class parent")
#class parent2:
 #   def methord2(self):
  #      print("methord2 from class parent2")
#class child(parent,parent2):
 #   def methord3(self):
  #      print("methord3 from class child")

#obj = child()
#obj.methord()
#obj.methord2()
#obj.methord3()                        



class base1:
    def greet(self):
        print("hello")
class base2:
    def greet(self):
        print("welcome")

class derived(base1,base2):
    def greet(self):
        base1.greet(self)
        base2.greet(self)
obj = derived()
obj.greet()