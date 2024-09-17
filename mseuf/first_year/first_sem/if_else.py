#Squaring the Years
birthYear = 0
currentYear = 0
squareRoot = 0

birthYear = int(input('Enter your birth year: '))
currentYear = int(input('Enter the current year: '))
squareRoot = (currentYear-birthYear)**.5

if squareRoot.is_integer():
    print('Your age is a perfect square.')
else:
    print('Your age is not a perfect square.')

#Capricorns Now
month = 0
day = 0

month = int(input('Enter your birth month: '))
day = int(input('Enter your birth day: '))

if month ==12:
    if day >= 22 and day <= 31:
        print ('Your zodiac sign is Capricorn.')
elif month ==1:
    if (day >= 1) and day <= 19:
        print ('Your zodiac sign is Capricorn.')
else:
    print('Your zodiac sign is not Capricorn.')
