items=0
price=0

items=int(input("How many items are you purchasing? "))
while items>0:
    itemNum=input("Item name: ")
    price+=float(input("How much is the item? "))
    items-=1
    if items==0:
        print("\nYour total is: %.2f" % price + "$")
        #price2 = format(price.".2f")
        discount10= price-(price*.10)
        discount20= price-(price*.20)
        if price>=100 and price<200:
             print("You have a 10%","discount!")
             print("Your final total is %.2f" % discount10 + "$")
        elif price >=200:
            print("You have a 20%","discount!")
            print("Your final total is %.2f" % discount20 + "$")
        else:
            print ("Your total final total is: %.2f" % price + "$")
        break
