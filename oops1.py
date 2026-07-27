
# Initialize  the class
class Employee:

    # constructor->the data and attributes of constructor gets called automatically as soon we create a object
    def __init__(self):
        print("Start executing attributes/data")
        self.id=226
        self.salary=50000
        self.designation="SDE"
        print("attributes and data is initialized")

    def travel(self,destination):
        print("The travel method was called manually")
        print(f"Employee is traveling to {destination} ")



# create the obj of the class
obj=Employee()
# print(obj.id)
# obj.travel("Kerala")

print(type(obj))
