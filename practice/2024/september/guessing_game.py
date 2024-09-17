import random
num = random.randint(1, 100)
guess = 0
guessAmount = 0

while guess != num:
  guesss = int(input("Guess the number (1-100): "))
  if (guess <= 0) or (guess > 100):
    print ("INVALID NUMBER!")
  elif guess < num:
    print ("GO HIGHER!")
  elif guess > num:
    print ("GO LOWER!")
  else:
    print ("YOU GOT IT!")
  if guess == num:
    print ("Guesses:", guessAmount)
