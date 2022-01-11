import tkinter as tk
import os
import Saving_to_database

root = tk.Tk()


class Gui:
    def get_all_informations(self):
        label = tk.Label(frame, bg='gray', text='aaaaa')
        label.pack()

    def read_all(self):
        data = Saving_to_database.database.read_all_products()
        label = tk.Label(frame, bg='gray', text=data)
        label.pack()


gui = Gui()

root.geometry('1200x600')
canvas = tk.Canvas(root, width=1200, height=620, bg='#ff1111')
canvas.pack()

frame = tk.Frame(root, bg="#fff")
frame.place(relheight=0.80, relwidth=0.70, relx=0.01, rely=0.1)

frame2 = tk.Frame(root, bg="#fff")
frame2.place(relheight=0.8, relwidth=0.2, relx=0.78, rely=0.1)

barcode_reader_button = tk.Button(frame2, text='Read Barcode',
                                  padx=10, pady=5, fg='white', bg="#263d42", command=gui.get_all_informations)
barcode_reader_button.pack()

read_all_button = tk.Button(frame2, text='Read All',
                            padx=10, pady=5, fg='white', bg="#263d42", command=gui.read_all)
read_all_button.pack()


class anotherShit(Gui):
    pass


root.mainloop()
