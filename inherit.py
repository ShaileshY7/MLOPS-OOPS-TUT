

class Animal():
    def __init__(self,name):
        self.name=name

    def speak(self):
        print(f"{self.name} makes sound")

class Dog(Animal):
    def speak(self):
        print(f"{self.name} barks")

obj=Animal("Lion")
obj.speak()

dog=Dog("buddy")
dog.speak()



# Super Keyword

# Super

# Base class
class Animal:
    def __init__(self):
        self.name = "Buddy"

    def speak(self):
        print(f"{self.name} makes a sound.")

# # Derived class
class Dog(Animal):
    def __init__(self, breed):
        super().__init__()
        self.breed = breed

    def speak(self):
        super().speak()  # Call the base class method
        print(f"{self.name} barks. It is a {self.breed}.")

# # Create an instance of Dog
dog = Dog("Golden Retriever")
dog.speak()
# Output:
# Buddy makes a sound.