
operation = int(input("Press the desired number for the operation would you like to calculate\n1 Addition\n2 Subtraction\n3 Multiplication\n4 Division\n5 Floor Division\n6 Modulus\n7 Exponentation\nEnter the number here: "))
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2
floor_division = num1 // num2
modulus = num1 % num2
exponent = num1 ** num2


print ("\nResults:")

if operation == 1:
    print ("Addition:", addition)
if operation == 2:
    print ("Subtraction:", subtraction)
if operation == 3:
    print ("Multiplication:", multiplication)
if operation == 4:
    print ("Division:", division)
if operation == 5:
    print ("Floor Division", floor_division)
if operation == 6:
    print ("Modulus:", modulus)
if operation == 7:
    print ("Exponent:", exponent)

