from tkinter import Tk, Frame, Label, Button
from PIL import Image, ImageTk
from apps.report.report_main import Report
from apps.resources.variables import *


LANDING_PAGE_ICON_SIZE = 300
LANDING_PAGE_FONT_SIZE = 40

class LandingPage:
    def __init__(self, root):
        self.root = root
        root.title('Library System Landing Page')

        # container window, everything will be added to this container
        self.container = Frame(root, bg='white', width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
        self.container.grid()

        # reports option
        self.report_image = self.open_image('apps/resources/reports.png', LANDING_PAGE_ICON_SIZE, LANDING_PAGE_ICON_SIZE)
        self.report_button = Button(root, image=self.report_image, command=self.go_to_report)
        self.report_button.place(relx=0.7, rely=0.7, anchor='center')
        self.report_text = Label(root, text='Reports', font=(FONT, LANDING_PAGE_FONT_SIZE, STYLE), fg='black', bg='white')
        self.report_text.place(relx=0.7, rely=0.9, anchor='center')

    def open_image(self, image_path, resized_width, resized_height):
        path = image_path
        image = Image.open(path)
        resized_image = image.resize((resized_width, resized_height), Image.ANTIALIAS)
        resized_image = ImageTk.PhotoImage(resized_image)
        return resized_image

    def go_to_report(self):
        report_gui = Report(root)
        self.container.grid_forget()

        print('go to report')


root = Tk()
landing_page = LandingPage(root)
root.mainloop()