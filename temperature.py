# Celsius to Fahrenheit & Kelvin

# Reading temperature in Celsius
celsius = float(input('Enter temperature in celsius: '))

# Converting
fahrenheit = 1.8 * celsius + 32
kelvin = 273.15 + celsius

# Displaying output
print('%0.3f Celsius = %0.3f Fahrenheit.' % (celsius, fahrenheit))
print('%0.3f Celsius = %0.3f Kelvin.' % (celsius, kelvin))
