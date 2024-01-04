from _assert import _assert, USStockAssert
from assertMgr import assertMgr


if __name__ == '__main__':
    """
    tmp = USStockAssert("VT", 1.0, 1.0)
    tmp.queryCurrentPrice()
    tmp = USStockAssert("PFE", 1.0, 1.0)
    tmp.queryCurrentPrice()
    """
    mgr = assertMgr()
    mgr.parseIBKRPositions()
    mgr.dumpCurrentAssert()
