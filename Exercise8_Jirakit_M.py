usernameInput = input("Username : ")
passwordInput = input("Password : ")
if usernameInput == "kitmimi" and passwordInput == "5555" :
    print("-----KITMIMI SHOP-----")
    print("1.Chocolate ring    price : 22 THB")
    print("2.Choc peanut   price : 20 THB")
    print("3.Honey dipped  price : 22 THB")
    userSelected = int(input("เลือกสินค้าตามหมายเลขด้านบน"))
    if userSelected == 1:
        name = "Chocolate ring"
        number= int(input("Chocolate ring  ราคา 22 THB จำนวน : ",))
        amount= number * 22
        print("Total :",name,"จำนวน",number, "ิ้น","ราคา",amount,"THB")
    elif userSelected == 2:
        name = "Choc peanut"
        number = int(input("Choc peanut  ราคา 20 THB จำนวนชิ้น : "))
        amount = number * 20
        print("Total :",name,"จำนวน",number,"ชิ้น","ราคา",amount,"THB")
    elif userSelected == 3:
        name = "Honey dipped"
        number = int(input("Honey dipped   ราคา 22 THB จำนวนชิ้น : "))
        amount = number * 22
        print("Total :",name,"จำนวน",number,"ชิ้น","ราคา",amount, "THB")
    print("----------------------")
    print("Thank you : KITMIMI Shop")
else :
    print("! Wrong Username or Password !")
