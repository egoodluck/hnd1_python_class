from get_top import get_order as go

abacha_toppings = []
while True:
    topping = input('Enter the topping you may want for your Abacha \nEnter "quit" to exit: ')
    if topping == 'quit':
        break
    else:
        abacha_toppings.append(topping)
print('\nYour Abacha is ready with the following toppings ')
go(abacha_toppings)
