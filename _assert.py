import yfinance as yf

class _assert:
    def __init__(self, symbol, positions, avgCostPrice = -1):
        self.symbol = symbol
        self.positions = positions
        self.avgCostPrice = avgCostPrice
        self.currentPrice = -1
        self.whichMarket = ""
        self.currency = ""  #could be enum type
    
    def queryCurrentPrice(self):
        pass

    def dumpInfo(self):
        print("{}\t{}\t{}\n".format(self.whichMarket, self.symbol, self.currentPrice))
        

class USStockAssert(_assert):
    def queryCurrentPrice(self):
        #https://www.makeuseof.com/stock-price-data-using-python/
        symbolInfo = yf.Ticker(str(self.symbol)).info
        self.currentPrice = symbolInfo['bid']

    def __init__(self, symbol, positions, avgCostPrice = -1):
        _assert.__init__(self, symbol, positions, avgCostPrice)
        self.whichMarket = "US"
        self.queryCurrentPrice()

class TWStockAssert(_assert):
    def queryCurrentPrice(self):
        return super().queryCurrentPrice()