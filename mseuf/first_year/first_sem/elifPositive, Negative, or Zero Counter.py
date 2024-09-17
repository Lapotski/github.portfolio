num1 = 0
num2 = 0
num3 = 0
num4 = 0
num5 = 0
positive = 0
negative = 0
zero = 0

num1 = int(input('Enter first integer: '))
num2 = int(input('Enter second integer: '))
num3 = int(input('Enter third integer: '))
num4 = int(input('Enter fourth integer: '))
num5 = int(input('Enter fifth integer: '))

if num1 != 0 or num1 == 0:
    if num1 > 0:
        positive+=1
    elif num1 < 0:
        negative+=1
    else:
        zero+=1
if num2 != 0 or num1 == 0:
    if num2 > 0:
        positive+=1
    elif num2 < 0:
        negative+=1
    else:
        zero+=1
if num3 != 0 or num3 == 0:
    if num3 > 0:
        positive+=1
    elif num3 < 0:
        negative+=1
    else:
        zero+=1
if num4 != 0 or num4 == 0:
    if num4 > 0:
        positive+=1
    elif num4 < 0:
        negative+=1
    else:
        zero+=1
if num5 != 0 or num5 == 0:
    if num5 > 0:
        positive+=1
    elif num5 < 0:
        negative+=1
    else:
        zero+=1

print ('Positive count:', positive)
print ('Negative count:',negative)
print ('Zero count:',zero)
