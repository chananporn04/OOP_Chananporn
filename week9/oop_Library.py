class Library:
    def __init__(self):
        self.bookname = []
    def add_book(self):
        while True:
            choice = input("พิมพ์ add เพื่อเพิ่ม พิมพ์ exit เพื่อออก  : ")
            if choice == 'add':
                book = {}
                book['bname'] = str(input('ใส่ชื่อหนังสือ : '))
                book['writer'] = str(input('ใส่ชื่อผู้แต่ง : '))
                book['page'] = str(input('ใส่จำนวนหน้า :'))
                book['price'] = str(input('ใส่ราคา :'))
                self.bookname.append(book)
            elif choice == 'exit':
                break
    def show_books(self):
        print("รายชื่อหนังสือในห้องสมุด:")
        for show_book in self.bookname:
            print(show_book)
    def find_book(self):
        bookname = str(input('ค้นหาชื่อ:'))
        i = 0
        for i in self.bookname:
            if bookname == i['bookname']:
                print(i)
lib1 = Library()
lib1.add_book()
lib1.show_books()
lib1.find_book()