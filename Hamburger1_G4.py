# Authors: Michael Underwood, Michael Hutchings,
# Lily Pettit, Elliot Pi, Noelle Burton, Preston Fitzgerald

# THIS IS THE MASTER - DO NOT DELETE WORK
# WORK WITHIN YOUR OWN BRANCH - WILL WILL MERGE CAHNGES WHEN WE EACH HAVE OUR PORTIONS DONE 
# ESSENTIALLY WE WILL BE COPY AND PASTING EACHOTHERS WORK FROM THE INDIVIDUAL BRANCHES AND CHECKING TO SEE IF IT WORKS. 

# LILLY 

# NOELLE

# MICHAEL U

#  This is where Preston will start working on a dictionary. Here's hoping nothing will break

# ELLIOT

# MICHAEL H

# Michael Hutchings

# Making a dictionary to make sure the code works

dictCustomer = {"Greg" : 0,
                "Bob" : 5,
                "Angela" : 10,
                "Kevin" : 15}

# Print the format of the original dictionary values and its order

print("The original dictionary is",str(dictCustomer),"\n")

# Mock name input and burger count input for testing purposes

name = input("What is the name")
burgers = 10 #The number given

# Checking if the name supplied is already in the dictionary. If it is, add to the value
# If the name is not in the dictionary, add it to the dictionary with the value

if name in dictCustomer:
    dictCustomer[name] = int(dictCustomer[name]) + int(burgers)
else:
    dictCustomer[name] = burgers

# Declaring a list with the keys and values of the dictionary, but sorted. 

listSortedCustomers = sorted(dictCustomer.items(), key=lambda kv: kv[1], reverse=True)

# Printing out the list to verify that it is correct

print("The sorted list is:",listSortedCustomers,"\n")

iCount = 0

# For loop to print the concatenated result 'meow'

for i in listSortedCustomers :
    print(str(listSortedCustomers[0+iCount][0]),"ate",str(listSortedCustomers[0+iCount][1]),"burgers")
    iCount = iCount +1
