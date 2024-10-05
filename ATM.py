def main():
    name = input('Enter Your name: ')
    print(f'\n******Thank you (Mr/Mrs) {name },...WELCOME TO OUR ATM MACHINE******\nPlease Insert the card....\n')
    insert = input('Enter INSERT to insert the card:\n   ')
    insert1 = 'INSERT'
    pin1 = 6137
    amount = 75000
    if insert == insert1 :
        print('\nCard Inserted successfully!\n')
        option = int(input('Choose your type of transaction:\n    1)check balance    2)withdraw\n    3)Add cash    4)EXIT\nEnter your type of transaction: '))
        if option == 1:
            pin = int(input('Enter Your 4 digit pin: '))
            if pin == pin1:
                print('Balance available in your AC: ',amount)
            else:
                print('<<<Incorrect pin!') 
        elif option == 2:
            pin = int(input('Enter Your 4 digit pin: '))
            if pin == pin1:
                withdraw = int(input('Enter Amount: '))
                if withdraw >= amount:
                    print('Insufficent Funds!')
                else:
                    print(f'Withdraw of {withdraw} is successful')
                    print('Available balance in your Ac is: ',(amount-withdraw))
            else:
                print('<<<Incorrect pin')
        elif option == 3:
            pin = int(input('Enter Your 4 digit pin: '))
            if pin == pin1:
                cash = int(input('Enter Amount: '))
                total = amount + cash
                print('Total Amount in your Ac: ',total)
            else:
                print('<<<Incorrect pin')    
        elif option == 4:
            print('****THANKYOU FOR USING OUR ATM >>>****')
        else:
            print('<<<Invalid input')
    else:
        print('<<Invalid!')
print(main())
        
if __name__ == "main":
    main()