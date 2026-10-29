#oop

#book title, author, isbn, price

class Book:
    #constructor === basically a special function
    def __init__(self, title, author, isdn, price):
        self.title = title
        self.author = author
        self.isdn = isdn
        self.price = price
    def print_details(self):
        print("Title: ",self.title)
        print("Author: ",self.author)
        print("ISDN: ",self.isdn)
        print("Price: ",self.price)
        print("-----------------------")

    def apply_discount(self, discount ):
        self.price = self.price * (1 - discount/100)
        print("New price is ", self.price)

b1 = Book("Two rivers", "Chinua Achebe", "ISB001", 300)
b2 = Book("Think And Grow Rich", "John Moore", "ISB002", 700)
b1.print_details()
b1.apply_discount(10)
b1.print_details()