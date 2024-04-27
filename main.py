from assetMgr import assetMgr
import logging
import sys

def setUpLogger(levels = logging.INFO):
    logger = logging.getLogger("main")
    ch = logging.StreamHandler(sys.stdout)
    fmt = logging.Formatter('%(message)s')
    ch.setFormatter(fmt)
    ch.setLevel(levels)
    logger.addHandler(ch)
    logger.setLevel(levels)
    return logger


if __name__ == '__main__':
    logger = setUpLogger(logging.DEBUG)

    #logger.basicConfig(format='%(message)s', level=logger.DEBUG)
    mgr = assetMgr(logger)
    logger.info("Parsing IBKR positions")
    mgr.parseIBKRPositions()
    logger.info("Dump Protofolio")
    mgr.dumpProtofolio()

    mgr.dumpToJson()

    mgr.extractExchangeRate()
