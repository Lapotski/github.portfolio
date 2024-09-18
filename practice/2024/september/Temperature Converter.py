# Temperature Converter

# Initialize variables
cont = "true"
option = 0

while cont.lower() == "true": 
    print("Choose the conversion type: \n1. Celsius to Fahrenheit \n2. Fahrenheit to Celsius")
    option = int(input("Enter your choice (1 or 2): "))
    
    if option == 1:
        temps = float(input("Enter temperature in Celsius: "))
        fahrenheit = (temps * 9/5) + 32
        print(f"Temperature in Fahrenheit: {fahrenheit:.2f}°F")
    elif option == 2:
        temps = float(input("Enter temperature in Fahrenheit: "))
        celsius = (temps - 32) * 5/9 
        print(f"Temperature in Celsius: {celsius:.2f}°C")
    else:
        print("Invalid Option")
    
    cont = input("Do you want to keep converting (TRUE or FALSE): ").lower()
