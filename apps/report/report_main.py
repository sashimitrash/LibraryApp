from tkinter import Label, Button, Frame
from PIL import Image, ImageTk
from apps.resources.variables import *


class Report:
    def __init__(self, root):
        self.root = root
        root.title('Report Main Menu')

        # container window, everything will be added to this container
        self.container = Frame(root, bg='black', width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
        self.container.grid()

        # background image, DOES NOT CHANGE DYNAMICALLY, so we do not allow prof to expand the window
        self.image = self.open_image('apps/resources/library_wallpaper.png', CANVAS_WIDTH, CANVAS_HEIGHT)
        self.background_image = Label(self.container, image=self.image)
        self.background_image.grid()

        # reports image
        self.report = self.open_image('apps/resources/reports.png', SIDE_IMAGE_WIDTH, SIDE_IMAGE_HEIGHT)
        # reinitialize because tkinter would destroy self.report variable after using it
        self.report_image  = Label(self.container, image=self.report)
        self.report_image .place(relx=SIDE_IMAGE_X, rely=SIDE_IMAGE_Y, anchor='center')
        self.report_text = Label(self.container, text='Reports', font=(FONT, FONT_SIZE, STYLE), fg='white', bg='black')
        self.report_text.place(relx=SIDE_TEXT_X, rely=SIDE_TEXT_Y, anchor='center')

        # title label
        self.label = Label(self.container, text='Select one of the options below:', fg='black', bg='#c5e3e5',
                           relief='raised', width=60, height=3)
        self.label.config(font=(FONT, FONT_SIZE, STYLE))
        self.label.place(relx=0.5, rely=0.09, anchor="center")  # label is always mid align

        # back to main_menu button
        self.return_btn = Button(self.container, text='Back to Main Menu', command=self.return_to_main_menu,
                                 bg='#c5e3e5', width=60, height=1, relief='raised', borderwidth=5)
        self.return_btn.config(font=(FONT, FONT_SIZE, STYLE))
        self.return_btn.place(relx=0.5, rely=0.9, anchor="center")  # return_btn is always mid align

        # Book on search button
        self.book_search = Button(self.container, text='11. Book Search', command=self.book_search,
                                  padx=55, pady=20, wraplength=200)
        self.book_search.config(font=(FONT, FONT_SIZE, STYLE), fg='white', bg='#17a1d5')
        self.book_search.place(relx=BUTTON_X, rely=0.16)

        # Books on Loan button
        self.book_loan = Button(self.container, text='12. Books on Loan', command=self.book_on_loan,
                                height=3, width=12, wraplength=200)
        self.book_loan.config(font=(FONT, FONT_SIZE, STYLE), fg='white', bg='#2964e7')
        self.book_loan.place(relx=BUTTON_X, rely=0.29)

        # Books on Reservation button
        self.book_reservation = Button(self.container, text='13. Books on Reservation', command=self.book_on_reservation,
                                       height=3, width=12, wraplength=200)
        self.book_reservation.config(font=(FONT, FONT_SIZE, STYLE), fg='white', bg='#4e3ddc')
        self.book_reservation.place(relx=BUTTON_X, rely=0.43)

        # Outstanding Fee button
        self.outstanding_fine_btn = Button(self.container, text='14. Outstanding Fines', command=self.outstanding_fine,
                                           height=3, width=12, wraplength=200)
        self.outstanding_fine_btn.config(font=(FONT, FONT_SIZE, STYLE), fg='white', bg='#8d29e7')
        self.outstanding_fine_btn.place(relx=BUTTON_X, rely=0.57)

        # Outstanding Fee button
        self.loan_to_member = Button(self.container, text='15. Books on Loan to Member', command=self.books_loan_to_member,
                                     height=3, width=12, wraplength=200)
        self.loan_to_member.config(font=(FONT, FONT_SIZE, STYLE), fg='white', bg='#ca17d5')
        self.loan_to_member.place(relx=BUTTON_X, rely=0.71)

    def open_image(self, image_path, resized_width, resized_height):
        path = image_path
        image = Image.open(path)
        resized_image = image.resize((resized_width, resized_height), Image.ANTIALIAS)
        resized_image = ImageTk.PhotoImage(resized_image)
        return resized_image

    def return_to_main_menu(self):
        print('returning to main menu')

    def book_search(self):
        print('Book search')

    def book_on_loan(self):
        print('Books on Loan')

    def book_on_reservation(self):
        print('Book on reservation')

    def outstanding_fine(self):
        print('Outstanding Fines')

    def books_loan_to_member(self):
        print('Books loan to members')

