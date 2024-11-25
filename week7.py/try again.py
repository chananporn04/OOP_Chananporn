sum = 0
while True:
 try:
    product = input('ใส่ราคาสินค้า : ')
    if product == 'exit':  
            print(f"ยอดขายทั้งหมด {sum} บาท")
            break
    product = int(product)
    if product == 0 :
       raise ZeroDivisionError
    elif product < 0:
       raise Exception
    else:
        sum += product
        print (sum)
 except  ZeroDivisionError:
    print('ราคาสินค้าต้องมากกว่า 0 ') 
 except ValueError:
    print('ใส่ตัวเลขตัวเลขเท่านั้น')
 except:
    print('ห้ามใส่ราคาสินค้าติดลบ')