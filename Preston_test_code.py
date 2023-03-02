from random import randint

class Order :
    def __init__(self):
        self.burger_count = self.randomBurgers()


    def randomBurgers(self) :
        iBurgers = randint(1,20)
        return iBurgers

class Person :

    def __init__(self) :
        self.customer_name = self.randomName()

    def randomName(self) :
        self.asCustomers = ["Jefe", "El Guapo", "Lucky Day", "Ned Nederlander", "Dusty Bottoms", "Harry Flugleman", "Carmen", "Invisible Swordsman", "Singing Bush"]
        return(self.asCustomers[randint(0,8)])
    
class Customer(Person) :

    def __init__(self):
        super().__init__()
        self.order = Order().burger_count

dDictionary = {}

for iCount in range(0, 100):
    oCustomer = Customer()
        
    sKey = oCustomer.customer_name

    if sKey in dDictionary :
        dDictionary[sKey] += oCustomer.order
    else :
        dDictionary[sKey] = oCustomer.order

for key, value in dDictionary.items() :
    print(str(key) + ":" + str(value)) 
