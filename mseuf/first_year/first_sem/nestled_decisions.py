#Book Recommendation
age = int(input('Enter your age: '))
genrePref = input('Enter your genre preference (a for adventure, m for mystery, f for fantasy, s for science fiction): ')

if age >=8 and age <=12:
    if genrePref == "a":
        print ('The Adventures of Tom Sawyer')
    elif genrePref == "m":
        print ('Nancy Drew: The Secret of the Old Clock')
elif age >=13:
    if genrePref == "f":
        print ("Harry Potter and the Sorcerer's Stone")
    elif genrePref == "s":
        print("Ender's Game")
elif age <8 or age >17:
    print ("No recommendation available")
  
#Second Perfection
num = int(input('Enter an integer: '))

sqRoot = num**.5
cubeRoot = num**(1/3)
evenCube = cubeRoot%2
checkSq = sqRoot % 1
checkCube = cubeRoot % 1

if checkCube ==0 and num !=64:
    if checkSq ==0:
        print('Perfect in every way')
    elif evenCube ==0:
        print('Perfect in even cubes')
    elif evenCube !=0:
        print('Perfect in an odd way')
else:
    print('Nothing special')
