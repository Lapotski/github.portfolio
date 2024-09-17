# Write code below 💖

#global variables
lion = 0
raven = 0
badger = 0
snake = 0

#question 1

q1 = int(input("""Q1) Do you like Dawn or Dusk?
    1) Dawn
    2) Dusk
    Answer: """))

if q1==1:
  lion +=1
  raven +=1
elif q1==2:
  badger +=1
  snake +=1
else:
  print("Wrong Input.")

#question 2

q2 = int(input("""Q2) When I’m dead, I want people to remember me as:
    1) The Good
    2) The Great
    3) The Wise
    4) The Bold
    Enter your answer here: """))

if q2==1:
  badger+=2
elif q2==2:
  snake+=2
elif q2==3:
  raven+=2
elif q2==4:
  lion+=2
else:
  print("Wrong input.")

#question 3

q3 = int(input("""Q3) Which kind of instrument most pleases your ear?
    1) The violin
    2) The trumpet
    3) The piano
    4) The drum
    Enter your answer here: """))

if q3 == 1:
  snake+=4
elif q3==2:
  badger+=4
elif q3==3:
  raven+=4
elif q3==4:
  lion+=4
else:
  print ("Wrong input.")

print ("""
House Points!
""")
print ("Gryffindor",lion)
print ("Ravenclaw",raven)
print ("Hufflepuff",badger)
print ("Slytherin",snake)
print ("")

#House Sorting
print("You have been sorted!")
if lion>=4:
  print ("You are a 🦁 Gryffindor!")
elif raven>+4:
  print("You are a 🦅 Ravenclaw!")
elif badger>=4:
  print("You are a 🦡 Hufflepuff!")
elif snake>=4:
  print ("You are a 🐍 Slytherin!")
else:
  print("Something went wrong try again.")
