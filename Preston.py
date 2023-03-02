# Initialize outside of a loop

dDictionary = {}

# Include in the loop

sKey = CustomerObject.customer_name

# if statement to determine if the value needs to be increased or if a new entry needs to be made

if sKey in dDictionary :
    dDictionary[sKey] += CustomerObject.order
else :
    dDictionary[sKey] = CustomerObject.order

# To see integration, see the Preston_test_code.py file