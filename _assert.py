import yfinance as yf

class _assert:
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
        self.logger.info("{}\t{}\t{}USD\t{}USD".format(self.whichMarket, self.symbol, self.currentPrice, self.currentPrice*self.positions))
        

class USStockAssert(_assert):
    def queryCurrentPrice(self):
        #https://www.makeuseof.com/stock-price-data-using-python/
        symbolInfo = yf.Ticker(str(self.symbol)).info
        self.currentPrice = float(symbolInfo['ask'])
        self.logger.info("Current price for {} is {}".format(self.symbol, self.currentPrice))

    def __init__(self, logger, symbol, positions, avgCostPrice = -1):
        _assert.__init__(self, logger, symbol, positions, avgCostPrice)
        self.whichMarket = "US"
        self.queryCurrentPrice()

class TWStockAssert(_assert):
    def queryCurrentPrice(self):
        return super().queryCurrentPrice()