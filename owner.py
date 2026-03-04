from productManage import ProductManage
from colorama import Fore,Style, Back
import getpass
# import os

# def clearscreen():
#     os.system('cls' if os.name =='nt' else 'clear')

class Owner:
    def ownerLogin():
        print('=========================================================================')
        print(Style.BRIGHT+Fore.CYAN+'\t\t\t📝 OWNER LOGIN '+Style.RESET_ALL)
        print('=========================================================================')
        id = 'owner'
        passw = '12345' 
        while True: 
            owner_id = input(Fore.WHITE+'🆔 Enter Owner User Name : '+Style.RESET_ALL)
            owner_pass = getpass.getpass(Fore.WHITE+'🔒 Enter Owner Password : '+Style.RESET_ALL)
            # print('\n---------------------------------------------------------')
            if owner_id == id and owner_pass == passw:
                print(Fore.LIGHTGREEN_EX+'\n\t\t✅ Login Successfully.'+Style.RESET_ALL)
                print('-------------------------------------------------------------------------')
                ch = 0
                while ch != '6':
                    # clearscreen()
                    print(Style.BRIGHT+Fore.YELLOW+'''🔘 SELECT CHOICE FROM BELOW :
                        1️⃣  Add Product
                        2️⃣  Upadate Product
                        3️⃣  Delete Product
                        4️⃣  View Product
                        5️⃣  View Order 
                        6️⃣  Exit'''+Style.RESET_ALL)
                    ch = input(Fore.WHITE+'👉 Enter Choice : '+Style.RESET_ALL)
                    if ch == '1':
                        ProductManage.addProduct()
                    elif ch == '2':
                        ProductManage.updateProduct()
                    elif ch == '3':
                        ProductManage.deleteProduct()
                    elif ch == '4':
                        ProductManage.viewProduct()
                    elif ch == '5':
                        ProductManage.viewOrder()
                    elif ch == '6':
                        print(Fore.LIGHTBLUE_EX+'🚪 Thank You!'+Style.RESET_ALL)
                        return
                    else:
                        print(Fore.LIGHTRED_EX+'❌ Invalid Choice...'+Style.RESET_ALL)
            else:
                print(Fore.RED+'\n\t\t❌ Invalid Creadential...'+Style.RESET_ALL)
                print('-------------------------------------------------------------------------')