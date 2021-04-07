
class stock:
    def __init__(self,read_or_new='r'):
        self.stock_list=[]
        if read_or_new=='r':
            print("read from file")

        elif read_or_new=='n':
            print("please entry the transaction details with the following format: yyyy/mm/dd crop_id sell_or_sold amount unit_price total_price\nFor example: 2021/04/01 0050 sell 300 80\nexit with entering 0\n\n")
            while 1:
                _str = input()
                if _str=="0":
                    break
                _str = _str.split(" ")
                stock_dic = {"date" : _str[0], "id" : _str[1], "sell_sold" : _str[2], "amount" : _str[3], "unit_price" : _str[4], "total_price" : int(int(_str[3]) * float(_str[4]))}
                self.stock_list.append(stock_dic)


    def insert(self,entry):
        self.stock_list.append(entry)

"""
dictionary with key: date,corp_id, sell_or_sold , amount, unit_price
"""

if __name__ == '__main__':
    opt = input("If you want to read from file, enter r; create a new record enter n: ")
    if opt=='r':
        _rec = stock(read_or_new='r')
    elif opt=='n':
        _rec = stock(read_or_new='n')
