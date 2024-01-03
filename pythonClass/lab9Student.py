# @Gabriel Haro-Villa
from random import randint

def main():
    rows = int(input("Number of rows: "))
    cols = int(input("Number of columns: "))
    low = int(input("Lowest potential value: "))
    high = int(input("Highest potential value: "))
    
    matrix = getTable(rows, cols)
    fillMatrix(matrix, low, high)
    location = findHighestValue(matrix)
    displayMatrix(matrix)
    print(f"The highest value is {matrix[location[0]][location[1]]} and is located at {location}")

# getTable creates a rows x cols table initialized to 0's
# @param rows The number of rows
# @param cols The number of columns
# @return the rectangular table
def getTable(rows, cols):
    table = []
    for row in range(rows):
        nextRow = [0] * cols
        table.append(nextRow)
    return table

# displayMatrix displays a matrix in table format with a cell width of 4
# @param matrix The matrix to display
def displayMatrix(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            print(f"{matrix[row][col]:4d}", end = "")
        print()

# fillMatrix fills a matrix with random integers in the range -10 through 10
# @param matrix The matrix to fill
# @param lowest The lowest potential value
# @param highest The highest potential value
def fillMatrix(matrix, lowest, highest):
    
    for rowList in matrix:
        for col in range(len(rowList)):
            rowList[col] = randint(lowest, highest)

# It will find the location of the highest value in the matrix.
# @param matrix to find the location
# @return the tuple containing two elements (location).
def findHighestValue(matrix):
    value = matrix[0][0]
    highRowIndex = 0
    highColIndex = 0
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            val = matrix[row][col]
            if val > value:
                value = val
                highRowIndex = row
                highColIndex = col
    return [highRowIndex, highColIndex]
        
main()