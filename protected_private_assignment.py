#   Dan Balesteri - Python 3.9.0 - Windows 10
#
# ENCAPSULATION ASSIGNMENT
# Create a class that uses encapsulation.
#
# 1. This class should make use of a private attribute or function.
#
# 2. This class should make use of a protected attribute or function.
#
# 3. Create an object that makes use of protected and private.

class Person:
    def __init__(self):
        self.__ssn = "123-45-6789"
        self._name = ""

    def getSSN(self):
        print(self.__ssn)

    def setSSN(self, newSSN):
        self.__ssn = newSSN

steve = Person()
steve._name = "Steve"
print(steve._name)
steve.getSSN()
steve.setSSN("987-65-4321")
steve.getSSN()
