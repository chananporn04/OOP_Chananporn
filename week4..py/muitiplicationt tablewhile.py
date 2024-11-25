number = int(input("ป้อนสูตรคูณ: "))
i = 1  
while i < 25:  
    b = number * i
    if (b / 2) % 2 != 0:
        print(f"{number} x {i} = {b}") 
    i += 1 