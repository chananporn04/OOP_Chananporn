class Cat:
    def __init__(self,ชื่อ,อายุ,เพศ,สี):
        self.name = ชื่อ
        self.age = อายุ
        self.gender = เพศ
        self.color = สี
    def old(self):
        self.age +=1



cat1 = Cat(ชื่อ="ศรีทอง",อายุ=4,เพศ="เพศผู้",สี="สีดำ")
cat2 = Cat("ศรีทอง",5,"ตัวเมีย","สีขาว")
cat2.old()
print(cat2.age)