from productManage import ProductManage
from owner import Owner
from customer import Customer
from colorama import Fore, Style

print(Style.BRIGHT+'\n\t-----------O   🛍️  WELCOME TO SUPER MARKET 🛍️   O-----------\n'+Style.RESET_ALL)
ch = 0
while (ch != '4'):

    print(Fore.LIGHTMAGENTA_EX+'''🔘 Select Choice Given Below :\n 
                        1️⃣  Log In as Ownerr̥
                        2️⃣  Log In as Customer
                        3️⃣  Sign In as Customer
                        4️⃣  Exit''')
    print('\n-------------------------------------------------------------------------')
    ch = input(Fore.WHITE+'Enter Choice : '+Style.RESET_ALL)
    
    if ch == '1':
        Owner.ownerLogin()
    elif ch == '2':
        Customer.customerLogin()
    elif ch == '3':
        Customer.customerRegistration()
    elif ch == '4':
        print(Fore.LIGHTBLUE_EX+Style.BRIGHT+'\n------------ 🚪 Thank You for Choosing us! ------------'+Style.RESET_ALL)
        print('________________________________________________________________________')
    else:
        print(Fore.LIGHTRED_EX+'❌ Invalid Choice, Try again!'+Style.RESET_ALL)
         