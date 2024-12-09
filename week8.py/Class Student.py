class Student:
    def __init__(self,name,id):
        self.name = name
        self.id = id
        self.grader = {}
    def score(self):
        choice = input("กรุณาเลือกวิชาที่จะกรอกคะแนน : ")
        score = int(input("ใส่คะแนน"))
        grade = self.grade(score)
        if choice == "M":
            self.grader["Math"] = grade
        elif choice == "T":
            self.grader["Thai"] = grade
        elif choice == "S":
            self.grader["Sci"] = grade
    def grade(self,score):
        if score >= 80:
            return 4
        elif score >= 70:
            return 3
        elif score >= 60:
            return 2
        elif score >= 50:
            return 1
        else:
            return 0
std1 = Student("WooMee",10)
std1.score()
print(std1.grader)