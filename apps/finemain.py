import tkinter as tk
from apps.resources.variables import *
from apps.resources.container import Container
import datetime as dt


class FineLandingPage(Container):
    def __init__(self, root, parent, engine):
        super().__init__(root, "Fine Menu")
        self.init_image()
        self.parent = parent
        self.engine = engine

        #book image
        self.book = self.open_image('apps/resources/fine.png', SIDE_IMAGE_WIDTH, SIDE_IMAGE_HEIGHT)
        self.book_image  = tk.Label(self.container, image=self.book)
        self.book_image.place(relx=SIDE_IMAGE_X, rely=SIDE_IMAGE_Y, anchor='center')

        #instructions
        instructions = tk.Label(self.container, text='Select one of the options below:', fg='black', bg='#cceae9',
                           relief='raised', width=60, height=3)
        instructions.config(font=(FONT, FONT_SIZE, STYLE))
        instructions.place(relx=HEADING_LABEL_X, rely=HEADING_LABEL_Y, anchor="center")

        #payment button
        payment_btn = tk.Button(self.container, command = lambda:[self.container.grid_forget(), FinePayment(root, self.parent, self.engine)],
                                   text="10.Fine Payment", fg='white', bg='#17a1d5', height=3, width=20, wraplength=200)
        payment_btn.config(font=(FONT, FONT_SIZE, STYLE))
        payment_btn.place(relx=0.55, rely=0.5)

        #main menu button
        home_btn = tk.Button(self.container, text='Back to Main Menu',
                            command=lambda: parent.return_to_main_menu(self),
                             bg='#cceae9', width=60, height=1, relief='raised',
                             borderwidth=5, highlightthickness=4, highlightbackground="#eaba2d")
        home_btn.config(font=(FONT, FONT_SIZE, STYLE))
        home_btn.place(relx=0.55, rely=0.9, anchor="center")


class FinePayment(Container):
    def __init__(self, root, parent, engine):
        super().__init__(root, "Fine Payment Menu")
        self.init_image()
        self.root = root
        self.parent = parent
        self.engine = engine
        self.cursor = self.engine.connect()

        #Instructions
        self.instructions = tk.Label(self.container, text='To Pay a Fine, Please Enter Information Below:',
                                 fg='black', bg='#2dccb6', relief='raised', width=60, height=3)
        self.instructions.config(font=(FONT, FONT_SIZE, STYLE))
        self.instructions.place(relx=HEADING_LABEL_X, rely=HEADING_LABEL_Y, anchor="center")

        #membership id
        self.membership = tk.Label(self.container, text = "Membership ID",  bg='#1391c1', fg='white', height=3, width=20)
        self.membership.config(font=(FONT, FONT_SIZE, STYLE))
        self.membership.place(relx=MENU_LABEL_X, rely=0.3, anchor="center")

        self.e1 = tk.Entry(self.container, font=(FONT, FONT_SIZE, STYLE))
        self.e1.place(relx=REPORT_ENTRY_BOX_X, rely=0.3, anchor='center',
                               width=REPORT_ENTRY_BOX_WIDTH, height=REPORT_ENTRY_BOX_HEIGHT)
        
        #payment date
        self.PaymentDate = tk.Label(self.container, text = "Payment Date", bg='#1fa4df', fg='white', height=3, width=20)
        self.PaymentDate.config(font=(FONT, FONT_SIZE, STYLE))
        self.PaymentDate.place(relx=MENU_LABEL_X, rely=0.43, anchor='center')

        self.TodayDate = dt.datetime.today().strftime('%Y-%m-%d')

        self.e2 = tk.Entry(self.container, font=(FONT, FONT_SIZE, STYLE))
        self.e2.insert(0, self.TodayDate)
        self.e2.place(relx=REPORT_ENTRY_BOX_X, rely=0.43, anchor='center',
                               width=REPORT_ENTRY_BOX_WIDTH, height=REPORT_ENTRY_BOX_HEIGHT)
        

        #payment amount
        self.PaymentAmount = tk.Label(self.container, text = "Payment Amount", bg='#49abde', fg='white', height=3, width=20)
        self.PaymentAmount.config(font=(FONT, FONT_SIZE, STYLE))
        self.PaymentAmount.place(relx=MENU_LABEL_X, rely=0.56, anchor='center')

        self.e3 = tk.Entry(self.container, font=(FONT, FONT_SIZE, STYLE))
        self.e3.place(relx=REPORT_ENTRY_BOX_X, rely=0.56, anchor='center',
                               width=REPORT_ENTRY_BOX_WIDTH, height=REPORT_ENTRY_BOX_HEIGHT)

        #pay fine
        self.pay = tk.Button(self.container, text='Pay Fine',
                        command=self.FinePay,
                        bg='#27c0ab', width=20, height=2, relief='raised', borderwidth=5,
                                 highlightthickness=4, highlightbackground="#eaba2d")
        self.pay.config(font=(FONT, FONT_SIZE, STYLE))
        self.pay.place(relx=0.3, rely=0.9, anchor="center")

        #home
        self.home2_btn = tk.Button(root, text='Back to Fines Menu',
                             command=lambda:[self.container.grid_forget(), FineLandingPage(self.root, self.parent, self.engine)],
                             bg='#27c0ab', width=20, height=2, relief='raised', borderwidth=5,
                                 highlightthickness=4, highlightbackground="#eaba2d")
        self.home2_btn.config(font=(FONT, FONT_SIZE, STYLE))
        self.home2_btn.place(relx=0.7, rely=0.9, anchor="center")

    def FinePay(self):
        self.MemberID = self.e1.get()
        self.Date = self.e2.get()
        self.PaymentAmt = self.e3.get()
        
        #confirmation text box
        self.confirm = tk.Label(self.container,
                                text= "Please Confirm Details to Be Correct:",
                                bg =popup_bg, fg=popup_font_color, width=35, height=2)
        self.confirm.config(font=(FONT, FONT_SIZE, STYLE))
        self.confirm.place(relx=0.5, rely=0.3, anchor="center")

        #MemberID label
        txt = "Member ID: {}\nPayment Date: {}\nPayment Amount: {}\n (Exact Fee Only)".format(self.MemberID, self.Date, self.PaymentAmt)
        self.MemberIDLabel = tk.Label(self.container, text=txt, bg =popup_bg, fg=popup_font_color, width=35, height=12)
        self.MemberIDLabel.config(font=(FONT,FONT_SIZE, STYLE))
        self.MemberIDLabel.place(relx=0.5, rely=0.55, anchor="center")
        
        #confirm payment button
        self.confirm_btn = tk.Button(self.container, text='Confirm Delete', padx=10, pady=10,
                                    command=self.canpay, bg='#27c0ab', borderwidth=5, relief='raised', highlightthickness=4, highlightbackground='#fae420')
        self.confirm_btn.config(font=(FONT,20,STYLE))
        self.confirm_btn.place(relx=0.4, rely=0.7, anchor='center')

        #back to fine button
        self.return_btn = tk.Button(self.container, text="Back to Payment Function", padx=10, pady=10,
                                    command=self.CloseConfirmPage,
                                    bg='#27c0ab', borderwidth=5, relief='raised', highlightthickness=4, highlightbackground='#fae420')
        self.return_btn.config(font=(FONT,20,STYLE), wraplength=300)
        self.return_btn.place(relx=0.6, rely=0.7, anchor='center')


    def canpay(self):
        self.MemberID = self.e1.get()
        self.PaymentAmt = self.e3.get()
        
        #sql code there to check if member has fine/ whether payment amount correct/ success
        sql_statement = "SELECT * FROM fine WHERE memberid = %s"
        data_fine = self.cursor.execute(sql_statement,(self.MemberID,)).fetchall()
        if len(data_fine) > 0: #whether member has fine
            actual_amount = data_fine[0][1]
            if actual_amount == int(self.PaymentAmt): #whether payment amount correct
                return self.SQLPay()
            else:
                return self.incorrectamt()
        else:
            return self.nofine()
        
        
    #SQL queries to delete fine
    def SQLPay(self):
        self.CloseConfirmPage()
        self.MemberID = self.e1.get()
        self.Date = self.e2.get()

        #delete from fine
        sql_statement3 = "DELETE FROM fine WHERE memberid = %s"
        self.cursor.execute(sql_statement3, (self.MemberID,))
        
        sql_statement4 = "INSERT INTO payment VALUES (%s, %s)"
        self.cursor.execute(sql_statement4, (self.MemberID, self.Date))

    def nofine(self):
        self.CloseConfirmPage()
        self.ErrorPop = tk.Label(self.container, text='Error! Member has no fine.', fg="#ffff00", bg="#cc0505",
                                width=40, height=15, wraplength=450)
        self.ErrorPop.config(font=(FONT,FONT_SIZE, STYLE))
        self.ErrorPop.place(relx=0.5, rely=0.5, anchor="center")

        #back to payment button
        self.back_btn = tk.Button(self.container, text='Back to Payment Function',
                                  command=self.CloseErrorPage, padx=20, pady=20,
                                    bg='#27c0ab', borderwidth=5, relief='raised', highlightthickness=4, highlightbackground='#fae420')
        self.back_btn.config(font=(FONT, FONT_SIZE, STYLE))
        self.back_btn.place(relx=0.5, rely=0.7, anchor="center")

    def incorrectamt(self):
        self.CloseConfirmPage()
        self.ErrorPop = tk.Label(self.container, text='Error! Incorrect fine payment amount', fg="#ffff00", bg="#cc0505",
                                width=40, height=15, wraplength=450)
        self.ErrorPop.config(font=(FONT,FONT_SIZE, STYLE))
        self.ErrorPop.place(relx=0.5, rely=0.5, anchor="center")

        #back to payment button
        self.back_btn = tk.Button(self.container, text='Back to Payment Function',
                                  command=self.CloseErrorPage, padx=20, pady=20,
                                    bg='#27c0ab', borderwidth=5, relief='raised', highlightthickness=4, highlightbackground='#fae420')
        self.back_btn.config(font=(FONT, FONT_SIZE, STYLE))
        self.back_btn.place(relx=0.5, rely=0.7, anchor="center")

    #close Error page
    def CloseErrorPage(self):
        self.ErrorPop.lower()
        self.back_btn.lower()
        
    #close Confirmation Page
    def CloseConfirmPage(self):
        self.MemberIDLabel.lower()
        self.confirm.lower()
        self.return_btn.lower()
        self.confirm_btn.lower()

    def ClosePayPopup(self):
        self.instructions.lower()
        self.membership.lower()
        self.e1.lower()
        self.PaymentDate.lower()
        self.e2.lower()
        self.PaymentAmount.lower()
        self.e3.lower()
        self.pay.lower()
        self.home2_btn.lower()
        
        

