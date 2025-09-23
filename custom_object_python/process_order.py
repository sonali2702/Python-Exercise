import json
import logging


logging.basicConfig(level=logging.INFO)


# Read the JSON file in try/except block, parse it into a 
# Python dictionary and log the dictionary variable

try:
    with open('order_data.json' , 'r') as  file :
        data=json.load(file)
        print(data)
        
except FileNotFoundError:
    print("Error : order_data.json File is not found  ")
    


# --- Accessing Nested Fields ---

# Access a top-level field "order_id" and log using info level
## Your code here

print(f" Processing Order ID : {data['order_id'] }")  
logging.info(data['order_id'])


# Access a field within a nested object, (customer --> name) and 
# (customer -> address -> city). Log using info level
## Your code here
customer = data['customer']
print(f" Customer : {customer['name']} from {customer['address']['city']}" )


# --- Processing a Nested List ---
# Get total cost of the all the items and log the total billing amount
print("\nOrder Items:")
total_cost = 0.0
# The 'items' key holds a list of dictionaries
## Your code here
    
for i in data['items']:
    
    # print(f" - {i['product_name']} (X{i['quantity']}) = $ {i['price']}")
    
    logging.info(f" - {i['product_name']} (X{i['quantity']}) = $ {i['price']}")
    
    total_cost+= i['price']
    print(f" Total Order Cost : ${total_cost}")
    logging.info(f" Total Order Cost : ${total_cost}")