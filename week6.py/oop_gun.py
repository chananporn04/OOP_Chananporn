class Gun:
    def __init__(self,name,ammo,hp):
        self.ชื่อ = name
        self.กระสุน = ammo
        self.พลังชีวิต = hp
    def add_ammo(self,ammo):
        self.กระสุน += ammo
    def fire_ammo(self):
        if self.กระสุน > 0:
            self.กระสุน -=1
        else:
            print('กระสุนหมด')
    def fire_gun(self,enemy):
        self.กระสุน -= 1
        enemy.พลังชีวิต -= 3
        
gun1 = Gun("T1",5,10)
gun2 = Gun("T2",10,5)
gun2.fire_gun(gun1)
print(gun1.กระสุน)
print(gun2.พลังชีวิต)