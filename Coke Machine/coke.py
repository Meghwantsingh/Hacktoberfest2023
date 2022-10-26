amount_due = 50
print("Amount Due: 50")
while amount_due !=0:
    coin = int(input("Insert Coin: "))
    if coin == 25:
        amount_due = amount_due - 25
        if amount_due < 0:
            print("Change Owed: ",abs(amount_due))
            break
        elif amount_due == 0:
            print("Chnage Owed: 0")
            break
        else:
            print("Amount Due:",amount_due)
    elif coin == 10:
        amount_due = amount_due - 10
        if amount_due < 0:
            print("Change Owed: ",abs(amount_due))
            break
        elif amount_due == 0:
            print("Chnage Owed: 0")
            break
        else:
            print("Amount Due:",amount_due)
    elif coin == 5:
        amount_due = amount_due - 5
        if amount_due < 0:
            print("Change Owed: ", abs(amount_due))
            break
        elif amount_due == 0:
            print("Chnage Owed: 0")
            break
        else:
            print("Amount Due:",amount_due)
    else:
        print("Amount Due:",amount_due)
