class Product:
    def __init__(self, product_name, product_price, product_stock):
        self._name = product_name
        self._price = product_price
        self._stock = product_stock

    def edit_stock(self):
        additional_stock = int(input("เพิ่มจำนวนสินค้า: "))
        self._stock += additional_stock

    def edit_price(self):
        new_price = int(input("แก้ไขราคาสินค้า: "))
        self._price = new_price

    def detail(self):
        return f"สินค้า {self._name} ราคา {self._price} บาท จำนวน {self._stock} ชิ้น"

class Phone(Product):
    def __init__(self, product_name, product_price, product_stock, phone_storage):
        super().__init__(product_name, product_price, product_stock)
        self.storage = phone_storage

    def show_phone(self):
        return f"{super().detail()} ความจุ {self.storage} GB"

class Laptop(Product):
    def __init__(self, product_name, product_price, product_stock, laptop_spec):
        super().__init__(product_name, product_price, product_stock)
        self.spec = laptop_spec

    def show_laptop(self):
        return f"{super().detail()} สเปค {self.spec}"

class Clothes(Product):
    def __init__(self, product_name, product_price, product_stock, clothes_size):
        super().__init__(product_name, product_price, product_stock)
        self.size = clothes_size

    def show_clothes(self):
        return f"{super().detail()} ไซส์ {self.size}"

phone1 = Phone("i15 pro", 35000, 20, 256)
print(phone1.show_phone())

laptop1 = Laptop("asus 15 pro", 25000, 5, "i5 12th rtx3050")
print(laptop1.show_laptop())

clothes1 = Clothes("dress", 200, 20, "M")
print(clothes1.show_clothes())

phone1.edit_stock()
phone1.edit_price()
print(phone1.show_phone())