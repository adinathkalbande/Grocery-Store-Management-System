from colorama import Fore, Style, Back
from prettytable import PrettyTable
from datetime import datetime
import random
from stapleProduct import StapleProduct
from dailyProduct import DailyProduct
from foodProduct import FoodProduct

#---------------------- Add Product -------------------------
class ProductManage:    
    def addProduct():
        while True:
            print('-------------------------------------------------------------------------')
            pid = input(Fore.WHITE+'🆔 Enter Product Id : ')
            found = False
            try:
                with open('Data/product.txt', 'r') as fp:
                    for line in fp:
                        eList = line.strip().split(', ')
                        if eList[0] == pid:
                            found = True
                            break
            except FileNotFoundError:
                print(Fore.LIGHTRED_EX+'🙁 File does not found!'+Style.RESET_ALL)
            if found:
                print(Fore.YELLOW+'✅ Product Id is allready available.'+Style.RESET_ALL)
                continue
            
            is_dailyProduct = False
            is_foodProduct = False
            is_stapleProduct = False
            while True:           
                print(Fore.LIGHTYELLOW_EX+'''🔘 Select Category from below : 
                        1️⃣. Daily Product
                        2️⃣. Food Product
                        3️⃣. Staple Product'''+Style.RESET_ALL)
                ch = input(Fore.WHITE+'👉 Enter choice :'+Style.RESET_ALL)

                if ch == '1':
                    category = 'Daily Product'
                    is_dailyProduct = True
                    break
                elif ch == '2':
                    category = 'Food Product'
                    is_foodProduct = True
                    break
                elif ch == '3':
                    category = 'Staple Product'
                    is_stapleProduct = True
                
                    break
                else:
                    print(Fore.LIGHTRED_EX+'❌ Invalid Choice, please try again...'+Style.RESET_ALL)
                    
            pnm = input('📦 | Enter Product Name : ')
            pbrand = input('🏷️ | Enter Product Brand : ')
            while True:
                try:
                    pquantity = int(input('#️⃣ | Enter Product Qauntity : '))
                    break
                except:
                    print(Fore.LIGHTRED_EX+'❌ Something else wrong...'+Style.RESET_ALL)
    
            unit = input('⚖️ | Enter Unit of Product (kg/gram/packets): ')

            while True: 
                try:           
                    price = int(input('💰 | Enter Price of Product : '))
                    break
                except:
                    print(Fore.LIGHTRED_EX+'❌ Something else wrong...'+Style.RESET_ALL)

                                
            if is_dailyProduct:
                obj = DailyProduct(pid, pnm, category, pquantity, unit, price)
                total_with_gst= round(obj.calculateGst(), 2)
                    
            elif is_foodProduct:
                obj = FoodProduct(pid, pnm, category, pquantity, unit, price)
                total_with_gst= round(obj.calculateGst(), 2)

            elif is_stapleProduct:
                obj = StapleProduct(pid, pnm, category, pquantity, unit, price)
                total_with_gst= round(obj.calculateGst(), 2)
            else:
                total_with_gst = price
            eData = f'{pid}, {category}, {pnm}, {pbrand}, {pquantity}, {unit}, {price}, {total_with_gst}'

            with open('Data/product.txt', 'a') as fp:
                fp.write(eData+'\n')
            print(Fore.GREEN+Style.BRIGHT+"✅ Product Added Successfully!"+Style.RESET_ALL)
            print('-------------------------------------------------------------------------')
            
            choice = input(Fore.YELLOW+'🟢 Enter You want to another product (yes/no): '+Style.RESET_ALL).lower()
            if choice != 'yes':
                break
            print('-------------------------------------------------------------------------')
    #---------------------- Update Product -------------------------
    def updateProduct():
        print('-------------------------------------------------------------------------')
        id = input(Fore.WHITE+'🆔 Enter Product Id you want to Update : '+Style.RESET_ALL)
        found = False
        updateLists = []
        with open('Data/product.txt', 'r') as fp:
            for line in fp:
                eData = line.strip()
                eList = eData.split(', ')
                if id == eList[0]:
                    print(Fore.GREEN+f'✔️  Product Id Is Found '+Style.RESET_ALL)
                    found = True



                    gst_update = False

                    choice = input(Fore.LIGHTCYAN_EX+'🔄 You Want to Change Category(Yes/No) : '+Style.RESET_ALL).lower()
                    if choice == 'yes':
                        while True:
                            print('''Select From Below : 
                                1. Daily Products
                                2. Food Products
                                3. Staple Products''')
                            ch = input('🛍️  Enter Category of Product : ')
                            if ch == '1':
                                eList[1] = 'Daily Products'
                                gst_update = True
                                
                                break
                            elif ch == '2':
                                eList[1] = 'Food Products'
                                gst_update = True
                                
                                break
                            elif ch == '3':
                                eList[1] = 'Staple Products'
                                gst_update = True
                                
                                break
                            else:
                                print('Invalid Choice...')
                    choice1 = input(Fore.LIGHTCYAN_EX+'🔄 You want to change name(Yes/No) : '+Style.RESET_ALL).lower()
                    if choice1 == 'yes':
                        eList[2] = input('📦 Enter New Name : ')
                    choice3 = input(Fore.LIGHTCYAN_EX+'🔄 You want to change Brand : '+Style.RESET_ALL).lower()
                    if choice3 == 'yes':
                        eList[3] = input('🏷️ Enter Brand Name : ')
                    choice4 = input(Fore.LIGHTCYAN_EX+'🔄 You want to change Quantity(Yes/No) : '+Style.RESET_ALL).lower()
                    if choice4 == 'yes':
                        while True: 
                            try:   
                                eList[4] = int(input('#️⃣ Enter Quantity : '))
                                break
                            except ValueError:
                                print(Fore.LIGHTRED_EX+'❌ Something Wrong Else, please try again...'+Style.RESET_ALL)
                    choice5 = input(Fore.LIGHTCYAN_EX+'🔄 You want to change unit of product(Yes/No) : '+Style.RESET_ALL)
                    if choice5 == 'yes':
                        eList[5] = input('⚖️ Enter Unit of Product(pac/kg/lit) : ')
                    choice6 = input(Fore.LIGHTCYAN_EX+'🔄 You want to change price of product(Yes/No) : '+Style.RESET_ALL).lower()
                    if choice6 == 'yes':
                        while True:
                            try:    
                                eList[6] = int(input('💰 Enter Price : '))
                                break
                            except ValueError:
                                print(Fore.LIGHTRED_EX+'❌ Something Wrong Else, please try again...'+Style.RESET_ALL)
                    
                    if gst_update:
                        category = eList[1]
                        qty = int(eList[4])
                        price = int(eList[6])

                        if eList[1] == 'Daily Products':
                            obj = DailyProduct(id, category, eList[2], eList[3], qty, price)
                            
                                
                        elif eList[1] == 'Food Products':
                            obj = FoodProduct(id, category, eList[2], eList[3], qty, price)
                            

                        elif eList[1] == 'Staple Products':
                            obj = StapleProduct(id, category, eList[2], eList[3], qty, price)
                            
                        eList[7]= obj.calculateGst()

                    updateList = ", ".join(map(str,eList))+'\n'
                    updateLists.append(updateList)
                else:
                    updateLists.append(line)
        if found:
            with open('Data/product.txt', 'w') as fp:
                fp.write(''.join(updateLists))
                print(Fore.LIGHTGREEN_EX+'✅ Product update successfully!'+Style.RESET_ALL)
        else:
            print(Fore.LIGHTRED_EX+'🙁 Id is not found!'+Style.RESET_ALL)
        print('-------------------------------------------------------------------------')

    
    #---------------------- Delete Product -------------------------
    def deleteProduct():
        print('-------------------------------------------------------------------------')
        id = input('🆔 Enter Id you want to delete product : ')
        found = False
        product_list = []
        
        with open('Data/product.txt', 'r') as fp:
            for line in fp:
                
                eData = line.strip().split(', ')
                if id == eData[0]:
                    found = True
                else:
                    product_list.append(line.strip())
        
        if found:
            with open('Data/product.txt', 'w') as fp:
                for item in product_list:
                    fp.write(item+'\n')
                print(Fore.GREEN+'✅ Product Delete Successfully!'+Style.RESET_ALL)
        else:
            print(Fore.LIGHTRED_EX+'🙁 Id Is Not Found...'+Style.RESET_ALL)
        print('-------------------------------------------------------------------------')

    #---------------------- View Product -------------------------
    def viewProduct():
        print('-------------------------------------------------------------------------')
        table = PrettyTable(['ID', 'CATEGORY', 'NAME', 'BRAND', 'QUANTITY', 'UNIT', 'PRICE', 'GST'])
        try:
            with open('Data/product.txt', 'r') as fp:
                for line in fp:
                    
                    eData = line.strip().split(', ')
                    while len(eData) < 8:
                        eData.append("0")  
                
                    eData = eData[:8]
                        
                    table.add_row(eData)
                print(Fore.CYAN+Style.BRIGHT+'\n\t\t\t👇 ALL PRODUCT LIST 👇\n'+Style.RESET_ALL)
                print(f'{table}\n')
                
        except FileNotFoundError:
            print(Fore.RED+'🙁 File Does not exist'+Style.RESET_ALL)
        print('-------------------------------------------------------------------------')
    def searchProduct():
        table = PrettyTable(['ID', 'CATEGORY', 'NAME', 'BRAND', 'QUANTITY', 'UNIT', 'PRICE', 'GST'])
        print('-------------------------------------------------------------------------')
        pName = input(Fore.LIGHTYELLOW_EX+'⏎ Enter Name of Product You want to search : '+Style.RESET_ALL)
        try:
            with open('Data/product.txt', 'r') as fp:
                for line in fp:
                    eData = line.strip()
                    eList = line.split(', ')
                    
                    while len(eList) < 8:
                        eList.append("0")  
                
                    eList = eList[:8]
                    if pName.lower() == eList[2].lower() or pName.lower() == eList[1].lower():
                        table.add_row(eList)
                
                if table._rows:
                    print(Style.BRIGHT+Fore.LIGHTCYAN_EX+f'\n                 👇🏻 PRODUCT IS FOUND 👇🏻'+Style.RESET_ALL)
                    print(table)
                    print('\n-------------------------------------------------------------------------')
                else:
                    print(Fore.RED+f'-----------🙁 {pName} is not available! ------------'+Style.RESET_ALL)

        except FileNotFoundError:
            print(Fore.RED+'🙁 File Does Not Exist'+Style.RESET_ALL)

    #---------------------- Add to cart -------------------------
    def addProductToCart(current_user):
        print('-------------------------------------------------------------------------')
        cart_file = f'Data/Cart/cart_{current_user}.txt'    
        while True:
            p_id = input(Fore.LIGHTYELLOW_EX+'⏎ Enter Product Id you want to add : ')
            try:
                p_quantity = int(input('#️⃣  Enter Quantity of Product : '+Style.RESET_ALL))
                # break
            except ValueError:
                print(Fore.LIGHTRED_EX+'❌ Something Else Wrong, please try again...'+Style.RESET_ALL)
                continue
            found = False
            try:
                with open('Data/product.txt', 'r') as fp: 
                    file = fp.readlines() #Read all lines from list
            except:
                print(Fore.LIGHTRED_EX+'🙁 File not found!'+Style.RESET_ALL)
                return
            

            for i in range(len(file)):
                eList = file[i].strip().split(', ')
                if eList[0] == p_id:
                    found = True
                    avai_quan = int(eList[4])
                    price = int(eList[6])
                    gst = float(eList[7])

                    if p_quantity <= avai_quan:
                        gst_price = price + gst
                        gst_all_price = p_quantity*gst             
                        total = gst_price * p_quantity
                        new_quan = avai_quan-p_quantity

                        with open(cart_file, 'a') as fp:
                            fp.write(f'{p_id}, {eList[1]}, {eList[2]}, {eList[3]}, {p_quantity}, {eList[5]}, {price}, {gst_all_price}, {total}\n')
                            print(Fore.LIGHTGREEN_EX+'✅ Product added successfully!'+Style.RESET_ALL)
                            print('-------------------------------------------------------------------------')
                        file[i] = f'{p_id}, {eList[1]}, {eList[2]}, {eList[3]}, {new_quan}, {eList[5]}, {price}, {gst}\n'
                        
                    else:
                        print(Fore.LIGHTRED_EX+'\t\t\t🚫 Stock Not available!'+Style.RESET_ALL)
                        print('-------------------------------------------------------------------------')
                    break
            if not found:
                print(Fore.LIGHTRED_EX+'🙁 Product not found'+Style.RESET_ALL)
                print('-------------------------------------------------------------------------')

            with open('Data/product.txt', 'w') as fp:
                fp.writelines(file)
            
            choice = input(Fore.LIGHTYELLOW_EX+'🟢 You want to add another product(Yes/No) = '+Style.RESET_ALL).lower()
            if choice != 'yes':
                break
            print('-------------------------------------------------------------------------')
    def deleteCart(current_user):
        print('-------------------------------------------------------------------------')
        cart_file = f'Data/Cart/cart_{current_user}.txt' 
        id = input('🆔 Enter Id you want to delete product : ')
        found = False
        product_list = []

        with open(cart_file, 'r') as fp:
            for line in fp:
                # print('Id is found :', eData)
                eData = line.strip().split(', ')
                if id == eData[0]:
                    found = True
                else:
                    product_list.append(line.strip())
        if found:
            with open(cart_file, 'w') as fp:
                for item in product_list:
                    fp.write(item+'\n')
                print(Fore.GREEN+'✅ Product Delete Successfully!'+Style.RESET_ALL)
        else:
            print(Fore.LIGHTRED_EX+'🙁 Id is not found...'+Style.RESET_ALL)
        print('-------------------------------------------------------------------------')

    #---------------------- Show cart Product -------------------------
    def showCartproduct(current_user):
        print('-------------------------------------------------------------------------')
        cart_file = f'Data/Cart/cart_{current_user}.txt'
        # print('=============================')
        
        # print('=============================')
        table = PrettyTable(['ID', 'CATEGORY', 'NAME', 'BRAND', 'QUANTITY', 'UNIT', 'PRICE', 'GST' ,'TOTAL'])
        totalBill = 0
        try:
            with open(cart_file, 'r') as fp:
                for line in fp:
                    data = line.strip().split(', ')
                    pid, cat, pnm, brand, qua, unit, price, gst, total = data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8] 
                    # pid, cat, pnm, qua, unit, total, gst = line.strip().split(', ')
                    table.add_row([pid, cat, pnm, brand, qua, unit, price, gst, total])
                    # totalBill+=int(total)
                print(Fore.LIGHTCYAN_EX+Style.BRIGHT+'\t\t\t👇🏻🛒 Cart Item 🛒👇🏻 '+Style.RESET_ALL)
                print(table)
                
        except FileNotFoundError:
            print(Fore.LIGHTRED_EX+'\t\t\t⚪ Your Cart Is Empty'+Style.RESET_ALL)
        print('\n-------------------------------------------------------------------------')

    #---------------------- Buy Product -------------------------                
    def buyProduct(current_user):
        print('-------------------------------------------------------------------------')
        cart_file = f'Data/Cart/cart_{current_user}.txt'
        try:
            with open('Data/customer.txt', 'r') as fp:
                for record in fp:
                    if current_user in record.split(', ')[0]:   
                        customer = record.strip().split(', ')
                        break
        except FileNotFoundError:
            print(Fore.LIGHTYELLOW_EX+'🙁 File not found!'+Style.RESET_ALL)
            return

        if customer is None:
            print(Fore.LIGHTYELLOW_EX+"🙁 Customer not found!"+Style.RESET_ALL)
            return
        try: 
            with open(cart_file, 'r') as fp:
                file = fp.readlines()
        except:
                print(Fore.LIGHTRED_EX+'🛒 Your cart is empty!'+Style.RESET_ALL)
                return
        
        if not file:
            print(Fore.LIGHTRED_EX+'⚪ Your cart is empty!'+Style.RESET_ALL)
            print('-------------------------------------------------------------------------')
            return
                
        print(Fore.CYAN+Style.BRIGHT+'          👇🏻🛒 Item in your cart 🛒👇🏻\n'+Style.RESET_ALL)
        table = PrettyTable((['ID', 'CATEGORY', 'NAME', 'QUANTITY', 'UNIT', 'PRICE', 'GST', 'TOTAL']))
        total_bill = 0
        total_gst = 0
        total_billGst = 0
        # gst_rate = 0.18

        for line in file:
            edata = line.strip().split(', ') 
            pid, cat, name, quan, unit, price, gst, total  = edata[0], edata[1], edata[2], edata[4], edata[5], edata[6], edata[7], edata[8]
            table.add_row([pid, cat, name, quan, unit, price, gst, total])
            total_bill += float(total)
            total_gst += float(gst)
            
            # total_billGst = total_bill+total_gst+total

        print(table)
        print(Fore.CYAN+f'Total Bill With GST   : {total_gst}'+Style.RESET_ALL)
        print(Fore.CYAN+f'Total Bill Amount     : {total_bill}'+Style.RESET_ALL)

        conform = input(Fore.YELLOW+'✅ Conform Your purchase(yes/no) : '+Style.RESET_ALL).lower()
        if conform == 'yes':
            while True:
                print('''🔘 Select Payment Method : 
                    1️⃣ ONLINE
                    2️⃣ CASH ON DELIVERY''')
                ch = input('👉 Enter Choice : ')
                if ch == '1':
                    payment_method = 'Online'
                    while True:
                        upi_id = input('💳 Enter UPI ID : ')
                        if '@' in upi_id:
                            break
                        else:
                            print(Fore.LIGHTRED_EX+'Invalid Upi Id, please try again...'+Style.RESET_ALL)
                    break
                elif ch == '2':
                    payment_method = 'Cash on Delivery'
                    break
                else:
                    print(Fore.LIGHTRED_EX+'❌ Invalid Choice, Please Try Again...'+Style.RESET_ALL)
                    break
            with open('tempFile.txt', 'w') as fp, open('Data/order.txt', 'a') as fp2:
                fp.write('Grocery Store Bill\n')
                for line in file:
                    data = line.strip().split(', ')
                    pid, cat, name, brand, quan, unit, price, gst, total = data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8]
                    # total_bill = total
                    fp.write(f'{pid}, {cat}, {name}, {brand}, {quan}, {unit}, {price}, {gst}, {total}, {payment_method}\n')
                    fp2.write(f'{customer[2]}, {pid}, {cat}, {name}, {brand}, {quan}, {unit}, {price}, {gst}, {total}, {payment_method}, Pending\n')
                    
            print(Fore.LIGHTGREEN_EX+'👍 Purchase successfully'+Style.RESET_ALL)
        else:
            print(Fore.YELLOW+'✋ Purchase cancelled'+Style.RESET_ALL)
        print(Fore.CYAN+'-------------------------------------------------------------------------'+Style.RESET_ALL)

    #---------------------- Bill Generate -------------------------
                    
    def generateBill(cust_id):
        customer = None
        try:
            with open('Data/customer.txt', 'r') as fp:
                for record in fp:
                    if cust_id in record:
                        customer = record.strip().split(', ')
                        break
        except FileNotFoundError:
            print(Fore.LIGHTRED_EX+'🙁 File not found')
        if customer is None:
            print("🙁 Customer not found"+Style.RESET_ALL)
            return

        try:
            with open('tempFile.txt', 'r') as fp:
                for line in fp:
                    eList = [line.strip().split(', ') for line in fp if line.strip()]
        except FileNotFoundError:
            print(Fore.LIGHTRED_EX+'🙁 File not found'+Style.RESET_ALL)
            return
        
        print('-------------------------------------------------------------------------')
        print(Fore.CYAN+Style.BRIGHT+'\t\t\t🧾 SUPER MARKET'+Style.RESET_ALL)
        print('G/456, Patil Compex\nBhosari Road, Pune 40001')
        print('-------------------------------------------------------------------------')
        print('\tDaily Offers, Daily Discounts @SuperMarket - Free Home Delivery')
        print('-------------------------------------------------------------------------')
        print('GSTIN : 26CORPP3939N1ZA \t\t\tTAX INVOICE')
        print('-------------------------------------------------------------------------')
        print(f'👤 Customer Name  : {customer[2]} \t\tInvoice Date : {datetime.now().strftime('%d-%m-%y')}')
        print(f'🏡 Address        : {customer[4]} \t\t\tInvoice No   : {random.randint(1, 1000)}' )
        print(f'📲 Mobile No      : {customer[3]} ')
        print('\n=========================================================================\n')
        table = PrettyTable(['ID', 'NAME', 'BRAND', 'QUANTITY', 'UNIT', 'PRICE', 'GST', 'TOTAL'])
        total_price = 0
        gst_rate = 0.18
        total_gst = 0
        total_amount = 0

        for item in eList:
            pid, pnm, brand, quan, unit, price, gst, total  = item[0], item[2], item[3], item[4], item[5], item[6], item[7], item[8]
            table.add_row([pid, pnm, brand, quan, unit, price, gst, total])
            # total_price += float(price)
            total_gst += float(gst)
            total_amount += float(total)
        print(table)

        print('\n=========================================================================')
        # print(f'💰 Taxable Amount           : {total_price}')
        print(f'💸 Total GST                   : {total_gst}')
        print(f'💰 Total Amount With Tax       : {total_amount}')
        print(f'💳 Payment Method              : {item[9]}\n')
        # print('\n==============================================================')
        print('🙏 Thank You For Shopping With Us!')
        print('\n\t\t\t✨ Visit again!')
        print('=========================================================================')

    def viewOrder():
        print('-------------------------------------------------------------------------')
        orders = {}
        # total = 0
        try:
            with open('Data/order.txt', 'r') as fp:
                for line in fp:
                    # eData = line.strip().split()
                    eData = [f.strip() for f in line.split(',')]
                    if len(eData) < 10:
                        continue

                    if eData[0] not in orders:
                        orders[eData[0]] = []

                    formatted = "{:<8} {:<15} {:<15} {:<10} {:<10}".format(
                        eData[1],   
                        eData[3],   
                        eData[4],   
                        eData[5],   
                        eData[9]    
                    )
                    orders[eData[0]].append(formatted)
                    
                    
        except FileNotFoundError:
            print("order.txt not found")
            return


        for cust, items in orders.items():
            print(Style.BRIGHT+Fore.LIGHTCYAN_EX+f'\n\t\tCustomer Name :  {cust}\n'+Style.RESET_ALL)
            print("{:<8} {:<15} {:<15} {:<10} {:<10}".format(
             "PID", "NAME", "BRAND", "QUANTITY", "PRICE"))
            print('-------------------------------------------------------------------------')
            for i in items:
                print(i)
            
            print('-------------------------------------------------------------------------')


        