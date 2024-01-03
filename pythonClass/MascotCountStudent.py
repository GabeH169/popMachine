# @Gabriel Haro-Villa

def main():
    schools = getSchoolMascots("KansasHighSchoolsSubsetUnclean.txt")
    mascotCount = getMascotCount(schools)
    showMascotCount(mascotCount)
    
# getSchoolMascots reads each school and their mascot from the given file.
# @param filename The file containing the schools and mascots.
# @precondition Each line in the file is of the form school:mascot
# @return A dictionary of school-mascot pairs   
def getSchoolMascots(filename):
    schools = {}
    
    with open(filename, 'r') as inFile:
        for line in inFile:
            schoolName, mascot = line.split(':')
            schoolName = schoolName.strip()
            mascot = mascot.strip().title()
            schools[schoolName] = mascot

    return schools

# getMascotCount tallies the number of times each mascot occurs
# @param schools A dictionary of school-mascot pairs
# @return A dictionary of mascot-count pairs
def getMascotCount(schools):
    mascotCount = {}

    for school in schools:
        mascot = schools[school]
        if mascot not in mascotCount:
            mascotCount[mascot] = 1
        else:
            mascotCount[mascot] += 1

    return mascotCount

# showMacotCount displays the mascots in sorted order. Each mascot 
# count is shown by the mascot.
# @param mascotCount A dictionary containing each mascot and the number
#        of times it occurred.
def showMascotCount(mascotCount):
    sortedMascots = sorted(mascotCount.keys())

    for mascot in sortedMascots:
        count = mascotCount[mascot]
        print(f"{mascot}: {count}")

main()