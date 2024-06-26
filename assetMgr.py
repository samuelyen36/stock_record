import xml.etree.ElementTree as ET
from _asset import *
import requests
import json

class assetMgr():
    def __init__(self, logger) -> None:
        self.protofolio = []       #stores different types of asset, US stock, TW stock or funds
        self.exchangeRateUStoTW: float = 0.0
        self.logger = logger
    
    def dumpProtofolio(self) -> None:
        self.logger.info("Market\tSymbol\tPositions\tCurrentPrice\tCurrentValue\n")
        for item in self.protofolio:
            item.dumpInfo()

    def parseIBKRPositions(self, xmlFileName = "positions.xml"):
        root = ET.parse(xmlFileName).getroot()
        date = ""
        for position in root.iter('OpenPosition'):
            if(position.attrib['listingExchange'] not in ["NYSE", "NASDAQ", "ARCA"]):
                self.logger.info("{} not US asset, exhanges at {}".format(position.attrib['symbol'], position.attrib['listingExchange']))
                continue
            IBKRasset = USStockasset(self.logger, position.attrib['symbol'], position.attrib['position'], position.attrib['costBasisPrice'])
            self.logger.debug("add symbol: {}, position: {}, costPrice: {}".format(position.attrib['symbol'], position.attrib['position'], position.attrib['costBasisPrice']))
            self.protofolio.append(IBKRasset)
        for FlexStatement in root.iter('FlexStatement'):
            #self.logger.debug(FlexStatement.attrib)
            date = FlexStatement.attrib['whenGenerated'].split(';')[0]
            self.logger.debug("report is generated at {}".format(date))

    def extractExchangeRate(self):
        #reference: https://steam.oxxostudio.tw/category/python/spider/exchange.html
        url = 'https://rate.bot.com.tw/xrt/flcsv/0/day'
        rate = requests.get(url)
        rate.encoding = 'utf-8'
        rt = rate.text
        rts = rt.split('\n')
        a = rts[1].split(',')  #information of USD
        if(a[0] != "USD"):
            self.logger.error("wrong currency exchange rate is extracted({} is extracted), error out".format(a[0]))
            return
        self.exchangeRateUStoTW = float(a[12])
        self.logger.info("exchange rate of {otherCurrency} is 1 {otherCurrency} to {rate}TWD".format(otherCurrency=a[0], rate=self.exchangeRateUStoTW))
        
    def dumpToJson(self, filename = "protofolio.json"):
        dictList = []
        for item in self.protofolio:
            itemDict = item.getDictInfo()
            dictList.append(itemDict)
        with open(filename, 'w+') as f:
           json.dump(dictList, f)
        pass
