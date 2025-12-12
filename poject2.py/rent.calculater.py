# # inputs we nee from the user
# # total rent 
# # total food ordered for snacking
# # Electricity unit spend
# # charge per uint 
# # person living in room/

# # output
# # tolal amount you've to pay is 
 

# rent = int(input("Enter your hostel/room rent = "))
# foods = int(input("Enter the amount of food ordered for snacking = "))
# electricity_spend = int(input("Enter the total of electricity spend units = "))
# charge_per_unit = int(input("Enter the charge per unit = "))

# person = int(input("Enter the number of person living in room/flat = "))


# total_bill = electricity_spend * charge_per_unit 

# output = (rent + foods + total_bill) // person

# # print(f"Each per person pay bill : {output} ")

# Rent Calculator
rent = int(input("Enter your hostel/room rent = "))
foods = int(input("Enter the amount of food ordered for snacking = "))
electricity_spend = int(input("Enter the total of electricity spend units = "))
charge_per_unit = int(input("Enter the charge per unit = "))
person = int(input("Enter the number of person living in room/flat = "))

total_bill = electricity_spend * charge_per_unit 
output = (rent + foods + total_bill) / person  # Use / instead of // for accurate division

print(f"Each person pay bill: {output:.2f}")  # Fixed typo and added decimal formatting
