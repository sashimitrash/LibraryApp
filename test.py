from tkinter import Label, Button, Tk
from PIL import Image, ImageTk
from apps.resources.variables import *
from apps.resources.container import Container
from apps.report.report_pages import Report
from apps.report.search import BookSearch

from sqlalchemy import create_engine
import pandas as pd
import pymysql




class testestest(Container):
    def __init__(self):
        USER = 'kctey'
        PASSWORD = 'CQu1FxSp'
        HOST = '127.0.0.1'
        PORT = 3306
        DATABASE = 'Library'

        engine = create_engine('mysql+pymysql://{0}:{1}@{2}:{3}/{4}'.format(
            USER, PASSWORD, HOST, PORT, DATABASE
        ))

        self.root = Tk()

        self.landing = BookSearch(self.root, self, engine)

        self.root.mainloop()



app = testestest()