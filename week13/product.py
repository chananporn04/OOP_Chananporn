class Product:
    def __init__(self):
        self.product_data = {}

    def add_product(self):
        print("----- เพิ่มสินค้า -----")
        Mint_products = int(input("คุณต้องการเพิ่มสินค้ากี่รายการ? : "))
        for i in range(Mint_products):
            product_name = input("กรอกชื่อสินค้า: ")
            product_price = int(input("กรอกราคาสินค้า: "))
            product_stock = int(input("กรอกจำนวนสินค้าในสต็อก: "))
            self.product_data[product_name] = (product_price, product_stock)

    def show_products(self):
        if not self.product_data:
            print("ไม่มีสินค้าขายในตอนนี้.")
        else:
            print("----- ข้อมูลสินค้า -----")
            for product_name, product_info in self.product_data.items():
                product_price, product_stock = product_info
                print(f"ชื่อสินค้า: {product_name} | ราคา: {product_price} | จำนวนในสต็อก: {product_stock}")

    def restock_product(self):
        print("----- เพิ่มจำนวนสินค้าในสต็อก -----")
        product_name = input("กรอกชื่อสินค้าที่ต้องการเพิ่มจำนวนในสต็อก: ")
        if product_name in self.product_data:
            additional_quantity = int(input("กรอกจำนวนที่ต้องการเพิ่ม: "))
            product_price, product_stock = self.product_data[product_name]
            self.product_data[product_name] = (product_price, product_stock + additional_quantity)
            print(f"อัพเดตสต็อกเรียบร้อย. สต็อกใหม่ของ {product_name}: {product_stock + additional_quantity}")
        else:
            print("ไม่พบสินค้าในระบบ.")

    def reduce_product_stock(self):
        print("----- ลดจำนวนสินค้าในสต็อก -----")
        product_name = input("กรอกชื่อสินค้าที่ต้องการลดจำนวนในสต็อก: ")
        if product_name in self.product_data:
            reduce_quantity = int(input("กรอกจำนวนที่ต้องการลด: "))
            product_price, product_stock = self.product_data[product_name]
            if reduce_quantity <= product_stock:
                self.product_data[product_name] = (product_price, product_stock - reduce_quantity)
                print(f"อัพเดตสต็อกเรียบร้อย. สต็อกใหม่ของ {product_name}: {product_stock - reduce_quantity}")
            else:
                print("ข้อผิดพลาด: จำนวนในสต็อกไม่พอที่จะลด.")
        else:
            print("ไม่พบสินค้าในระบบ.")

    def update_product_price(self):
        print("----- อัพเดตราคาสินค้า -----")
        product_name = input("กรอกชื่อสินค้าที่ต้องการอัพเดตราคา: ")
        if product_name in self.product_data:
            new_price = int(input("กรอกราคาใหม่: "))
            product_price, product_stock = self.product_data[product_name]
            self.product_data[product_name] = (new_price, product_stock)
            print(f"อัพเดตราคาเรียบร้อย. ราคาสินค้าใหม่ของ {product_name}: {new_price}")
        else:
            print("ไม่พบสินค้าในระบบ.")

store1 = Product()

store1.add_product()
store1.show_products()
store1.restock_product()
store1.show_products()
store1.reduce_product_stock()
store1.show_products()
store1.update_product_price()
store1.show_products()