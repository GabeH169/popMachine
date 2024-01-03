##
# This program computes income taxes, using a simplified tax schedule.
# @Gabriel Haro-Villa

# Initialize constant variables for the tax rates and rate limits.
RATE1 = 0.10
rate15 = 0.15
RATE2 = 0.25
RATE1_SINGLE_LIMIT = 32000.0
RATE1_MARRIED_LIMIT = 64000.0
SINGLE_TAX_BELOW_8K = 8000
MARRIED_TAX_BELOW_16K = 16000
SINGLE_RATE = 800
MARRIED_RATE = 1600
SINGLE_TAX_OVER_32K = 4400
MARRIED_TAX_OVER_64K = 8800


# Read income and marital status
income = float(input("Please enter your income: $"))
maritalStatus = input("Please enter s for single, m for married: ")

# Compute taxes due.
tax1 = 0 # tax due at first tax bracket income level
tax2 = 0 # remaining tax due if exceeding the first bracket income

if maritalStatus == "s" or maritalStatus == "S":
    if income <= RATE1_SINGLE_LIMIT :
        if income <= SINGLE_TAX_BELOW_8K :
            tax1 = RATE1 * income
        elif SINGLE_TAX_BELOW_8K < income <= RATE1_SINGLE_LIMIT :
            tax1 = SINGLE_RATE + rate15
    else :
        tax1 = SINGLE_TAX_OVER_32K
        tax2 = RATE2 * (income - RATE1_SINGLE_LIMIT)

elif maritalStatus == "m" or maritalStatus == "M":
    if income <= RATE1_MARRIED_LIMIT :
        if income <= MARRIED_TAX_BELOW_16K :
            tax1 = RATE1 * income
        elif MARRIED_TAX_BELOW_16K < income <= RATE1_MARRIED_LIMIT :
            tax1 = MARRIED_RATE + rate15 * (income - MARRIED_TAX_BELOW_16K)
    else :
        tax1 = MARRIED_TAX_OVER_64K
        tax2 = RATE2 * (income - RATE1_MARRIED_LIMIT)

else :
    print("Unrecognized martial status")
    exit()

totalTax = tax1 + tax2

# Display the tax.
print(f"The tax is ${totalTax:,.2f}")