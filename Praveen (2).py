'''
Name : Praveen Kumar Nampalli
Course : Ict4370-1
Date : 10-Apr-2022
This program gives the result of stock owner bob's highest increase in value on a per share basis.
'''
#creating the list of stocks, num of shares, purchase price, and current value
stocks = ['GOOGLE', 'MSFT','RDS-A', 'AIG','FB']
numOfShares = [25,85,400,235,130]
purchasePrice = [772.88,56.60,49.58,54.21,124.31]
currentValue = [941.53,73.04,55.74,65.27,175.45]

#printng the table header 
print('Stocks  \tnumOfShares \tpurchasePrice \tcurrentValue')
for i in range(len(stocks)):
    print(stocks[i],numOfShares[i],purchasePrice[i],currentValue[i],sep='\t\t')
#printing the stock header with owner name 
print('Stock ownership for Bob Smith')
#printing the stock  header with Share and Earn/Loss 
print('Stock\tShare# \tEarning/Loss')
#Using the condtional if to print the table
highestIncrease=[]
cond=False
#Using for loop to print the table
for i in range(len(stocks)):
    highestIncrease.append(currentValue[i]-purchasePrice[i])
    if highestIncrease[i]>0:
        cond = True
    net = (numOfShares[i]*highestIncrease[i])
#print the 2decimal values using float variable
    net = format(net, '.2f')
#prints the stocks and num of share values
    print(stocks[i],numOfShares[i],net,sep='\t')

if cond:

#prints the highest increase value in the portfolio on share basis  
  print("The stock with the highest increase in value in your portfolio on a per share basis is",stocks[highestIncrease.index(max(highestIncrease))])
else:
#prints the lowest decrease value in the portfolio on share basis
  print("The stock with the least decrease in value in your portfolio on a per share basis is",stocks[highestIncrease.index(max(highestIncrease))])
