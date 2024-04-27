import yfinance as yf

#base class
class _asset:
    def __init__(self, logger, symbol, positions, avgCostPrice = -1.0):
        self.symbol = symbol
        self.positions: float = float(positions)
        self.avgCostPrice: float = float(avgCostPrice)
        self.currentPrice: float = -1.0
        self.whichMarket = ""
        self.currency = ""  #could be enum type
        self.logger = logger
    
    def queryCurrentPrice(self):
        pass

    def dumpInfo(self):
        self.logger.info("{}\t{}\t{}\t\t{:.2f}USD\t{:.2f}USD".format(self.whichMarket, self.symbol, self.positions, self.currentPrice, self.currentPrice*self.positions))

    def getDictInfo(self):
        resDict = {"market": self.whichMarket, "symbol": self.symbol, "positions": self.positions, "avgCost": self.avgCostPrice, "currency": self.currency}
        return resDict
        

class USStockasset(_asset):
    def queryCurrentPrice(self):
        #https://www.makeuseof.com/stock-price-data-using-python/
        symbolInfo = yf.Ticker(str(self.symbol)).info
        self.currentPrice = float(symbolInfo['ask'])
        self.logger.info("Current price for {} is {}".format(self.symbol, self.currentPrice))

    def __init__(self, logger, symbol, positions, avgCostPrice = -1):
        _asset.__init__(self, logger, symbol, positions, avgCostPrice)
        self.whichMarket = "US"
        self.queryCurrentPrice()
        self.currency = "USD"

class TWStockasset(_asset):
    def queryCurrentPrice(self):
        return super().queryCurrentPrice()