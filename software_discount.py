Software_unit_cost= 99
Unit= int(input("Enter a unit: "))
if(Unit>=100):
    print("50%")
if(Unit<=99):
    print("40%")
if(Unit>=50):
    print("40%")
if(Unit<=49):
    print('30%')
if(Unit>=20):
    print("30%")
if(Unit<=19):
    print("20%")
if(Unit>=10):
    print("20%")
if(Unit<=9):
    print("No discount")
Original_cost=(Software_unit_cost*Unit)
Discount_amount= (Original_cost*discount_rate)
Final_cost = Original_cost-Discount_amount

