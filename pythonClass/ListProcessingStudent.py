# @Gabriel Haro-Villa
from random import randint

def main() :
    #numRolls = int(input("Number of rolls? "))

    # Create two empty lists named rolls1 and rolls2
    rolls1 = []
    rolls2 = []
    # Call rollDice with rolls1 and the number of rolls entered by the user
    numRolls = int(input("Number of rolls? "))
    rollDice(rolls1, numRolls)
    # Call rollDice with rolls2 and the number of rolls entered by the user
    rollDice(rolls2, numRolls)
      
    print("Rolls 1: ", end = "")
    # Call showList by sending rolls1
    showList(rolls1)
    print("Rolls 2: ", end = "")
    # Call showList by sending rolls2
    showList(rolls2)
    # Determine the lowestTotal for both rolls lists by calling  
    # getLowestTotal and displaying the returned result preceded 
    # by "Lowest Total: "
    lowestTotal = getLowestTotal(rolls1, rolls2)
    print(f"Lowest Total: {lowestTotal}")
    
    #table = getTable() # Completed -- getTable returns a 2d list of integers
    #lowest = int(input("Lowest value to get: "))
    #highest = int(input("Highest value to get: "))    
    # Call getListRange with the table and the lowest and highest values. 
    # Send the result returned from this call to showList
    table = getTable()
    lowest = int(input("Lowest value to get: "))
    highest = int(input("Highest value to get: "))
    listRange = getListRange(table, lowest, highest)
    showList(listRange)

# rollDice appends random values in the range [1, 6] to the rolls list 
# @param rolls The empty list to fill
# @param numRolls The number of roll results to append to the list
def rollDice(rolls, numRolls):
    MAX_SIDE = 6
    MIN_SIDE = 1
    for i in range(numRolls):
        rolls.append(randint(MIN_SIDE, MAX_SIDE))


# showList displays list values on one line with space separators.
# After the values are displayed insert print() so that any future
# output is shown on the next line.
# @param theList The list of values
def showList(theList):
    for value in theList:
        print(value, end = " ")
    print()

# getLowestTotal calculates and returns the lowest total score for the 
# two lists of rolls.
# @param rolls1 The first list of rolls
# @param rolls2 The second list of rolls
# @return The lowest total for all pairs of rolls.
def getLowestTotal(rolls1, rolls2):
    total = 0
    
    for i in range(len(rolls1)):
        if rolls1[i] > rolls2[i]:
            total += rolls2[i]
        else:
            total += rolls1[i]
    return total

# getListRange creates a single dimensional list of values from the table
# that lie within a given inclusive range
# @param table The table (2d list) to search
# @param low The lowest value in the range to include
# #param high The highest value in the range to include
# @return a single dimensional list containing the list of values within
# the given range.
def getListRange(table, lowest, highest):
        result = []
        for line in table:
            for value in line:
                if lowest <= value <= highest:
                    result.append(value)
        return result

# COMPLETED
# getTable creates a two-dimensional list of integers
# @return The table of integers
def getTable():
    return[
        [50, -12, -99, 95, -28, -28, -79, 8, -65, -51, 89, -70, -39, -35, 30],
        [42, 18, -87, 93, 99, -58, -54, -7, -43, -19, -45, 33, 61, 84, 70],
        [-27, -26, 32, 96, -33, -97, -77, -3, -38, 18, -82, 24, -3, 7, 24],
        [-45, -40, 73, 43, 56, 44, -46, -40, 88, 54, 56, -57, 2, -100, -3],
        [-9, 7, 78, 48, -31, 82, 88, -41, 88, -72, -90, 90, -25, 66, 60],
        [-70, -71, 21, 37, 57, -91, -70, 36, -72, 43, 73, 59, 34, -65, -14],
        [-22, 43, -97, 14, 0, 71, -68, -20, 9, 4, 65, 25, 4, -43, 63],
        [79, 62, -92, -6, 85, -49, 89, 16, 87, -13, 59, 36, -72, -67, -82],
        [-72, 10, 29, 20, 55, 25, 1, -32, -84, -20, -48, 52, -24, 59, -53],
        [-97, 70, 59, 35, -71, -59, 16, -99, -22, 97, 6, -18, -46, 11, -2],
        [-97, -13, -28, -67, 70, 33, -18, -29, 34, -14, -46, -83, -18, 54, -37],
        [-94, -92, -61, -25, -20, -13, -10, 7, 4, -1, -48, -49, 4, 99, -90],
        [-71, -77, -60, -25, 56, -84, 63, 42, -44, -79, 35, 68, 43, -54, -50],
        [-44, 7, -77, -26, 0, -93, 29, -99, 18, -89, 82, -13, -30, 92, 26],
        [54, 59, -22, 90, 14, 100, 15, 4, -69, 19, -92, -64, 19, -87, -30]
        ]
main()