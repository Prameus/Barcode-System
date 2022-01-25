from itertools import product
import tkinter as tk
from tkinter import Entry, Label, Toplevel, ttk
import os
from tkinter import messagebox
from tkinter import font
from turtle import width

from matplotlib.pyplot import text
import Saving_to_database

root = tk.Tk()


class Gui:

    count = 0

    def get_all_informations(self):
        label = tk.Label(self.frame, bg='gray', text='aaaaa')
        label.pack()

    def read_all(self):
        data = Saving_to_database.database.read_all_products()
        for record in data:
            my_tree.insert(parent='', index='end', iid=self.count,
                           values=(record[0], record[1], record[2], record[3]))
            self.count = self.count + 1

# database`den cektigim bilgileri durmadan geliyor ve 1 2 , 1 2 olarak durmadan dusuyor?

    def delete_row(self):
        selected = my_tree.focus()
        Saving_to_database.database.delete_product(selected)

    def add_product(self):
        selected = my_tree.focus()
        values = my_tree.item(selected, 'values')
        self.pop_screen(values)

    def pop_screen(self, values):
        global product_entry, carat_entry, barcode_entry, pop

        pop = Toplevel(root)
        pop.title('Uyari')
        pop.geometry('350x230')

        product_label = Label(pop, text='Product:')
        product_label.grid(column=0, row=0, ipady=20,)
        product_entry = Entry(pop)
        product_entry.grid(column=1, row=0, sticky=tk.W)

        carat_label = Label(pop, text='Carat:')
        carat_label.grid(column=0, row=1, ipady=20, sticky=tk.W)
        carat_entry = Entry(pop, width=15)
        carat_entry.grid(column=1, row=1, sticky=tk.W)

        barcode_label = Label(pop, text='Barcode:')
        barcode_label.grid(column=0, row=2, ipady=20, sticky=tk.W)
        barcode_entry = Entry(pop, width=40)
        barcode_entry.grid(column=1, row=2)

        approve = tk.Button(pop, text='Approve', width=5,
                            padx=10, pady=5, fg='white', bg="#263d42", command=self.approve_values_add)
        approve.grid(column=0, row=5, padx=40)

        cancel = tk.Button(pop, text='Cancel', width=5,
                           padx=10, pady=5, fg='white', bg="#263d42", command=self.cancel_process)
        cancel.grid(column=1, row=5)

    def selected_item(self, event):
        global selected, values

        selected = my_tree.focus()
        values = my_tree.item(selected, 'values')
        self.pop_screen()

        product_entry.insert(0, values[1])
        carat_entry.insert(0, values[2])
        barcode_entry.insert(0, values[3])

    def approve_values_update(self):
        product_entry_info = product_entry.get()
        carat_entry_info = int(carat_entry.get())
        barcode_entry_info = int(barcode_entry.get())

        Saving_to_database.database.update_product(
            'product', product_entry_info, selected)
        Saving_to_database.database.update_product(
            'carat', carat_entry_info, selected)
        Saving_to_database.database.update_product(
            'barcode', barcode_entry_info, selected)

    def approve_values_add(self):
        product_entry_info = product_entry.get()
        carat_entry_info = int(carat_entry.get())
        barcode_entry_info = int(barcode_entry.get())

        Saving_to_database.database.adding_product(
            (self.count + 1), product_entry_info, carat_entry_info, barcode_entry_info)

    def cancel_process(self):
        pop.destroy()

    def clear_all(self):
        for i in my_tree.get_children():
            my_tree.delete(i)
        Saving_to_database.database.clear_all()


gui = Gui()

root.geometry('1200x600')
canvas = tk.Canvas(root, width=1200, height=620, bg='#ff1')
canvas.pack()

style = ttk.Style()
style.configure("Treeview",
                foreground='blue',
                rowheight=25,
                fieldbackground='silver')
style.configure('Treeview.Heading', font=(None, 12, font.ROMAN),)
style.configure('Treeview.Column', font=(None, 12, font.ITALIC),)

style.map('Treeview', background=[('selected', 'green')])

frame = tk.Frame(root, bg="#fff")
frame.place(relheight=0.80, relwidth=0.70, relx=0.01, rely=0.1)

frame2 = tk.Frame(root, bg="#fff")
frame2.place(relheight=0.8, relwidth=0.2, relx=0.78, rely=0.1)

my_tree = ttk.Treeview(frame, height=15)

my_tree['columns'] = ('ID', 'product', 'carat', 'barcode')

my_tree.column('#0', width=0, stretch=0)
my_tree.column('ID', width=180, anchor=tk.CENTER)
my_tree.column('product', width=180, anchor=tk.CENTER)
my_tree.column('carat', width=200, anchor=tk.CENTER)
my_tree.column('barcode', width=200, anchor=tk.CENTER)

my_tree.heading('#0', text='label')
my_tree.heading('ID', text='ID')
my_tree.heading('product', text="products")
my_tree.heading('carat', text="carat")
my_tree.heading('barcode', text="barcode")
my_tree.bind("<Double-1>", gui.selected_item)

my_tree.pack()

barcode_reader_button = tk.Button(frame2, text='Read Barcode', width=30,
                                  padx=10, pady=5, fg='white', bg="#263d42", command=gui.get_all_informations)
barcode_reader_button.pack()

read_all_button = tk.Button(frame2, text='Read All', width=30,
                            padx=10, pady=5, fg='white', bg="#263d42", command=gui.read_all)
read_all_button.pack()

delete_button = tk.Button(frame2, text='Delete', width=30,
                          padx=10, pady=5, fg='white', bg="#263d42", command=gui.delete_row)
delete_button.pack()

adding_button = tk.Button(frame2, text='Add Product', width=30,
                          padx=10, pady=5, fg='white', bg="#263d42", command=gui.add_product)
adding_button.pack()

clear_all_button = tk.Button(frame2, text='Clear All', width=30,
                             padx=10, pady=5, fg='white', bg="#263d42", command=gui.clear_all)
clear_all_button.pack()

root.mainloop()
