class Animal:
    def speak(self):
        print("animal speaking")

class dog(Animal):
    def bark(self):
        print("dog barking")

class husky(dog):
    def eyes(self):
        print("has blue eyes")

obj = husky()
obj.speak()
obj.bark()
obj.eyes()                      