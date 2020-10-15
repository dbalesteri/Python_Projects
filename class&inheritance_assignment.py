#   Python: 3.9.0
#
#   Author: Dan S. Balesteri
#
#   Purpose: The Tech Academy - Python Course
#       page 185
# Create two classes that inherit from another class.
# Each child should have at least two of their own attributes.
# 
#
import math

class Animal:
    name = "No Name Provided"
    numberOfLegs =  0
    diet = ''
    habitat = ''
    scientificName = ''

class Bird(Animal):
    flyDistanceM = 0
    beakLengthIn = 0
    
class Dog(Animal)
    bestFriend = True
    loyalty = math.inf
