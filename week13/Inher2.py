class Animal:
    def __init__(self,name,age,color):
        self.name = name
        self.age = age
        self.color = color
    def showinfo(self):
        return f"ชื่อ {self.name} อายุ {self.age} ปี  มีสี {self.color}"

class Dog(Animal):
    def __init__(self, name, age, color,race):
        super().__init__(name, age, color)
        self.race = race
    def showdog(self):
        return f"หมาพันธ์ุ {self.race} มี {super().showinfo()}"
dog1 = Dog('ปีเตอร์',5,'ดำ',"หลังอาน")
print(dog1.showdog())

        