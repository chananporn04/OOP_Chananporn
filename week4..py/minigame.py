import random
scorewin = 0 
scorelose = 0
scoreallow= 0
while True :
 ai = random.choice(['ค้อน', 'กรรไกร', 'กระดาษ'])
 print("เลือก ค้อน กรรไกร หรือ กระดาษ")
 player = input("คุณเลือก: ")  

 print(f"สุ้ม: {ai}")
 print(f"คุณเลือก: {player}")

 if ai == player:
    print("ผลลัพธ์คือ เสมอ!")
    scoreallow+= 1
 elif (ai == 'ค้อน' and player == 'กรรไกร') :
    print("ผลลัพธ์คือ คุณแพ้!") 
    scorelose += 1
 elif (ai == 'กรรไกร' and player == 'กระดาษ') :
    print("ผลลัพธ์คือ คุณแพ้!") 
    scorelose += 1
 elif (ai == 'กระดาษ' and player == 'ค้อน'):
    print("ผลลัพธ์คือ คุณแพ้!")
    scorelose += 1
 elif (ai == 'กระดาษ' and player == 'กรรไกร'):   
    print("ผลลัพธ์คือ คุณชนะ!")
    scorewin += 1
 elif (ai == 'กรรไกร' and player == 'ค้อน'):
    print("ผลลัพธ์คือ คุณชนะ!")
    scorewin += 1
 elif (ai == 'ค้อน' and player == 'กระดาษ'):
    print("ผลลัพธ์คือ คุณชนะ!")  
    scorewin += 1
 elif player == 'หยุด':
    print("ออกแล้ว")  
    print(f'ผลลัพธ์การ ชนะ : {scorewin} \nผลลัพธ์การ แพ้ : {scorelose} \nผลลัพธ์การ เสมอ {scorelose}')
    break
 else:
    print("กรุณาเลือกให้ถูกต้อง (ค้อน, กรรไกร, หรือ กระดาษ)")