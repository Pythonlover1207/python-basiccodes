#code for Smart Store Combo Calculator
#dict
items = {
    "pen" : 10,
    "notebook" : 40,
    "bottle" : 80,
    "bag" : 120,

}
#user input1
item1 = input("Plz Enter Your First Item Name : ")
num1 = int(input("Enter the quntity :  "))
#user input2
item2 = input("Plz Enter Your Second Item Name : ")
num2 = int(input("Enter the quntity : "))
#condition for item validation
if(item1 not in items or item2 not in items):
    print("Your given item are not in the list. Plz Check the items.")
else:
    price1 = items.get(item1)
    price2 = items.get(item2)
 #Calculation of Total
    Total = (price1*num1) + (price2*num2)
#Discounts_calculation
    discount_25 = Total*0.25
    discount_10 = Total*0.1
#Condition for discount
    if(Total>200):
        print("Congratulations! You Got a Discount of : Rupee ",discount_25)
        print("Your Grand Total is (including discount) : Rupee ",Total-discount_25 )
    elif(num1 or num2 == 5):
        print("Congratulations! You Got a Discount of : Rupee",discount_10)
        print("Your Grand Total is (including discount) : Ruppe", Total-discount_10)
    elif(num1 and num2 <5):
        print("Your Grand Total is : Rupee", Total)

#End of the Code 
