class Cat:
    def __init__(self,cat_name,cat_color):
        self.name = cat_name
        self.color = cat_color
    def cry(self):
        print("เมี้ยวๆ")
mycat1 = Cat("ศรีทอง","สีส้ม")
mycat2 = Cat("ศรีเงิน","สีขาว")
print(mycat1.name)
print(mycat2.color)
mycat1.cry()