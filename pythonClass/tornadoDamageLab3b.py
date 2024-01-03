# @Gabriel Haro-Villa

# This program will get a wind speed in miles per hour from a user and display
# the corresponding damage report

# CONSTANTS
EF_5 = 200
EF_4 = 166
EF_3 = 133
EF_2 = 111
EF_1 = 86
EF_0 = 65

# Get the wind speed from user input
windSpeed = int(input("Wind speed (MPH): "))

# Display the damage report
if windSpeed > EF_5 :
    print("EF-5: Destruction of all infrastructure.")
elif EF_4 <= windSpeed:
    print("EF-4: Homes leveled, cars thrown around.")
elif EF_3 <= windSpeed:
    print("EF-3: Entire stories of homes and buildings destroyed, trains " +
        "overturned, cars lifted off the ground.")
elif EF_2 <= windSpeed:
    print("EF-2: Torn off roofs, mobile homes destroyed, large trees " + 
        "uprooted.")
elif EF_1 <= windSpeed:
    print("EF-1: Roofs stripped, mobile homes overturned, exterior home " +
        "damage.")
elif EF_0 <= windSpeed:
    print("EF-0: Some damage to roofs, siding, and tree branches.")
else :
    print("Likely not a tornado.")