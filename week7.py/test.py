try:
    num = int(input('ใส่แม่สูตรคูณ'))
    if num == 0:
        raise Exception
    for i in range(1,13,1):
        print(f'{num} x {i} = {num*i}')
except ValueError:
    print('ใส่เฉพาะตัวเลข')
except:
    print('ห้ามใส่ 0 ')
