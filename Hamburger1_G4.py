# Authors: Michael Underwood, Michael Hutchings,
# Lily Pettit, Elliot Pi, Noelle Burton, Preston Fitzgerald

# "track exactly how many hamburgers each customer eats."

import random
from random import randint
from collections import deque
# create class Order
class Order:
    def __init__(self):
        self.burger_count = self.randomBurgers()
# create method
    def randomBurgers(self) :
        return random.randint(1, 20)
# create class Person
class Person :
    # initialize constructor and attribute customer_name
    def __init__(self) :
        self.customer_name = ""
    # method randomName that randomly returns one name from our list of 9 names
    def randomName(self) :
        asCustomers = ["Jefe", "El Guapo", "Lucky Day", "Ned Nederlander", "Dusty Bottoms", "Harry Flugleman", "Carmen", "Invisible Swordsman", "Singing Bush"]
        return random.choice(asCustomers)
class Customer(Person):
    def __init__(self):
        super().__init__()
        self.order = Order()
        
# The Queue is here
queCustomers = []
# Input for how many customers to run in the loop
iNumCustomer = int(input("Numbers of customers: "))
randNum = 0
# Loop to create the queue with random numbers. Uses the input for the proper amount of times to loop
for iCount in range(0, iNumCustomer):
    # Creates the object
    oCustomer = Customer()
    # Declares the variable with the random number method
    randNum = oCustomer.order.burger_count
    # Adds that random number to the queue
    queCustomers.append(randNum)
# Prints the queue to make sure it worked
print(queCustomers)
# Declares our doordasher dictionary
dictCustomer = {"Jefe" : 0,
                "El Guapo" : 0,
                "Lucky Day" : 0,
                "Ned Nederlander" : 0,
                "Dusty Bottoms" : 0,
                "Harry Flugleman" : 0,
                "Carmen" : 0,
                "Invisible Swordsman" : 0,
                "Singing Bush" : 0}

# Declares object
asCust = Customer()
# Declared list variable
asCustomer = []
# For loop to add our random number queue to the doordasher dictionary
for iCount in range(0,len(queCustomers)) :
    # Declared variable with method
    asCustomer = asCust.randomName()
    # Updates dictionary
    dictCustomer[asCustomer]+=queCustomers[0]
    # Prints updated first number in queue each time to guarantee that it works
    print(queCustomers[0])
    # Pop the number we just used
    queCustomers.pop(0)

# Declaring a list with the keys and values of the dictionary, but sorted.
listSortedCustomers = sorted(dictCustomer.items(), key=lambda kv: kv[1], reverse=True)
# Printing out the list to verify that it is correct
print("The sorted list is:",listSortedCustomers,"\n")
iCount = 0

# For loop to print the concatenated result 'meow'
for i in listSortedCustomers :
    print(str(listSortedCustomers[0+iCount][0]),"delivered",str(listSortedCustomers[0+iCount][1]),"burgers")
    iCount = iCount +1


