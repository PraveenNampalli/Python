'''
Name : Praveen Kumar Nampalli
Course : Ict4370-1
Date : 04/24/2022
The program will print the result of stock onwership of Bob Smith's yearly profit/loss in tabular column
'''
#create date format to show mon-date-year   
from datetime import date

today = date.today()

#calculating the profit/loss using formula
def profitloss(stocks):
    for i in stocks:
        x= (stocks[i][0]*(stocks[i][2] - stocks[i][1]))
        x= round(x,2)
        stocks[i].append(x)

#calculating profit/Loss in percentage using formula
def profitLosspercentage(stocks):
    perval =[]
    for i in stocks:
        perval.append(((stocks[i][2]-stocks[i][1])/stocks[i][1])*100)
      
#calculating yearly profit/Loss
def yearlyprofitLoss(stocks):
    for i in stocks:
        day, month, year = map(int, stocks[i][3].split('/'))
        yearDiff = today.year - year
        x = (((((stocks[i][2] - stocks[i][1])/stocks[i][1])/yearDiff))*100)
        x= round(x,2)
        stocks[i].append(x)


#creating the list of stock, no.of.shares and its purchase,current values with dates
stocks = {'GOOGLE':[125, 772.88,941.53, '8/1/2017'],'MSFT':[85,56.60,73.04,'8/1/2017'],'RDS-A':[400,49.58,55.74,'8/1/2017'],
    'AIG':[235,54.21,65.27,'8/1/2017'],'FB':[130,124.31,175.45,'8/1/2017'],'M':[425,30.30,23.98,'1/10/2018'],'F':[85,12.58,10.95,'2/17/2018'],
    'IBM':[80,150.37,145.30,'5/12/2018']} 

yearlyprofitLoss(stocks)
profitloss(stocks)
profitLosspercentage(stocks)

#prints the table header 
print('-' *70)
print('   \t         Stock ownership for Bob Smith')
print('-' *70)
#prints the above given list in a tabular form
print("stocks\t\tNum# \t\tEarning/Loss\tYearly Earning/Loss")
print('-' *70)

#using for loop to print the calulated result
for i,k in zip(stocks,stocks.keys()):
    print(k,stocks[i][0],stocks[i][5],stocks[i][4],sep="\t\t") 
    print('-' *70)

