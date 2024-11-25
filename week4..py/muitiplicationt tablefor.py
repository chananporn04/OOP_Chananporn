number = int(input("ป้อนสูตรคูณ: "))
for i in range(1, 25):  
    b = number * i
    if (b / 2) % 2 != 0:
     print(f"{number} x {i} = {b}") 