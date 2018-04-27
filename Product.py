from tkinter import *
from tkinter import ttk


class Product:
    prod_y = 80
    num_of_products = 0
    prod_to_delete = []

    def __init__(self, label, pic, name, date, num, endurance, price):
        self.label = label
        self.picture = pic
        self.name = name
        self.date = date
        self.num = num
        self.endurance = endurance
        self.price = price
        self.prod_cbox = []

    def delete_prod(self, num, delete):
        size = len(Product.prod_to_delete)
        if delete:
            Product.prod_to_delete.insert(size, num)
        else:
            Product.prod_to_delete.remove(num)

    def delete(self, label):
        print('d')

    def add_to_label(self, label):
        num = self.num_of_products
        delete = False
        prod_y = Product.prod_y
        checkbox = Checkbutton(label, width=1, bg='grey', variable=delete, onvalue=True, offvalue=False,
                               command=lambda: self.delete_prod(num, delete))
        checkbox.place(x=30, y=prod_y-5)
        Label(label, image=self.picture, bg='grey', font="Times 22").place(x=60, y=prod_y-25)
        Label(label, text=self.name, bg='grey', font="Times 22").place(x=150, y=prod_y)
        Label(label, text=self.date, bg='grey', font="Times 22").place(x=400, y=prod_y)
        Label(label, text=str(self.num), bg='grey', font="Times 22").place(x=570, y=prod_y)
        Label(label, text=str(self.endurance), bg='grey', font="Times 22").place(x=730, y=prod_y)
        Label(label, text=str(self.price), bg='grey', font="Times 22").place(x=870, y=prod_y)
        self.prod_cbox.insert(len(self.prod_cbox), ttk.Checkbutton(label, width=1))
        Product.prod_y += 80
        Product.num_of_products += 1
