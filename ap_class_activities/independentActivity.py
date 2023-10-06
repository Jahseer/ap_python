# create a function that will add a new list item to a checkout cart
# the user should be able to enter the name of the item and the price.
# your function should add the name of the item to the list of items
# you will also need to write code that will add all the prices of the items
# including the price of the new item.

# keywords:

#clues: append() function, we need strings, 

# starter code
list__of_items=['apple', 'organe','book']

apple_price= 1.00
orange_price=3.00
book_price=10.00


def cart_items():
    newitem_name= input('enter name of new item')
    newitem_price= float(input)('please enter price of item')
    list__of_items.append(newitem_name)
    total_price= apple_price + orange_price + book_price + newitem_price

    print('here is all of your items : ')
    print(list__of_items)
    print("total price below:")
    print(total_price)   

    cart_items()


