def currency_converter():
    try:
        dollar = float(input("Enter the dollar amount: "))
        rate = float(input("Enter the conversion rate: "))
        INR = dollar*rate
        print(INR)
    except ValueError:
        print ("Enter only Numbers")
        currency_converter()
currency_converter()

def password_check(password=''):
    while password != 'sudheer':
        password = input("Enter Password: ")
        if password == 'sudheer':
            print("Log in success")
        else:
            print("Sorry Try Again")
password_check()
