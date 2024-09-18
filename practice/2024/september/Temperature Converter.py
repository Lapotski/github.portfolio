#Temperature Converter

#initialize variables
cont = "TRUE"
option = 0
celcius = 0
fahrenheit = 0
temps = 0

while cont  == "TRUE":
    print ("Choose the conversion type: \n1. Celcius to Fahrenheit \n2.Fahrenheit to Celcius")
    option = int(input("Enter your choice (1 or 2): "))
    if option == 1:
        temps = float(input("Enter temperature in Celcius: "))
        fahrenheit = (temps * 9/5) + 32
        print(f"Temperature in Fahrenheit: {fahrenheit:.2f}°F")
    elif option == 2:
        temps = float(input("Enter temperature in Fahrenheit: "))
        celcius = (temps - 32) * 5/9
        print(f"Temperature in Celcius: {celcius:.2f}°C")
    else:
        print("Invalid Option")
    cont = input("Do you want to keep converting (TRUE or FALSE): ")