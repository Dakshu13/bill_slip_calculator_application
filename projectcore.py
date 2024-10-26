#The aim of the application to provide the accurate share among the peers
#The application can also be used for other purposes which includes hotel bill split
# Provide a statement to welcome the viewers on this application
print("Welcome to split bill among peers applications!")
# Ask the user to provide the total bill
initial_bill = int(input("Enter the value of the initial bill:\n"))
# Now ask the user to provide the value of tip, which is 10,12 or 15
tip_bill = int(input("Enter the value of the tip bill:\n"))
# Storing the sum of initial_bill and tip_bill into total_bill
total_bill = initial_bill + tip_bill
#Print out the value of the total_bill
print(f"The total bill is ${total_bill}.")
# Now, ask the user about the number of people to split the total bill
split_people = int(input("Enter the number of people to split the bill:\n"))
# Split the bill by dividing it by total_bill and round to 2 decimals
split_bill = total_bill/split_people
print(f"The split is: ${round(split_bill,3)}")
