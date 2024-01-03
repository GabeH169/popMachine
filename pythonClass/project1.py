# @Gabriel Haro-Villa
# This program simulates a mini ATM.

def main() :
    balance = 1500
    choice = ""
    while choice != 'E':
        choice = getMenuChoice()
        if choice == 'W' :
            balance = processWithdrawl(balance)
        elif choice == 'D' :
            balance = processDeposit(balance)
        elif choice == 'B' :
            print(f"Current balance: ${balance:,.2f}")
        print()
    print("Thank you for banking with us.")

# getMenuChoice presents a banking menu of choices
# @return The customer's menu choice as a single upper
# case letter.
def getMenuChoice() :
    print("====================")
    print("Enter W for Withdraw")
    print("Enter D for Deposit")
    print("Enter B for Balance")
    print("Enter E for Exit")
    print("====================")
    userChoice = input("Choice: ").upper()
    return userChoice

# processWithdrawal processes a customer's withdrawal
# @param balance The current balance
# @return The updated balance
def processWithdrawl(balance) :
    withdrawlAmt = float(input("Enter withdrawl amount: $"))
    if withdrawlAmt <= 0:
        print("Improper withdraw amount entered.")
    elif withdrawlAmt > balance :
        print("Insufficient funds.")
    else:
        balance = balance - withdrawlAmt
        print(f"Please take your ${withdrawlAmt:,.2f}")
    return balance

# processDeposit processes a customer's deposit
# @param balance The current balance
# @return The updated balance
def processDeposit(balance) :
    depositAmt = float(input("Enter deposit amount: $"))
    if depositAmt <= 0 :
        print("Improper deposit amount entered.")
    else:
        balance = balance + depositAmt
        print(f"${depositAmt:,.2f} deposited.")
    return balance

main()