import os
os.system('cls' if os.name == 'nt' else 'clear')

#! Topics to be Covered:
#* Everything in Python is class
#* Defining class
#* Defining class attributes
#* Difference between class attributes and instance attributes
#* SELF keyword
#* Defining methods
#* Class Methods vs. Static Methods and Instance Methods
#* Special methods (init, str)
#* 4 pillars of OOP:
    #? Encapsulation
    #? Abstraction
    #? Inheritance
        #? Multiple inheritance
    #? Polymorphism
        #? Overriding methods
#* Inner class
#* Overloading an operator (optional)
#* Abstract base class 


#! What is OOP?
""" # Object Oriented programming (OOP) is a programming paradigm that relies on the concept of classes and objects.
# It is used to structure a software program into simple, reusable pieces of code blueprints (usually called classes), which are used to create individual instances of objects.
# significantly reduces code repetition by classifying similar structures (dont repeat yourself)
# Easier to debug, classes often contain all applicable information to them
# Secure, protects information through encapsulation """


#! Everything in Python is class
# Python >generally class based  vs.  javascript >generally function based

def print_types(data):
    for i in data:
        print(i, type(i))

test = [122, "victor", [1,23,2], {1,2,3,4}, True, lambda x:x]

print_types(test)


#! Defining Class
# It is a convention to name the classes capitalized.

class Person:
    name = "victor",
    age = 33

person1 = Person()  #creating object or instance
person2 = Person()

print(person1.name)  # instances inherits class attributes
print(person2.age)


print(person1.job)  # attribute error
Person.job = "developer"
print(person1.job)  # developer


#! Class Attributes and Instance Attributes

class Employee:
    company = "Amazon"

    def set_details(self, name, age):
        self.name = name
        self.age = age

    def get_details(self):
        print(f"{self.name}- {self.age}")

    @staticmethod  # static methods(no parameter)
    def salute():
        print("hi there")

employee1 = Employee()
employee2 = Employee()

employee1.location = "Turkiye"
employee1.company = "Tesla"
print(employee1.company)  # Tesla
print(employee2.company)  # Amazon
print(employee2.location)  # Attribute error
print(employee1.location)  # Turkiye

employee1.name = "victor"
employee1.age = 33
employee1.get_details()  # victor- 33

employee2.set_details("henry", 25)
employee2.get_details()  # henry- 25

employee1.salute()



#! Special Methods (dunder methods)

class Personel:
    company = "amazon"
    personel_count = 0

    def __init__(self,name,age, gender = "male"):  # it is called automatically so we have to send argunments in Personel() to create an instance
        self.name = name
        self.age = age
        self.gender = gender
        Personel.personel_count += 1

    def __str__(self):
        return f"{self.name}-{self.age} "


    def get_details(self):
        print(f"{self.name}- {self.age} - {self.gender}")

personel1 = Personel("hasan", 36)
personel1.get_details()

# personel2 = Personel()  # TypeError because of args.

personel2 = Personel("ali", 30)
print(Personel.personel_count)

print(personel1)
print(personel2.company)  # amazon


#! OOP PRINCIPLES (4 PILLARS)
    #? Encapsulation
    #? Abstraction
    #? Inheritance
    #? Polymorphism

#? Encapsulation
# The principle in which we determine how much of the classes, data and methods can be viewed and changed by the user.
    # public- private -protected (not in js and python)
    # there is not a complete encapsulation in Pyhton.
class Personels:
    company = "amazon"

    def __init__(self,name,age, gender = "male"):  # it is called automatically so we have to send argunments in Personel() to create an instance
        self.name = name
        self.age = age
        self.gender = gender
        self._id = 5000  
        self.__number = 200

    def __str__(self):
        return f"{self.name}-{self.age} "


    def get_details(self):
        print(f"{self.name}- {self.age} - {self.gender}")

personels1 = Personels("hasan", 36)
print(personels1._id)  # can be reached --5000
print(personels1.__number)  # cannot be reached
print(personels1._Personels__number)  # can be reached --200


#? Abstraction
    # Abstraction is the proess of hiding the internal complex details of an application from the outer world.

liste = [2,3,5,1,4]
liste.sort()
print(liste)

# class Update(models.Model):
#     updated = models.DateTimeField("auto_now_true")

#     class Meta:
#         abstract = True

# class Question(Update):
#     pass
# class Answer(Update):
#     pass