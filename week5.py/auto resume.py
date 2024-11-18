myself = {}
resume = int(input("จำนวนคน :"))
for i in  range (1,resume+1):
    print(f"กรุณากรอกชื่อคนที่ {i} :")
    myself["nickname"] = str(input("กรุณากรอกชื่อเล่น : "))
    myself["stdid"] = str(input("กรุณากรอกเลขที่ : "))
    myself["hobby"] = str(input("กรุณากรอกงานอดิเรก : "))
    myself["color"] = str(input("กรุณากรอกสีที่ชอบ : "))
    print(f"ข้อมูลคนที่ {str(i)}\n{resume}")