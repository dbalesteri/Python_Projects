# Dan Balesteri - Python 3.9.0 - Windows 10
#
# ABSTRACTION ASSIGNMENT
# Create a class that utilizes the concept of abstraction.
#
# 1. Your class should contain at least one abstract method and one regular method.
#
# 2. Create a child class that defines the implementation of its parents abstract method.
#
# 3. Create an object that utilizes both the parent and child methods.

from abc import ABC, abstractmethod

class Animal(ABC):
        
    def eat(self, food):
        print("This animal has decided to eat {} for fuel.".format(food))

    @abstractmethod
    def call(self, noise):
        pass

class Species(Animal):
    def call(self, noise):
        print("This species makes a {} sound to alert other animals.".format(noise))

dog = Species()
dog.eat("dropped popcorn")
dog.call("bark")

snake = Species()
snake.eat("mice")
snake.call("rattle")
