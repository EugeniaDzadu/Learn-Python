
# *******Pella Store*******
# 1. Buy Item
# 2. View Cart 
# 3. Remove from cart
# 4. Make purchase
# 5. About Us 
# 6. Exit app

# Console colours

item_database = []
item_input = 0
while item_input != 6:
    item_input = int(input('******Pella Store****** \n'
                           '1. Buy Item \n'
                           '2. View Cart \n'
                           '3. Remove from cart \n'
                           '4. Make purchase \n'
                           '5. About Us \n'
                           '6. Exit App \n\n'
                           'Provide options: '))
    if item_input == 1:
        product = (input('Enter product: '))
        quantity  = int(input('Enter quantity: '))
        price_per_product = int(input('Enter price per product: '))
        if item_database.count(product):
           item_database.append(product)
           total_price = quantity*price_per_product
           print(f"{total_price}GHC")
        
    elif item_input == 2:
        if len(item_database)!=0:
            for i in item_database:
                print(i)
        else:
            print('Your shopping cart is empty')
            
    elif item_input == 3:
        item_remove =input('Enter product to remove: ')
        if len(item_database)!=0:
           item_remove in item_database
           item_database.remove(item_remove) 
           print('Item removed from cart succesfully')
        else:
                print('Product can not be found in the cart')
              
    elif item_input == 4:
        print(f"{total_price}GHC")
        payment = (input('Enter payment: '))
        item_database.append(payment)
        print(f'{payment}GHC \n Transaction successful')
        print('Thanks for shopping with Pella Stores,\n Have a nice day!')
         
    elif item_input == 5:
        print('You are welcome to Pella store, \n' 
              'the best grocery vendors in the city of Kumasi \n' 
              'please feel free to ask the shop attendants for help if you need one.\n' 
              'HAPPY SHOPPING!!')
        
    elif item_input == 6:
        break