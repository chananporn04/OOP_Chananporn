try:  
    num = int(input("ใส่ยอด : "))  
    if num == 0:
        raise ZeroDivisionError()
    elif num < 0 :
        raise Exception()
    elif num >= 5000:
        mint =  num * 0.2
        mint1 = num - mint
        print(f"20% Discount = {mint} num = {mint1}")
    elif num >= 2000:
        mint =  num * 0.1
        mint1 = num - mint
        print(f"10% Discount = {mint} num = {mint1}")
    else:
        print("คุณไม่ได้รับส่วนลด")
except ValueError:
    print("ใส่เฉพาะตัวเลข")
except ZeroDivisionError:
    print("ห้ามใส่ 0")
except:
    print("ห้ามใส่ค่าติดลบ")