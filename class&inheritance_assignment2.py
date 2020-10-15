#   Python: 3.9.0
#
#   Author: Dan S. Balesteri
#
#   Purpose: The Tech Academy - Python Course
#       page 193
# Create two classes that inherit from another class.
# 1. Each child should have at least two of their own attributes.
# 2. The parent class should have at least one method (function).
# 3. Both child classes should utilize polymorphism on the parent class method.
# 
#
import math

class Animal:
    name = "No Name Provided"
    numberOfLegs =  0
    diet = ''
    habitat = ''
    scientificName = ''

    def feed(self):
        msg = "\nThe animal exhibits it's feeding behavior.\n"
        return msg

class Bird(Animal):
    flyDistanceM = 0
    beakLengthIn = 0
    def feed(self):
        msg = "\nThis bird uses its gizzard to crush down food.\n"
        return msg
    
class Dog(Animal):
    bestFriend = True
    loyalty = math.inf
    def feed(self):
        msg = "\nThis dog eats any and all food currently available to it.\n"
        return msg

dog = Dog()
bird = Bird()

if __name__ == "__main__":
    print(dog.feed())
    print(bird.feed())
