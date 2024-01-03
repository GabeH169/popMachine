# @Gabriel Haro-Villa
# This program proccess bank account checks and prevents a negative balance.

#Get account balance from the user
balance = float(input("Please enter a balance: $"))
print()
checkAmount = 1

# While loop calculates the balance from checks enter from user
while checkAmount > 0 :
    checkAmount = float(input("Check amount (0 or negative to end): $"))
    # This if statement subtracts the checkAmount from balance
    if checkAmount < balance and checkAmount > 0 :
        balance = balance - checkAmount
        print(f"Current balance: ${balance:,.2f}")
        print()
    # This elif statement prevents the balance from going negative
    elif checkAmount > balance :
        print("Warning: Check will bounce. No transaction occurred.")
        print()
        # This elif statement will terminate if the checkAmount = balance
    elif checkAmount == balance :
        balance = balance - checkAmount
        print(f"Current balance: ${balance:,.2f}")
        break

# Prints the final balance
print()
print(f"Final balance: ${balance:,.2f}")