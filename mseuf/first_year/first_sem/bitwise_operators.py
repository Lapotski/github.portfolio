#12 OR 25
num1 = 12
num2 = 25

result = num1 | num2
print (result)

#AND with N
numN = int(input("Enter an integer: "))
numOne = 25

result = numN & numOne
print (numN, "AND", numOne, "=", result)

#X Right Shift Y
a = int(input("Enter A: "))
b = int(input("Enter B: "))

result = x>>y
print (a,">>",b,"=",result)

#Swapping Bitwise
x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))

print ("Before swap: num1 =",str(x)+", num2 =",y)

x = x^y
y = x^y
x = x^y

print ("After swap: num1 =",str(x)+", num2 =",y)
