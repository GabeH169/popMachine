# @Gabriel Haro-Villa
def main():
    countyNames = ["Chase", "Crawford", "Ford", "Harper", "Kiowa", 
                   "McPherson", "Norton", "Republic", "Shawnee", "Wabaunsee"]
    
    countySeats = ["Cottonwood Falls", "Girard", "Dodge City", "Anthony", 
                   "Greensburg", "McPherson", "Norton", "Belleville", 
                   "Topeka", "Alma", ]
    
    countyPops = [2572, 38972, 34287, 5485, 2460, 
                  10038, 5459, 4674, 178909, 6877]
    
        
    showCountyData(countyNames, countySeats, countyPops)
    name = input("\nCounty to insert: ").title()
    seat = input(f"{name} County seat: ")
    pop = int(input(f"{name} County population (digits only): "))
    
    ## ADD CODE
    # Call findInsertionIndex to find the index where the county name just
    # entered is to be inserted into the countyNames list. Depending upon
    # the index returned either insert or append the county name, seat,
    # and population into their respective lists.
    index = findInsertionIndex(countyNames, name)
    countyNames.insert(index, name)
    countySeats.insert(index, seat)
    countyPops.insert(index, pop)
    
    print()  
    showCountyData(countyNames, countySeats, countyPops)
    name = input("\nCounty requiring population adjustment: ").title()
    
    ## ADD CODE
    # Call linearSearch to find the index where the county just entered is
    # located in the countyNames list. IF the name was found, display the
    # current population with thousands separators and prompt for the new
    # population. Store the new population at the given index in the
    # countyPops list. ELSE display that the county wasn't found.
    indx = linearSearch(countyNames, name)
    if indx != -1:
        currentPop = countyPops[indx]
        print(f"Current population: {currentPop:,}")
        newPop = int(input("New population (digits only): "))
        countyPops[indx] = newPop
    else:
        print(f"{name} County not found")
    
    print()    
    showCountyData(countyNames, countySeats, countyPops)
   
# showCountyData displays the data for the given counties
# @param countyNames The list of county names
# @param countySeats The list of county seats
# @param countyPops The list of county populations
def showCountyData(countyNames, countySeats, countyPops):
    for i in range(len(countyNames)):
        print(countyNames[i])
        print(f"  Seat: {countySeats[i]}")
        print(f"  Population: {countyPops[i]:,}")
    
# linearSearch searches for a given value in a list
# @param theList The list to search
# @param value The value to match
# @return The index of value if found or -1 if not found.
def linearSearch(theList, value) :
    try:
        index = theList.index(value)
    except:
        index = -1
    return index

# findInsertionIndex finds the index where value is to be inserted
# into the list.
# @precondition The list of values is in increasing sorted order
# @param theList The list of values
# @param value the value to insert
# @return the located index
def findInsertionIndex(theList, value):
    for i in range(len(theList)):
        if theList[i] >= value:
            return i
    return len(theList)

main()