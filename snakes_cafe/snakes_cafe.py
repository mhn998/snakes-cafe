print("""**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************""")

Appetizers = ["Appetizers" , "Wings" , "Cookies" , "Spring Rolls"]
Entrees = [ "Salmon" ,"Steak" ,"Meat Tornado", "A Literal Garden"]
Desserts = ["Ice Cream" , "Cake" ,"Pie"]
Drinks = ["Coffee" ,"Tea" ,"Unicorn Tears"]

print('''
    Appetizers
    ----------
''')
for item in Appetizers:
    print(item)
    
print('''
    Entrees
    -------
''')

for item in Entrees:
    print(item)
    
print('''
    Desserts
    --------
''')

for item in Desserts:
    print(item)
    
print('''
    Drinks
    ------
''')

for item in Drinks:
    print(item)
    

print('''***********************************
** What would you like to order? **
***********************************''')

Menu = Appetizers + Entrees + Desserts + Drinks

ordered = []
# order = input(">")


while(True):
    order = input(">")
      
    if order in Menu:
        ordered.append(order)  
        print("**", ordered.count(order), "order of", order, "have been added to your meal**")
    else:
        if(order!='quit'):
            print('invalid order! please choose from the Menu')
        
    if order == 'quit':
        print("This is your complete order accordingly" , ','.join(ordered))
        break;