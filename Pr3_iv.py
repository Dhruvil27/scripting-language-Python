def change():
    amnt = float(input("Enter an amount in USD: "))
    quarters = divmod(amnt, 0.25)
    print("Quarters: ", quarters[0])
    amnt = round(quarters[1], 2)
    dimes = divmod(amnt, 0.10)
    print("Dimes: ", dimes[0])
    amnt = round(dimes[1], 2)
    nickels = divmod(amnt, 0.05)
    print("Nickels: ", nickels[0])
    amnt = round(nickels[1], 2)
    penny = divmod(amnt, 0.01)
    print("Pennies", penny[0])
change()