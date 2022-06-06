'''
Name : Praveen Kumar Nampalli
Course : Ict4370-1
Date : 05/08/2022
 In this program created a bond data, purchase class details using classes and exemptions, importing csv files
  and prints the result in a text file
'''
import csv
import sys
try:
    outfile = open('D:/output.txt', 'a')
except OSError:
    print("Could not open/read file:")
    sys.exit()
sys.stdout = outfile

from datetime import date, datetime
class Stock:
    def __init__ (self, stockName, noOfShare, purchasePrice, currentPrice, purchaseDate, stockId):
        self.stockName = stockName
        self.noOfShare = noOfShare
        self.purchasePrice = purchasePrice
        self.currentPrice = currentPrice
        self.purchaseDate = purchaseDate
        self.stockId = stockId
        
    def getDaysDifference (self):
        d1 = datetime.today ()
        d2 = self.purchaseDate 
        d2Format = datetime.strptime(d2, '%m/%d/%Y')#date.fromisoformat (d2) 
        daysBetween = ((d1 - d2Format).days)
        return daysBetween
    
    def calcLossOrGain (self):
        earningLoss = round ((float (self.currentPrice) - float (self.purchasePrice)) *
                             float (self.noOfShare),2)
        return earningLoss
    
    def calcEarningPerShare (self):
        perShareEarning = round (float (Stock.findLossOrGain (self)) /
                                 float (self.noOfShare),2)
        return perShareEarning
    
    def calcYield (self):
        yieldValue = round (((((float (self.currentPrice) -
        float (self.purchasePrice)) /float (self.purchasePrice)))) * 4)
        return yieldValue

    def calcEarnLossRate (self):
        earningRate = round ((((((self.currentPrice) -
        float (self.purchasePrice)) /float (self.purchasePrice))
                        /(float (Stock.getDaysDifference(self))))* 100), 4)
        return earningRate

    def printBondData (self):
        print ((str (self.stockName)), (str (self.noOfShare)), ("$" + str (self.purchasePrice)), ("$" + str (self.currentPrice)), (self.purchaseDate), (self.stockId),
         (str (self.coupon)), (str (self.yieldValue) + "%"),sep='\t\t',end="\n")
       
    def printBondHeader ():
        print ("-" * 125)
        print ('\t\t\t\t\t\tBond Ownership for Bob Smith')
        print ("-" * 125)
        print ('Bond\t\tShare#\t\tPurchase Price\tCurrent Price\tPurchase Date\tStockId\tCoupon\tYield')
        print ("-" * 125)
        
    def stockTablesHeader():
        print ("-" * 125)
        print ('\nStock \tShare# \tEarnings/Loss \tYearly Earning/Loss') 
        print ("-" * 75)
    
    def printStockTable (self):
        print(self.stockName,self.noOfShare,self.purchasePrice,self.currentPrice,sep='\t\t')

      
    def printStockValues (self):
        print ((str (self.stockName)),(str (self.noOfShare)),("$" + str (Stock.calcLossOrGain (self))) ,(str (Stock.calcEarnLossRate (self)) + "%"),sep='\t\t') 
        
class Bonds (Stock):
    def __init__ (self, name, share, purchase, current, pDate, stockId, coupon, yieldValue):
        super ().__init__ (name, share, purchase, current, pDate, stockId)
        self.coupon = coupon
        self.yieldValue = yieldValue

    def getCoupon ():
        return self.coupon

    def getYeildRate():
        return self.yieldValue
        print ("-" * 125)  

 
stocks = {}
id=100

try:
    with open('D:/Lesson6_Data_Stocks.csv', 'r') as file:
        reader = csv.reader(file)
        for row in list(reader)[1:]:
            stocks[row[0]] = (Stock (row[0], int(row[1]), float(row[2]), float(row[3]), row[4], id))
            id = id+1
except OSError:
    print("Could not open/read file:")
    sys.exit()

print('\nBond Table')
bonds = []

try:
    with open('D:/Lesson6_Data_Bonds.csv', 'r') as file:
        reader = csv.reader(file)
        for row in list(reader)[1:]:
            bonds.append(Bonds (row[0], int(row[1]), float(row[2]), float(row[3]), row[4],id ,float(row[5]), float(row[6])))
            id = id+1
except OSError:
    print("Could not open/read file:")
    sys.exit()
    
Bonds.printBondHeader()

for i in range(len(bonds)):
    bonds[i].printBondData()
Stock.stockTablesHeader()

for key in stocks:
    stocks.get(key).printStockValues()

outfile.close()
