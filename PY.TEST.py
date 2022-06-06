'''
Name : Praveen Kumar Nampalli
Course : Ict4370-1
Date : 06/05/2022
 In this program we tried use test cases on stock and run, where the result should match the data provided in the previous assignment PYW8
 and the result should show the success test with no errors
'''
#imprting unitest library and Stock from PYW8 assignment
import unittest
from PYW8 import Stock

# creating a class 
class StockTestCase(unittest.TestCase):

#defining the test functions
    def test_stock_name(self):
        res = Stock('GOOG', 20,30,19,25,250,1111177,2/17/2017)
        stockname = res.Symbol
        self.assertEqual(stockname, 'GOOG')         #using assertion to verify the given stock symbol are equal or not

    def test_stock_date(self):
        res = Stock('GOOG', 20,30,19,25,250,1111177,2/17/2017)
        stockdate = res.stockDate
        self.assertEqual(stockdate, 2/17/2017)       #using assertion to verify the given stock date are equal or not

    def test_stock_close(self):
        res = Stock('GOOG', 20,30,19,25,250,1111177,2/17/2017)
        stockclose = res.Close
        self.assertEqual(stockclose,25)              #using assertion to verify the given stock close value are equal or not

    def test_stock_shares(self):
        res = Stock('GOOG', 20,30,19,25,250,1111177,2/17/2017)
        stockshares = res.noOfShare
        self.assertEqual(stockshares,250)            #using assertion to verify the given stock share value are equal or not

def main():
    unittest.main()

if __name__ == "__main__":
    main()
   




