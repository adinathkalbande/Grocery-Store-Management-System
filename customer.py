from productManage import ProductManage
from colorama import Fore,Style, Back
import getpass
import random
import hashlib


class Customer:
    def customerLogin():
        print('=========================================================================')
        print(Fore.LIGHTCYAN_EX+Style.BRIGHT+'\t\t\t📝 CUSTOMER LOGIN '+Style.RESET_ALL)
        print('=========================================================================')
        while True:
            cust_id = input(Fore.WHITE+'🆔 Enter Customer ID : '+Style.RESET_ALL)
            cust_pass = getpass.getpass('🔒 Enter Customer Password : '+Style.RESET_ALL)
            hashed_pass = hashlib.sha256(cust_pass.encode()).hexdigest()
            try:
                captchCode = random.randint(11111, 99999)
                print(Fore.YELLOW+f'👉 Your Captcha is Ready : {captchCode}'+Style.RESET_ALL)
                Captcha = int(input(Fore.WHITE+'🔢 Enter Captcha : '+Style.RESET_ALL))
            except ValueError:
                print(Fore.RED+'❌ Invalid Captcha...'+Style.RESET_ALL)
                print('-------------------------------------------------------------------------')
                continue
        
            with open('Data/customer.txt', 'r') as fp:
                for line in fp:
                    eData = line.strip()
                    eList = eData.split(', ')
                    # print(eList)
                    if cust_id == eList[0] and hashed_pass == eList[1] and captchCode == Captcha:
                        print('-------------------------------------------------------------------------')
                        print(Fore.GREEN+'\t\t\t✅ Login Successfully.'+Style.RESET_ALL)
                        print('-------------------------------------------------------------------------')

                        print(Fore.CYAN+Style.BRIGHT+'\n---------------O 🙏 WELCOME TO SUPERMARKET 🙏 O----------------\n'+Style.RESET_ALL)
                        
                        ch = 0
                        while(ch != '8'):
                            print(Fore.LIGHTYELLOW_EX+Style.BRIGHT+'''🔘 SELECT FROM BELOW :
                                1️⃣. View Product
                                2️⃣. Search Product
                                3️⃣. Add Product to cart
                                4️⃣. View Cart
                                5️⃣. Buy Product
                                6️⃣. Delete Cart Product
                                7️⃣. Generate Bill
                                8️⃣. Exit'''+Style.RESET_ALL)
                            ch = input(Fore.WHITE+'👉 Enter Choice : '+Style.RESET_ALL)
                            if ch == '1':
                                ProductManage.viewProduct()
                            elif ch == '2':
                                ProductManage.searchProduct()
                            elif ch == '3':
                                ProductManage.addProductToCart(cust_id)
                            elif ch == '4':
                                ProductManage.showCartproduct(cust_id)
                            elif ch == '5':
                                ProductManage.buyProduct(cust_id)
                            elif ch == '6':
                                ProductManage.deleteCart(cust_id)
                            elif ch == '7':
                                ProductManage.generateBill(cust_id)
                            elif ch == '8':
                                print(Fore.LIGHTBLUE_EX+'\t\t\t🚪 Thank You For Choosing Us!'+Style.RESET_ALL)
                                print('-------------------------------------------------------------------------')
                                return
                            else:
                                print(Fore.LIGHTRED_EX+'❌ Invalid Choice!'+Style.RESET_ALL) 
                        return
            
                print(Fore.LIGHTRED_EX+'❌ Invalid Creadential...'+Style.RESET_ALL)
                print('-------------------------------------------------------------------------')
        

    def customerRegistration():
        print('=========================================================================')
        print(Style.BRIGHT+Fore.LIGHTCYAN_EX+'\t\t\t📝 REGISTRATION '+Style.RESET_ALL)
        print('=========================================================================')
        
        # try:
        userName = input(Fore.WHITE+'👤 Enter Your Name : '+Style.RESET_ALL).strip()
        firstName = userName.split()[0]
        rand_num = random.randint(111, 999)
        userId = f'{firstName}@{rand_num}'.lower()
        while True:
            userPass = input(Fore.WHITE+'🔒 Enter Password : '+Style.RESET_ALL)
            if len(userPass) == 6 and userPass.isalnum() and not userPass.isalpha() and not userPass.isdigit():
                break
            else:
                print(Fore.YELLOW+'⚠️ Password should be some alphabets and digit.'+Style.RESET_ALL)
        encrypt_pass = hashlib.sha256(userPass.encode()).hexdigest()
        while True:
            mobilNo = input(Fore.WHITE+'📞 Enter Your Mobile Number : '+Style.RESET_ALL)
            if len(mobilNo) == 10 and mobilNo.isdigit():
                break
            else:
                print(Fore.YELLOW+'⚠️ Please Entered valid Mobile Number.'+Style.RESET_ALL)
                
        address = input(Fore.WHITE+'🏡 Enter Your Address : '+Style.RESET_ALL)
        with open('Data/customer.txt', 'a') as fp:
            fp.write(f'\n{userId}, {encrypt_pass}, {userName}, {mobilNo}, {address}')
            print('-------------------------------------------------------------------------')
            print(Fore.LIGHTGREEN_EX+'🎉 Registration Succefully.')
            print('👤 Your User Name is : ', userId)
            print(Fore.WHITE+'-------------------------------------------------------------------------'+Style.RESET_ALL)