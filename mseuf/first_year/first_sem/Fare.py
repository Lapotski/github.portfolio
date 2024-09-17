km = 0
fare = 0
roundedKM = 0
totalFare = 0

km = float(input("Distance travelled in km: "))
roundedKM = round(km*2)/2
totalFare = (roundedKM//.5)*20

print ('Total Fare: %.2f pesos.' % totalFare)