# Person class

from random import randint

# create class Person
class Person :
    # initialize constructor and attribute customer_name
    def __init__(self) :
        customer_name = ""

    # method randomName that randomly returns one name from our list of 9 names
    def randomName(self) :
        asCustomers = ["Jefe", "El Guapo", "Lucky Day", "Ned Nederlander", "Dusty Bottoms", "Harry Flugleman", "Carmen", "Invisible Swordsman", "Singing Bush"]
        
        # assign a random value 0 - 8 to variable iRandom
        iRandom = randint(0,8)

        # return the value from the list in the random position
        sReturn = asCustomers.pop(iRandom)
        return str(sReturn)
