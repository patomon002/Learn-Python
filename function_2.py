def money(current_balance, spend): #current_balance and spend are called parameters
    if current_balance > spend:
        balance = current_balance - spend
        print(f"your balance is {balance}")    #OR print("your balance is ", balance)
    else:
        print("your current balance is below the amount your can spend")
money(80, 20)
money(70, 50)
money(60, 90)


