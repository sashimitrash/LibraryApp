from landing_page import LandingPage
from apps.resources.container import Container
from tkinter import Tk
from sqlalchemy import create_engine
import pymysql


class LibraryApp(Container):
    def __init__(self):
        USER = 'root'
        PASSWORD = 'Password1!'
        HOST = '127.0.0.1'
        PORT = 3306
        DATABASE = 'Library'

        self.engine = create_engine('mysql+pymysql://{0}:{1}@{2}:{3}/{4}'.format(
            USER, PASSWORD, HOST, PORT, DATABASE
        ))

        self.root = Tk()

        self.landing = LandingPage(self.root, self, self.engine)

        self.root.mainloop()

    def return_to_main_menu(self, child):
        LandingPage(self.root, self, self.engine)
        child.container.grid_forget()



app = LibraryApp()