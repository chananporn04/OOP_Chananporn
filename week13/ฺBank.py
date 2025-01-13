class Bank:
    def __init__(self, id,name,balance):
        self.id = id
        self.name = name
        self.__balance = balance
    def Deposit(self,amount):
        if amount > 100:
            self.__balance += amount
        else:
            print("ใส่ยอดเงิน 100 บาทขึ้นไป")
    def outmonay(self,out):
        if out > 0 and out <= self.__balance:
            self.__balance -= out
        else:
            print("ใส่ยอดเงิน 100 บาทขึ้นไป")
    def check(self):
        return self.__balance
id1 = Bank(1,"นานา",5000)
id1.__balance += 5000
id1.outmonay(1000)
id1.check()
print(f'เงินของ {id1.name} มีจำนวน {id1.check()} บาท')