from cgitb import text
import tkinter as tk
from tkinter import Entry, Label, Toplevel, ttk
import os
from tkinter import messagebox
from tkinter import font
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
                           values=(record[0], record[1], record[2], record[3]))
            self.count = + 1

    def double_selected_item(self, event):
        global pop
        pop = Toplevel(root)
        pop.title('Uyari')
        pop.geometry('250x250')

        selected = my_tree.focus()
        tk.Label(pop, text='Sectiginiz Satiri Degistirmek Istiyor musunuz??').grid()

        button_yes = tk.Button(pop, text='Yes',
                               fg='white', bg="#263d42", command=lambda: self.choice("yes"))
        button_yes.grid(row=0, column=1)
        button_no = tk.Button(pop, text='No',
                              fg='white', bg="#263d42", command=lambda: self.choice("no"))
        button_no.grid(row=0, column=2)

    def choice(self, choosen):
        if choosen == "yes":
            messagebox.showinfo('yes dedin')

        else:
            messagebox.showinfo('no dedin')


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

my_tree = ttk.Treeview(frame)
my_tree['columns'] = ('ID', 'product', 'carat', 'barcode')


my_tree.column('#0', width=0, stretch=0)
my_tree.column('ID', width=200, anchor=tk.CENTER)
my_tree.column('product', width=200, anchor=tk.CENTER)
my_tree.column('carat', width=200, anchor=tk.CENTER)
my_tree.column('barcode', width=200, anchor=tk.CENTER)

my_tree.heading('#0', text='label')
my_tree.heading('ID', text='ID')
my_tree.heading('product', text="products")
my_tree.heading('carat', text="carat")
my_tree.heading('barcode', text="barcode")
my_tree.bind("<Double-1>", gui.double_selected_item)

my_tree.pack()

barcode_reader_button = tk.Button(frame2, text='Read Barcode', width=30,
                                  padx=10, pady=5, fg='white', bg="#263d42", command=gui.get_all_informations)
barcode_reader_button.pack()

read_all_button = tk.Button(frame2, text='Read All', width=30,
                            padx=10, pady=5, fg='white', bg="#263d42", command=gui.read_all)
read_all_button.pack()



class anotherShit(Gui):
    pass


root.mainloop()
