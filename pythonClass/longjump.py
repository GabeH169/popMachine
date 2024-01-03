# This program converts a long jump given in
# centimeters to feet and inches
# @Gabriel Haro-Villa

# Get the athlete's name and distance jumped
firstName = str(input("Long jumper's first name: "))
lastName = str(input("Long jumper's last name: "))
distanceJumped = int(input("Distance jumped (cm): "))
print()

# Convert distance to feet and inches
CMS_PER_INCH = 2.54
INCHES_PER_FEET = 12

inches = distanceJumped / CMS_PER_INCH
feet = int(inches / INCHES_PER_FEET)
inches = inches - (INCHES_PER_FEET * feet)

# Display the converted distance
print(f"{firstName[0]}. {lastName} jumped {feet}' -{inches:.1f}\"")