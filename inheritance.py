class animal:
    def __init__(self,name):
        self.name=name

    def speak(self):
        pass
class Dog(animal):
    def speak(self):
        return "woof"
my_dog=Dog("simba")
print(my_dog.name)
print(my_dog.speak())