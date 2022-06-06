'''
Name : Praveen Kumar Nampalli
Course : Ict4370-1
Date : 05/22/2022
 In this program created data visualizing on stock class and generated a graph using classes and objects by importing csv file and json file
  and prints the result as figure in graph model
'''
#importing the libraries
import json
import csv
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
from datetime import datetime
import matplotlib.pyplot as plt


#reading the stock details from csv file
rows = {}
with open(r'C:\Users\prave\Downloads\Lesson6_Data_Stocks.csv') as file:
    csvreader = csv.reader(file)
    for row in list(csvreader)[1:]:
            rows[row[0].lower()] = int(row[1])
            
print(rows)

#loading the alls stock data from json file
file_path = r'C:\Users\prave\Downloads\AllStocks.json'
with open(file_path) as json_file: 
    data_set = json.load(json_file)

#creating the class
class stock:
    def __init__ (self, Symbol, Open, High, Low, Close, noOfShare, stockVolume, stockDate):
        self.Symbol = Symbol.title()
        self.Open = Open
        self.High = High
        self.Low = Low
        self.Close = Close
        self.noOfShare = noOfShare
        self.stockVolume = stockVolume
        self.stockDate = stockDate
        self.closingPrice = 0
        
    def add_stock(self, closingPrice):
        self.closingPrice = closingPrice
        
def describe_stock(self):
#Display a summary of the stock's information
       print("\n" +(self.Symbol))
       print("  Open " + str(self.Open))
       print("  High " + str(self.High))
       print("  Low " + str(self.Low))
       print("  Close " + str(self.Close))
       print("  noOfshare " + str(self.noOfshare))

#calculating the closing price with multiplying the close price and noOfshare values
def calcClosingprice (self):
        closingPrice = round ((int (self.Close)) * int (self.noOfShare),2)
        return closingPrice

#creating the dictionary 
stockDictionary = []
for stk in data_set:
    if stk['Symbol'].lower() not in stockDictionary:
        stockDictionary.append(stock(stk['Symbol'].lower(), stk['Open'], stk['High'], stk['Low'], stk['Close'], rows[stk['Symbol'].lower()], stk['Volume'], stk['Date']))
        
#creating a for loop for stockdictionary
plot = {}
for stock in stockDictionary:
    stock.add_stock(calcClosingprice(stock))

    if stock.Symbol.lower() not in plot:
        plot[stock.Symbol.lower()]=[]
    plot[stock.Symbol.lower()].append([stock.stockDate,stock.closingPrice])

#giving the colors to each stock to identify 
col=['blue','orange', 'green', 'red', 'purple', 'brown', 'pink', 'grey']


count=0

#Printing data to make sure everything is updating as expected
print(plot)
for key, value in rows.items(): 
    xAxis = [value[0] for value in plot[key.lower()]]
    yAxis = [value[1] for value in plot[key.lower()]]
    plt.plot(xAxis, yAxis, color=col[count], linestyle='solid', marker='None')
    plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=85))
    plt.gca().yaxis.set_major_locator(mticker.MaxNLocator(5))
    plt.gcf().autofmt_xdate()
    count=count+1
    
# LINE GRAPH 
plt.xlabel('Date')
plt.ylabel('Volume')
plt.gca().invert_xaxis()
plt.rcParams["figure.figsize"] = [1.50, 1.50]
plt.rcParams["figure.autolayout"] = True
line1, = plt.plot([], label="GOOGL")    #labeling the stock symbols with receeding colors
line2, = plt.plot([], label="MSFT")
line3, = plt.plot([], label="RDS-A")
line4, = plt.plot([], label="AIG")
line5, = plt.plot([], label="FB")
line6, = plt.plot([], label="M")
line7, = plt.plot([], label="F")
line8, = plt.plot([], label="IBM")
leg = plt.legend(loc='upper left')      #labeling the stock symbols on the top left corner
plt.savefig('Allstocks.png')            #saving the fig in .png format
plt.show()
