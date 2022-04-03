#coffee.py
coffee = 10
while True:
    money = int(input("Please input money: "))
    if money == 300:
        print("Coffe is coming out!")
        coffee -= 1
    elif money > 300:
        print("Your change is %d and your coffe is coming out!"%(money-300))
        coffee -= 1
    else:
        print("You didn`t gain your coffee and your money is returned!")
        print("The remaining coffee is %d" %coffee)
    if coffee == 0:
        print("Sold out!!!!")
        break
    
