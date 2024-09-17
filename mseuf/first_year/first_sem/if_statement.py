#Same Sign
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 > 0 and num2 > 0:
    print ("Numbers have the same sign.")
elif num1 < 0 and num2 < 0:
    print ("Numbers have the same sign.")
else:
    print ("")

#Leap Years
year = int(input("Enter the year: "))
year4 = year % 4
            
if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
    print ("Year is a leap year.")
