import xml.etree.ElementTree as ET
from _assert import *

class assertMgr():
    def __init__(self) -> None:
        self.totalAssert = []
        pass
    
    def dumpCurrentAssert(self) -> None:
        for item in self.totalAssert:
            item.dumpInfo()

    def parseIBKRPositions(self, xmlFileName = "positions.xml"):
        root = ET.parse(xmlFileName).getroot()
        date = ""
        for position in root.iter('OpenPosition'):
            #print(position.attrib)
            IBKRAssert = USStockAssert(position.attrib['symbol'], position.attrib['position'], position.attrib['costBasisPrice'])
            self.totalAssert.append(IBKRAssert)
        for FlexStatement in root.iter('FlexStatement'):
            #print(FlexStatement.attrib)
            date = FlexStatement.attrib['whenGenerated'].split(';')[0]
            print("report is generated at {}".format(date))