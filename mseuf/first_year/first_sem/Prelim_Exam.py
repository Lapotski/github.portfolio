"""(paraphrased) Netflix is donating 10% of every sub to charity. Netflix is getting taxed 5%.
Input netflix sub price, amount of subs, percentage donated,
Display total gross amount, amount donated, tax amount, net sale."""

#Constant Variable
TAX = .05

#Initialize Variables
netflixPrice = 0
netflixSubs = 0
percDonation = 0
totalGross = 0
amountDonated = 0
taxAmount = 0
netSale = 0
donationConversion = 0 

#user input
netflixPrice = float(input('Enter Netflix Subscription Price: '))
netflixSubs = int(input('Enter the amount of Netflix Subscriptions: '))
percDonation = float(input('Enter the percentage donated to charity: '))

#calculations
totalGross = netflixPrice*netflixSubs
donationConversion = percDonation/100
amountDonated = totalGross*donationConversion
taxAmount = totalGross*TAX
netSale = totalGross-(amountDonated+taxAmount)

#display outputs
print ('Total Gross Amount: $%.2f' % totalGross)
print ('Amount Donated: $%.2f' % amountDonated)
print ('Tax: $%.2f' % taxAmount)
print ('Net Sale: $%.2f' % netSale)