
'''
9. Create a shopping cart for the below bakery_items using dictionary or list

bakery_items = {"Bread":40, "Butter":120, "Jam":200, "Cheese":220, "Crossiant":60}

Menu for operations
 print(""" Enter choice
            1. View the bakery items
            2. Add the item into the cart
            3. View the cart
            4. Update item in the cart
            5. Remove item from the cart
            6. Checkout and generate bill
            """)
           
Based on the menu , I should able to create mycart

'''



bakery_items = {"Bread":40, "Butter":120, "Jam":200, "Cheese":220, "Crossiant":60}
ch=0
my_cart={}
while(ch!=6):
    ch=int(input(""" Enter choice
                1. View the bakery items
                2. Add the item into the cart
                3. View the cart
                4. Update item in the cart
                5. Remove item from the cart
                6. Checkout and generate bill
                """))
    if(ch==1):
        print(bakery_items)
    elif(ch==2):
        item=input("Enter the item to buy:")
        quantity=int(input("Enter the quantity :"))
        my_cart[item]=quantity;
    elif(ch==3):
        print(my_cart)
    elif(ch==4):
        item=input("Enter the item to be change the quantity: ")
        quantity=int(input("Enter the quantity :"))
        my_cart[item]=quantity;
    elif(ch==5):
        item=input("Enter the item to be remove: ")
        my_cart.pop(item)
    elif(ch==6):
        total=0
        for i in my_cart:
            total=total+(bakery_items[i]*my_cart[i])
        print("Total amount:",total)
        break;
    else:
        print("Invalid choice!!!")

        

