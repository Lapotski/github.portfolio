"""We just got home from a trip to South America, specifically Colombia, Peru, and Brazil. There's some leftover cash in:
🇨🇴 Colombian pesos
🇵🇪 Peruvian soles
🇧🇷 Brazilian reais"""

clmPesos = float(input("How much do you have in pesos? "))
prvSoles = float(input("How much do you have in soles? "))
brzReais = float(input("How much do you have in Reais? "))

usDollars = ((clmPesos * 0.00024) + (prvSoles * 0.27) + (brzReais * 0.18))

print ("You have $",usDollars)
