import random

class Student:
    def __init__(self, name, nickname,score=0):

        self.name = name
        self.nickname = nickname
        self.score = score

    def take(self):

        self.score = random.randint(1, 10)

    def grade(self):
        if self.score >= 6:
            print(f"{self.nickname} สอบผ่าน\n------------------------------------")
        else:
            print(f"{self.nickname} สอบไม่ผ่าน\n-----------------------------------")



student1 = Student('ชนันพร พิมพ์เสนา', 'มิ้น')
student1.take()


student2 = Student('สุขใจ จิตดี', 'ดวง')  
student2.take()


student3 = Student('พิมพ์พา ระกา', 'สี')  
student3.take()


student4 = Student('สำเภา สีเพชร', 'จ๋า')  
student4.take()


student5 = Student('นาวา พิพับ', 'วาวา')  
student5.take()


allstd = [student1,student2,student3,student4,student5]
for i in allstd:
    print(f'นาย {i.name} ได้คะแนน : {i.score} คะแนน ')
    i.grade()