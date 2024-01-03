# This program runs a simple pop machine.
# @Gabriel Haro-Villa
#an edit
from Slot import Slot
from Soda import Soda

def main():
    popMachine = startMachine("sodas.txt")
    purchaseMore = "Y"
    while (purchaseMore[0].upper() == "Y"):
        showMachine(popMachine)
        slotNum = int(input("Which slot #? "))

        # ** ADD CODE **
        # Remember that the index of the slot in the machine is
        # 1 less than slotNum just entered by the user above.

        # If the slot's quantity is 0 
        #   state that the slot is sold out (Remember to match the output)
        # else 
        #   1. Continue to get deposits until enough money is entered
        #   2. Tell the user to take their soda. Telling them to take
        #   their change if some is left is optional. This was not done
        #   in the sample run.
        #   3. Call the purchase method for the slot with a value of 1.
        #      (This means that 1 item was purchased from the slot)
        slotIndex = slotNum - 1

        if popMachine[slotIndex].getQuantity() == 0:
            print(f"Slot {slotNum} sold out")
        else:
            deposit = 0.0
            while deposit < popMachine[slotIndex].getItem().getPrice():
                deposit += float(input("Enter deposit: $"))
            print(f"Please take your {popMachine[slotIndex].getItem().getName()}")
            popMachine[slotIndex].purchase(1)
        purchaseMore = input("Purchase another item (Y or N)? ")
        print()
    stopMachine(popMachine, "sodasChanged.txt")

# startMachine stocks the pop machine based upon file data
# @param filename The filename containing the data
# @return A pop machine list filled with slots
def startMachine(filename):
    machine = []
    with open(filename, "r") as inFile:
        for line in inFile:
            slotData = line.split(",")
            soda = Soda(slotData[0], 
                        float(slotData[1]),
                        int(slotData[2]))
            slot = Slot(soda, int(slotData[3]))
            machine.append(slot)
    return machine

# showMachine shows the sodas in the machine, preceded with a slot
# number. The quantity in the slot is also shown.
# @param machine The list of pop machine slots
def showMachine(machine):
    slotNum = 1
    for slot in machine:
        soda = slot.getItem()
        print(f"{slotNum}. {soda.getName()}, ${soda.getPrice():.2f}" +
              f" ({slot.getQuantity()} available)")
        slotNum += 1

# stopMachine stores the current state of the machine back to file
# @param machine The list of pop machine slots
# @param filename The filename to which the data is written
def stopMachine(machine, filename):
    with open(filename, "w") as outFile:
        for slot in machine:
            outFile.write(f"{slot}\n")
            
main()