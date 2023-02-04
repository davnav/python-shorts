class Car:    # let us define a class Car
    name = ""   # class variable
    def __init__(self):
       self.value = 0 

    def normal_method(self,value):  #normal method which has a parameter self
        self.value = value    # assigning the instance variable a value
    @classmethod  # we are planning to define a class method, so using the decorator
    def assign_name(cls,name):  # define the class method - Note that first argument to the method is class
        cls.name = name  # class variable updates with passed parameter

Car.assign_name('cx30')  #this is how we call the class method - Note class with dot operatr on the method
print(Car.name) # you can print the updated class veriable with 

car1 = Car()    # creating an instance
car1.normal_method(1000) #calling normal method with dot opertator with instance

print(car1.value)
