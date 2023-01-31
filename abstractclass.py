# An abstract class can be considered as a blueprint for other classes.
# A class which contains one or more abstract methods is called an abstract class. 
# An abstract method is a method that has a declaration but does not have an implementation

# By defining an abstract base class, you can define a common Application Program Interface(API) for a set of subclasses.
#  This capability is especially useful in situations where a third-party is going to provide implementations, such as with plugins,
#  but can also help you when working in a large team or with a large code-base 
#  where keeping all classes in your mind is difficult or not possible. 

from abc import ABC,abstractmethod


# In Python 3.4 and above, you can inherit from ABC. In earlier versions of Python, you need to specify your class's metaclass as ABCMeta.
# Specifying the metaclass has different syntax in Python 3 and Python 2

class Vehicle(ABC):                  # declare a abstract class . Note - We have inherited ABC
    
    @abstractmethod             # going to declare a abstract method
    def ride(self):
        pass

class Car(Vehicle):             # define another class which inherits the abstract class
    
    def ride(self):             # definition the abstract method
        print('You can ride me')

# v = Vehicle()   - We can't instantiate abstract class


car1 = Car()   # create an instanace of car
car1.ride()    # call the method ( which is actually an abstract method in Vehicle class)

    
