class Bank :
    def __init__(self,id,name,balance):
        self.id = id
        self.name = name
        self.balance = balance
    def deposit(self,amount):
        if amount >= 100 :
            self.balance += amount
        else:
            print('ใส่ยอดเงิน 100 บาทขึ้นไป')

id1 = Bank(1,"mint",5000)
id1.deposit(300)
print(f'เงินของ {id1.name} มีอยู่ {id1.balance} บาท')
