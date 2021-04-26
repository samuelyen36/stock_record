class stock:
    def __init__(self,read_or_new='r'):
        self.stock_list=[]      #a list of dictionary
        if read_or_new=='r':        #read from file
            print("read from file")
            with open("record.txt",'r') as f:
                while True:
                    _str = f.readline()
                    if not _str:
                        break
                    _str = _str.split(" ")
                    stock_dic = {"date" : _str[0], "id" : _str[1], "sell_buy" : _str[2], "amount" : _str[3], "unit_price" : _str[4], "total_price" : int(int(_str[3]) * float(_str[4]))}
                    self.stock_list.append(stock_dic)

        elif read_or_new=='n':      #create a new file
            print("please entry the transaction details with the following format: yyyy/mm/dd crop_id sell_or_sold amount unit_price total_price\nFor example: 2021/04/01 0050 sell 300 80\nexit with entering 0\n\n")
            while 1:
                _str = input()
                if _str=="0":
                    break
                _str = _str.split(" ")
                stock_dic = {"date" : _str[0], "id" : _str[1], "sell_buy" : _str[2], "amount" : _str[3], "unit_price" : _str[4], "total_price" : int(int(_str[3]) * float(_str[4]))}
                self.stock_list.append(stock_dic)


    def insert(self,entry):
            print("please entry the transaction details with the following format: yyyy/mm/dd crop_id sell_or_sold amount unit_price total_price\nFor example: 2021/04/01 0050 sell 300 80\nexit with entering 0\n\n")
            while 1:
                _str = input()
                if _str=="0":
                    break
                _str = _str.split(" ")
                stock_dic = {"date" : _str[0], "id" : _str[1], "sell_buy" : _str[2], "amount" : _str[3], "unit_price" : _str[4], "total_price" : int(int(_str[3]) * float(_str[4]))}
                self.stock_list.append(stock_dic)


    def list_all(self):
        print("date\tID\t買賣\tamount\t單位價格\t總價")
        for i in self.stock_list:
            if i['sell_buy'] == 'buy':
                _real_price = '-' + str(i['total_price'])
            else:
                _real_price = str(i['total_price'])
            print("{date}\t{id}\t{sell_buy}\t{amount}\t{unit_price}\t{total_price}\n".format(date = i['date'], id = i['id'], sell_buy = i['sell_buy'], amount = i['amount'], unit_price = i['unit_price'], total_price = _real_price ))


    def save_to_file(self):     #todo : do no save the identical(repeated) entry
        with open("record.txt","w+") as f:
            for i in self.stock_list:
                f.write("{date} {id} {sell_buy} {amount} {unit_price} {total_price}\n".format(date = i['date'], id = i['id'], sell_buy = i['sell_buy'], amount = i['amount'], unit_price = i['unit_price'], total_price = i['total_price'] ))

        print("finish saving the file\n")
    
    def check_bal(self):
        _filter = input("do you want to select a specific product? If yes, type the ID, otherwise, type 0 ")
        bal = 0
        if _filter == '0':    #no specific one
            print("no specifier")
            for i in self.stock_list:
                if i['sell_buy'] == 'buy':
                    tmp = int(i['total_price']) * -1
                else:
                    tmp = int(i['total_price'])
                bal = bal + tmp
        else:
            for i in self.stock_list:
                if i['id']==_filter:
                    if i['sell_buy'] == 'buy':
                        tmp = int(i['total_price']) * -1
                    else:
                        tmp = int(i['total_price'])
                    bal = bal + tmp
                else:
                    continue
        print("total balance is: {}".format(bal))



"""
dictionary with key: date,corp_id, sell_or_sold , amount, unit_price
"""

if __name__ == '__main__':
    opt = input("If you want to read from file, enter r; create a new record enter n: ")
    if opt=='r':
        _rec = stock(read_or_new='r')
    elif opt=='n':
        _rec = stock(read_or_new='n')

    while True:
        opt = input("save file: s\tlist entry: l\tadd new entry: i\tcheck balance: b\n")
        if opt=='s':
            _rec.save_to_file()
        if opt=='l':
            _rec.list_all()
        if opt=='i':
            _rec.insert()
        if opt=='b':
            _rec.check_bal()