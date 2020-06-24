"""
    ATM (Automatic Teller Machine)
"""

restart = ('Y', 'y', 'YES', 'yes')
balance = 5000
for chances in range(0, 4):
    try:
        print("**---------------Welcome To Python Bank ATM-------------------**")
        PIN = int(input("Enter your Four digit PIN:"))
        PINS = (1234, 2345, 3435, 3423)
        if PIN in PINS:
            while restart not in ('n', 'NO', 'no', 'N'):
                print("Press 1.Withdrawal")
                print("Press 2.MINI Statement")
                print("Press 3.Balance Enquiry")
                print("Press 4.Pin Generation")
                print("Press 5.Return Card")
             # Next step control returns here the control
                try:
                    e = int(input('Enter transactions option type(1,2,3,4,5):'))
                    if e == 1:
                        q = int(input("Enter withdrawal Amount in [100, 200, 500, 1000, 2000]:"))
                        if q in range(100, 10000, 100):
                            print('Withdrawing Amount :', q)
                            balance -= q
                            print('Available Balance :', balance)
                            print("Collect Your Cash!!")
                        elif q == balance:
                            print('Insufficient Balance!!')
                        else:
                            print('Invalid Amount!!')
                        restart = input('Would You Like to Go Back ? :')
                        if restart in ('n', 'NO', 'no', 'N'):
                            print("**Thank You For Banking With Us**")
                            exit(0)
                        break
                    elif e == 2:
                        print("""Account No : 0000XXXXX2345 
                                    Mini Statement:
                                      10/12/2020 : 12000 Debit
                                      12/12/2020 : 10000 Credit
                                      24/12/2020 : 5000  Debit
                                      Available Balance : 5000.00
                                      Collect Your Recept!! """)
                        restart = input('Would You Like to Go Back ? :')
                        if restart in ('n', 'NO', 'no', 'N'):
                            print("**Thank You For Banking With Us**")
                            exit(0)
                        break
                    elif e == 3:
                        print("Your Current Balance :", balance)
                        restart = input('Would You Like to Go Back ? :')
                        if restart in ('n', 'NO', 'no', 'N'):
                            print("**Thank You For Banking With Us**")
                            exit(0)
                        break
                    elif e == 4:
                        new_pin = int(input("Enter New Four Numbered PIN:"))
                        print("PIN Changed Successfully!!")
                        restart = input('Would You Like to Go Back ? :')
                        if restart in ('n', 'NO', 'no', 'N'):
                            print("**Thank You For Banking With Us**")
                            exit(0)
                        break
                    elif e == 5:
                        print("Collect Your Card")
                        restart = input('Would You Like to Go Back ? :')
                        if restart in ('n', 'NO', 'no', 'N'):
                            print("**Thank You For Banking With Us**")
                            exit(0)
                        break
                except ValueError:
                        print("Entered Invalid Option !!\n Try Again")
                        restart = input('Would You Like to Go Back ? :')
                        if restart in ('n', 'NO', 'no', 'N'):
                            print("**Thank You For Banking With Us**")
                            exit(0)
                        break
            if restart not in ('N', 'n', 'y', 'Y', 'yes', 'NO', 'no', 'YES'):
                print("Invalid Key Entered!")
                print("**Thank You For Banking With Us**")
                exit(0)
        elif PIN != PINS:
            print("Entered Incorrect PIN Number !!")
            chances += 1
            restart = ('y')
            if chances == 3:
                print('Your card is Blocked!!\nIt is Valid After 24Hrs')
                print("**Thank You For Banking With Us**")
                exit(0)
    except ValueError:
        print("Your Card is Blocked!!\nIt is valid After 24 Hrs")
    if chances == 3:
        print("Your Daily Card Access Limit Reached!!\nIt is valid after 24 Hrs")
        print("**Thank You For Banking With Us**")

    elif PIN in (4321, 5432, 5343, 3243):
        print("Your Card is Blocked!!\nIt is valid After 24 Hrs")
        print("**Thank You For Banking With Us**")
        exit(0)
