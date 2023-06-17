class book:
    def __init__(self):
        title=""
        publisher=""
        price=0
    def set(self, title, publisher, price):
        self.title= title
        self.publisher= publisher
        self.price=price
    def display(self):
        print("title:", self.title)
        print("publisher:", self.publisher)
        print("price:", self.price)
    def __gt__(self,b):
        if self.price>b.price:
            return True
        else:
            return False
b1=book()
b1.set("oops with c++", "LAXMAN UNIVERSITY", 1400)
b2=book()
b2.set("basics of c++", " pooji", 200)
if b1>b2:
    print("this book is about bilu ")
    b1.display()
    b2.display()