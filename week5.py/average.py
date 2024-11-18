tostop = int(input("ป้อนกี่ตัว : "))
Numm = []
for i in range (1,tostop+1):
    num = int(input(f"ป้อนตัวที่ {i} "))
    Numm.append(num)
    print(Numm)
print(f"ค่าเฉลี่ยของ {Numm} คือ : {sum(Numm)/len(Numm)}")