# @Gabriel Haro-Villa
def main():
    # Create three empty lists named countyNames, countySeats, and countyPops
    countyNames = []
    countySeats = []
    countyPops = []
    state = input("Get county data for which state: ")
    #Call getCountyData with the state and the lists
    getCountyData(state, countyNames, countySeats, countyPops)
    
    EXIT = "4"
    choice = "0"
    while (choice != EXIT):
        print("(1) Show statistical summary")
        print("(2) Show counties within a given population range")
        print("(3) Show counties beginning with a certain letter")
        print("(4) Exit")
        choice = input("Choice? ")
        
        # Insert one multiway branching if statement to handle each menu
        # choice. Notice that the choice is a string, even though a digit is
        # to be entered. This will guard against a program crash if a non-digit
        # were entered.
        if choice == '1':
            showStatSummary(state, countyNames, countySeats, countyPops)
        elif choice == '2':
            print("Show counties with what population range?")
            lowerBound = int(input("Lower bound: "))
            upperBound = int(input("Upper bound: "))
            showPopulationRange(lowerBound, upperBound, countyNames, countySeats, countyPops)
        elif choice == '3':
            letter = input("Show counties beginning with which letter? ").upper()
            showCountySubset(letter, countyNames, countySeats, countyPops)

        print()

# getCountyData reads county data from a given state's file into the list
# parameters. The county name, its seat, and its population will be stored
# at the same index in each of the three different lists.
# @param state The name of the state for which data is to be read
# @param countyNames Will be filled with the state's county names
# @param countySeats Will be filled with the seat for each county
# @param countyPops Will be filled with populations for each county
def getCountyData(state, countyNames, countySeats, countyPops):
    fileName = r'C:\\Users\\gabri\\OneDrive\Documents\\pythonClass\\' + state + 'CountyData.txt'
    inFile = open(fileName, 'r')
    next(inFile)
    for line in inFile:
        data = line.split(',')
        if len(data) == 3:
            countyNames.append(data[0])
            countySeats.append(data[1])
            countyPops.append(int(data[2]))
    inFile.close()


# showStatSummary displays the state population, the number of counties, and
# the average county population.
# @precondition countyNames, countySeats, and countyPops are parallel
# @param state The name of the state
# @param countyNames The county names for the state
# @param countySeats The county seats for the state
# @param countyPops The county populations for the state
def showStatSummary(state, countyNames, countySeats, countyPops):
    numCounties = 0
    totalCountyPop = 0

    for i in range(len(countyNames)):
        numCounties += 1
        totalCountyPop += countyPops[i]
        avgCountyPop = round(totalCountyPop / numCounties)

    print(f"Statistics for {state}:")
    print(f"State population: {totalCountyPop:,}")
    print(f"Number of counties: {numCounties}")
    print(f"Average county population: {avgCountyPop:,}")
# showPopulationRange shows county information for those county populations
# within a given population range.
# @precondition countyNames, countySeats, and countyPops are parallel
# @param lowerBound The inclusive lower bound for the range
# @param upperBound The inclusive upper bound for the range
# @param countyNames The county names for the state
# @param countySeats The county seats for the state
# @param countyPops The county populations for the state    
def showPopulationRange(lowerBound, upperBound, countyNames, countySeats, countyPops):
    for i in range(len(countyPops)):
        if lowerBound <= countyPops[i] <= upperBound:
            print(f"{countyNames[i]},{countySeats[i]},{countyPops[i]}")

# showCountySubset shows county information for those county names
# beginning with a given letter. 
# @precondition countyNames, countySeats, and countyPops are parallel
# @param letter The first letter to match
# @param countyNames The county names for the state
# @param countySeats The county seats for the state    
def showCountySubset(letter, countyNames, countySeats, countyPops):
    for i in range(len(countyNames)):
        if countyNames[i].startswith(letter):
            print(f"{countyNames[i]},{countySeats[i]},{countyPops[i]}")

main()