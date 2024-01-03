# @Gabriel Haro-Villa

# This program will calculate the heat index by using the
# entered temperature and relative humidity

def main():
    MIN_TEMP = 80
    MAX_TEMP = 110
    MIN_HUMIDITY = 40
    MAX_HUMIDITY = 100
    
    temp = int(input(f"Fahrenheit Temperature ({MIN_TEMP} - {MAX_TEMP}): "))
    while not MIN_TEMP <= temp <= MAX_TEMP :
        temp = int(input(f"Fahrenheit Temperature"
                         f" ({MIN_TEMP} - {MAX_TEMP}): "))
        
    humidity = int(input(f"Relative Humidity ({MIN_HUMIDITY} -"
                         f" {MAX_HUMIDITY}): "))
    while not MIN_HUMIDITY <= humidity <= MAX_HUMIDITY :
        humidity = int(input(f"Relative Humidity ({MIN_HUMIDITY} -"
                             f" {MAX_HUMIDITY}): "))
        
    heatIndx = getHeatIndex(temp, humidity)
    print()
    print(f"Heat index: {heatIndx:.1f} degrees")

# getHeatIndex calculates the heat index
# @param temp The current temp
# @param humidity The current humidity
# @return The calculated heat index
def getHeatIndex(temp, humidity) :
    temp2 = temp ** 2
    humidity2 = humidity ** 2
    heatIndex = (-42.379 + (2.04901523 * temp) + (10.14333127 * humidity) \
        - (0.22475541 * temp * humidity) - 6.83783 * ((10 ** -3) * temp2) \
        - 5.481717 * ((10 ** -2) * humidity2) + \
        1.22874  * ((10 ** -3) * temp2 * humidity) +
        8.5282 * ((10 ** -4) * temp * humidity2) - \
        1.99 * ((10 ** -6) * temp2 * humidity2))
    return heatIndex

main()