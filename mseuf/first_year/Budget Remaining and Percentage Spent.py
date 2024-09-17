#Budget Remaining and Percentage Spent

budgetTot = float(input('Enter your monthly budget: '))
budgetSpent = float(input('Enter how much you\'ve spent: '))

budgetRemain = budgetTot-budgetSpent
percSpent = (budgetSpent/budgetTot)*100

print('Your remaining balance is ₱%.2f, gastador ka kasi.' % budgetRemain)
print('You have spent '+str(percSpent)+"% of your budget. Nanlumo ka ba bigla?")