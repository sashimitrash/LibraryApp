from sqlalchemy import create_engine
import tkinter as tk
from variables import *

class BookInsertionSuccess():
    def __init__(self, root):
        
        self.root = root
        root.title("Book aquisition success!")
        root.geometry('400x300')

        #Textbox
        mesage = '''Success! New book added into library'''

        success_box = tk.Text(root, width=60, height=20)
        success_box.pack(expand=True)
        success_box.insert('end', message)
        success_box.config(font=(FONT, FONT_SIZE, STYLE), fg='white', bg='#17a1d5')

        #main menu button
        home_btn = tk.Button(root, text='Back to Acquisition Function', command=self.root.destroy,
                                 bg='#c5e3e5', width=5, height=1, relief='raised', borderwidth=5)
        home_btn.config(font=(FONT, FONT_SIZE, STYLE))
        home_btn.place(relx=0.5, rely=0.7, anchor="center")  # return_btn is always mid align
