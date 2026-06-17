## Input we need from the user
#Total rent
#Total food ordered for snacking 
#Electricity units spend
#charge per unit
#Person living in room/flat

##output
#Total amount you've to pay is 


rent = int(input("Enter your hostel/flat rent = "))
food = int(input("Enter the amount of food order = "))
electricity = int(input("Enter the total of electricity spend = "))
charge_per_unit = int(input("Enter the charger per unit = "))
persons = int(input("Enter the number of person living in a room/flat  = "))

total_bill = electricity_spend * charge_per_unit

output = (food + rent + total_bill) // persons

print("Enter person will pay = ",output)

