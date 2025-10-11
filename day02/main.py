print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
# here, I calculated the amount per person first, then added a tip to each
# amt_per = round((bill / people) * (1 + tip/100),2)
# alternative way - calculate total bill with tip, then split it
total_with_tip = bill * tip/100 + bill
amt_per = round(total_with_tip / people,2)
print(f"Each person should pay: {amt_per}")


