import tkinter as tk
from tkinter import ttk
import os
import Saving_to_database

root = tk.Tk()


class Gui:

    count = 0

    def get_all_informations(self):
        label = tk.Label(frame, bg='gray', text='aaaaa')
        label.pack()

    def read_all(self):
        data = Saving_to_database.database.read_all_products()
        for record in data:
            my_tree.insert(parent='', index='end', iid=self.count,
                           values=(record[0], record[1], record[2]))
            self.count = + 1


gui = Gui()

root.geometry('1200x600')
canvas = tk.Canvas(root, width=1200, height=620, bg='#ff1111')
canvas.pack()

frame = tk.Frame(root, bg="#fff")
frame.place(relheight=0.80, relwidth=0.70, relx=0.01, rely=0.1)

frame2 = tk.Frame(root, bg="#fff")
frame2.place(relheight=0.8, relwidth=0.2, relx=0.78, rely=0.1)

my_tree = ttk.Treeview(frame)
my_tree['columns'] = ('ID', 'product', 'carat', 'barcode')

my_tree.column('#0', width=0, stretch=0)
my_tree.column('ID', width=200)
my_tree.column('product', width=200)
my_tree.column('carat', width=200)
my_tree.column('barcode', width=200)

my_tree.heading('#0', text='label')
my_tree.heading('ID', text='ID')
my_tree.heading('product', text="products")
my_tree.heading('carat', text="carat")
my_tree.heading('barcode', text="barcode")

my_tree.pack()

barcode_reader_button = tk.Button(frame2, text='Read Barcode',
                                  padx=10, pady=5, fg='white', bg="#263d42", command=gui.get_all_informations)
barcode_reader_button.pack()

read_all_button = tk.Button(frame2, text='Read All',
                            padx=10, pady=5, fg='white', bg="#263d42", command=gui.read_all)
read_all_button.pack()


class anotherShit(Gui):
    pass


root.mainloop()
