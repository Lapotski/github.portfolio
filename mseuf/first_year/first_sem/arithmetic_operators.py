#Addition and Subtraction
x = int(input("Enter x: "))
y = int(input("Enter y: "))

sum = x+y
dif = x-y

print ("%d + %d =" % (x,y) ,sum)
print ("%d - %d =" % (x,y) ,dif)

#Celsius to Fahrenheit Converter
c = float(input("Enter temperature in Celsius: "))

calF = c * (9/5) + 32
formF = format(calF, '.2f')

print ("Temperature in Fahrenheit:", formF)
