from textwrap import wrap
from tkinter import *
from PIL import Image, ImageTk
from numpy import insert
from sqlalchemy import null, text, create_engine
from apps.resources.variables import *
from apps.resources.container import Container
from datetime import *

class Loan(Container):
    def __init__(self, root, parent, engine):
        super().__init__(root, 'Loan Main Menu')
        self.init_image()
        self.parent = parent
        self.engine = engine
        
        # loan image
        self.loan = self.open_image('apps/resources/loan.png', SIDE_IMAGE_WIDTH, SIDE_IMAGE_HEIGHT)
        # reinitialize because tkinter would destroy self.report variable after using it
        self.loan_image  = Label(self.container, image=self.loan)
        self.loan_image.place(relx=SIDE_IMAGE_X, rely=SIDE_IMAGE_Y, anchor='center')
        self.loan_text = Label(self.container, text='Loans', font=(FONT, FONT_SIZE, STYLE), fg='white', bg='black')
        self.loan_text.place(relx=SIDE_TEXT_X, rely=SIDE_TEXT_Y, anchor='center')

        # title label
        self.label = Label(self.container, text='Select one of the options below:', fg='black', bg='#c5e3e5',
                           relief='raised', width=60, height=3)
        self.label.config(font=(FONT, FONT_SIZE, STYLE))
        self.label.place(relx=HEADING_LABEL_X, rely=HEADING_LABEL_Y, anchor="center")  # label is always mid align

        # back to main_menu button
        self.return_btn = Button(self.container, text='Back to Main Menu', command=lambda: parent.return_to_main_menu(self),
                                 bg='#c5e3e5', width=60, height=1, relief='raised', borderwidth=5)
        self.return_btn.config(font=(FONT, FONT_SIZE, STYLE))
        self.return_btn.place(relx=0.5, rely=0.9, anchor="center")  # return_btn is always mid align
        

        # Book borrow button
        self.book_borrow = Button(self.container, text='6. Borrow', command=self.book_borrow,
                                  padx=55, pady=20, wraplength=200)
        self.book_borrow.config(font=(FONT, FONT_SIZE, STYLE), fg='white', bg='#17a1d5')
        self.book_borrow.place(relx=BUTTON_X, rely=0.16)

        # Book return button
        self.book_return = Button(self.container, text='7. Return', command=self.book_return,
                                height=3, width=12, wraplength=200)
        self.book_return.config(font=(FONT, FONT_SIZE, STYLE), fg='white', bg='#2964e7')
        self.book_return.place(relx=BUTTON_X, rely=0.29)

    def open_image(self, image_path, resized_width, resized_height):
        path = image_path
        image = Image.open(path)
        resized_image = image.resize((resized_width, resized_height), Image.ANTIALIAS)
        resized_image = ImageTk.PhotoImage(resized_image)
        return resized_image

    def book_borrow(self):
        Borrow(self.root, self.parent, self.engine)
        self.container.grid_forget()
    
    def book_return(self):
        Return(self.root, self.parent, self.engine)
        self.container.grid_forget()
        
class Borrow(Container):
    def __init__(self, root, parent, engine):
            super().__init__(root, 'Book Borrow')
            self.init_image()
            self.parent = parent
            self.engine = engine
            self.cursor = engine.connect()
            
            #Create title label
            self.label = Label(self.container, text='To Borrow a Book, Please Enter Information Below:', fg='black', bg='#2dccb6',
                           relief='raised', width=60, height=3)
            self.label.config(font=(FONT, FONT_SIZE, STYLE))
            self.label.place(relx=HEADING_LABEL_X, rely=HEADING_LABEL_Y, anchor="center")  # label is always mid align
            
            # back to loan_menu button
            self.back_btn = Button(self.container, text='Back to Loans Menu', command=self.go_to_loans,
                                 bg='#27c0ab', width=20, height=2, relief='raised', borderwidth=5,
                                 highlightthickness=4, highlightbackground="#eaba2d")
            self.back_btn.config(font=(FONT, FONT_SIZE, STYLE))
            self.back_btn.place(relx=0.7, rely=0.9, anchor="center")

            # borrow button
            self.borrow_btn = Button(self.container, text='Borrow Book', command=self.go_to_confirm,
                                 bg='#27c0ab', width=20, height=2, relief='raised', borderwidth=5,
                                 highlightthickness=4, highlightbackground="#eaba2d")
            self.borrow_btn.config(font=(FONT, FONT_SIZE, STYLE))
            self.borrow_btn.place(relx=0.3, rely=0.9, anchor="center")

            # Accession Number box
            self.AN_box = Label(self.container, text='Accession Number', bg='#1391c1', fg='white', height=3, width=20)
            self.AN_box.config(font=(FONT, FONT_SIZE, STYLE))
            self.AN_box.place(relx=MENU_LABEL_X, rely=0.23, anchor='center')
            self.AN_entry = Entry(self.container, font=(FONT, FONT_SIZE, STYLE))
            self.AN_entry.place(relx=REPORT_ENTRY_BOX_X, rely=0.23, anchor='center',
                               width=REPORT_ENTRY_BOX_WIDTH, height=REPORT_ENTRY_BOX_HEIGHT)
            
            # Membership ID box
            self.ID_box = Label(self.container, text='Membership ID', bg='#1391c1', fg='white', height=3, width=20)
            self.ID_box.config(font=(FONT, FONT_SIZE, STYLE))
            self.ID_box.place(relx=MENU_LABEL_X, rely=0.5, anchor='center')
            self.ID_entry = Entry(self.container, font=(FONT, FONT_SIZE, STYLE))
            self.ID_entry.place(relx=REPORT_ENTRY_BOX_X, rely=0.5, anchor='center',
                               width=REPORT_ENTRY_BOX_WIDTH, height=REPORT_ENTRY_BOX_HEIGHT)
            
            
    
    
    def go_to_confirm(self):
        
        #checking for missing or incomplete fields
        listOfEntrys = [self.AN_entry.get(), self.ID_entry.get()]
        if "" in listOfEntrys: #checks missing
            self.failed()
            #Back to borrow function button
            self.backBorrowButton = Button(self.container, text="Back to Borrow Function", padx=20, pady=20, 
             bg="#27c0ab",borderwidth=5, highlightthickness=4, highlightbackground="#ecb606", relief="raised", command=self.close_incompleteError)
            self.backBorrowButton.place(relx=0.6, rely=0.65, anchor="center")
        else:
            #Prompt
            self.popupPromptLabel = Label(self.container, text="Confirm Loan Details To \nBe Correct", 
            width = 40, height=15, anchor='n', font=(FONT,FONT_SIZE, STYLE), bg="#9ddd58", fg="#000000")
            self.popupPromptLabel.place(relx=0.5, rely=0.5, anchor='center')
            #AN Entry
            self.input_AN = Label(self.container, text=self.AN_entry.get())
            self.input_AN.place(relx=0.6, rely=0.3, anchor="center")
            #Book title Entry
            sql_statement = "SELECT title FROM books WHERE accession_no = '{}'".format(self.AN_entry.get())
            data_BT = self.cursor.execute(sql_statement).fetchall()[0][0]
            self.input_BT = Label(self.container, text=data_BT) 
            self.input_BT   .place(relx=0.6, rely=0.35, anchor="center")
            #Borrow date Entry
            self.input_BD = Label(self.container, text=date.today()) 
            self.input_BD.place(relx=0.6, rely=0.4, anchor="center")
            #Membership ID Entry
            self.input_ID = Label(self.container, text=self.ID_entry.get())
            self.input_ID.place(relx=0.6, rely=0.45, anchor="center")
            #Member name Entry
            sql_statement = "SELECT name FROM members WHERE memberid = '{}'".format(self.ID_entry.get())
            data_name = self.cursor.execute(sql_statement).fetchall()[0][0]
            self.input_name = Label(self.container, text=data_name)
            self.input_name.place(relx=0.6, rely=0.5, anchor="center")
            #Due Date Entry
            self.input_DD = Label(self.container, text=date.today() + timedelta(days=14))
            self.input_DD.place(relx=0.6, rely=0.55, anchor="center")
            #Labels
            self.AN_label = Label(self.container, text = "Accession Number:")
            self.AN_label.place(relx=0.4, rely=0.3, anchor="center")
            self.BT_label = Label(self.container, text = "Book Title:")
            self.BT_label.place(relx=0.4, rely=0.35, anchor="center")
            self.BD_label = Label(self.container, text = "Borrow Date:")
            self.BD_label.place(relx=0.4, rely=0.4, anchor="center")
            self.ID_label = Label(self.container, text = "Membership ID:")
            self.ID_label.place(relx=0.4, rely=0.45, anchor="center")
            self.name_label = Label(self.container, text = "Member Name:")
            self.name_label.place(relx=0.4, rely=0.5, anchor="center")
            self.DD_label = Label(self.container, text = "Due Date:")
            self.DD_label.place(relx=0.4, rely=0.55, anchor="center")
            #checking for missing or incomplete fields
            listOfEntrys = [self.AN_entry.get(), self.ID_entry.get()]
            if "" in listOfEntrys: #checks missing
                return self.failed()
    
            #Confirm Loan Button
            self.confirmLoanButton = Button(self.container, text="Confirm Loan", padx=20, pady=20, 
            command=self.go_to_error, bg="#27c0ab",borderwidth=5, highlightthickness=4, highlightbackground="#ecb606", relief="raised")
            self.confirmLoanButton.place(relx=0.4, rely=0.65, anchor="center")
             #Back to borrow function button
            self.backBorrowButton = Button(self.container, text="Back to Borrow Function", padx=20, pady=20, 
             bg="#27c0ab",borderwidth=5, highlightthickness=4, highlightbackground="#ecb606", relief="raised", command=self.close_confirmPage)
            self.backBorrowButton.place(relx=0.6, rely=0.65, anchor="center")
            
    def failed(self):   
        self.ErrorPop = Label(self.container, text='Error!\n\n Duplicate, Missing or\nIncomplete fields.',
        fg='yellow', bg='#FF0000',
        relief='raised', width=30, height=15)
        self.ErrorPop.config(font=(FONT, FONT_SIZE, STYLE))
        self.ErrorPop.place(relx=0.5, rely=0.4, anchor="center")
        self.ErrorPop.lift()  
    
    def close_incompleteError(self):
        self.ErrorPop.lower()
        self.backBorrowButton.lower()          
            
           
    def close_confirmPage(self):
        self.cursor = self.engine.connect()
        #Close confirmation page popup
        self.popupPromptLabel.lower()
        self.confirmLoanButton.lower()
        self.backBorrowButton.lower()
        self.input_AN.lower()
        self.input_BT.lower()
        self.input_BD.lower()
        self.input_ID.lower()   
        self.input_name.lower()
        self.input_DD.lower()
        self.AN_label.lower()
        self.BT_label.lower()
        self.BD_label.lower()
        self.ID_label.lower()
        self.name_label.lower()
        self.DD_label.lower()
    
    def go_to_error(self):
        self.cursor = self.engine.connect()
        #Close confirmation page popup
        self.popupPromptLabel.lower()
        self.confirmLoanButton.lower()
        self.backBorrowButton.lower()
        self.input_AN.lower()
        self.input_BT.lower()
        self.input_BD.lower()
        self.input_ID.lower()   
        self.input_name.lower()
        self.input_DD.lower()
        self.AN_label.lower()
        self.BT_label.lower()
        self.BD_label.lower()
        self.ID_label.lower()
        self.name_label.lower()
        self.DD_label.lower()
        
        for x in range(1):
            #Book out on loan error
            sql_statement = "SELECT BorrowedBookAccession FROM loan WHERE BorrowedBookAccession = '{}' AND ReturnedDate IS NULL".format(self.AN_entry.get())
            data_BookBorrowed = self.cursor.execute(sql_statement).fetchall()
            if len(data_BookBorrowed) > 0:
                self.go_to_borrowedError()
                break
            #Loan quota error
            sql_statement = "SELECT * FROM loan WHERE BorrowerID = '{}' AND ReturnedDate IS NULL".format(self.ID_entry.get())
            data_quota = self.cursor.execute(sql_statement).fetchall()
            if len(data_quota) >= 2:
                self.go_to_quotaError()
                break
            #Outstanding fine error
            sql_statement = "SELECT memberid FROM fine WHERE memberid = '{}'".format(self.ID_entry.get())
            data_fine = self.cursor.execute(sql_statement).fetchall()
            if len(data_fine) > 0:
                self.go_to_fineError()
                break
            sql_statement = "SELECT ReserverID, ReservedDate FROM reservation WHERE ReservedBookAccession = '{}' ORDER BY ReservedDate".format(self.AN_entry.get()) 
            data_reserveInfo = self.cursor.execute(sql_statement).fetchall()
            #if memberid matches reservedid and smallest reserved date matches reserverid
            if len(data_reserveInfo) > 0:
                if data_reserveInfo[0][0] == self.ID_entry.get():
                    sql_statement = "INSERT INTO loan(BorrowerID, BorrowedBookAccession, BorrowDate) VALUES('{}', '{}', '{}')".format(self.ID_entry.get(), self.AN_entry.get(), date.today())
                    self.cursor.execute(sql_statement)
                    sql_statement = "DELETE FROM reservation WHERE ReservedBookAccession = '{}' AND ReserverID = '{}'".format(self.AN_entry.get(), self.ID_entry.get())
                    self.cursor.execute(sql_statement)
                else:
                    self.go_to_reserveError()
            else:
                sql_statement = "INSERT INTO loan(BorrowerID, BorrowedBookAccession, BorrowDate) VALUES('{}', '{}', '{}')".format(self.ID_entry.get(), self.AN_entry.get(), date.today())
                self.cursor.execute(sql_statement)
    
    def go_to_reserveError(self):
        self.popupErrorLabel = Label(self.container, text="Error!\n\n Book currently reserved by another Member.", 
        fg='yellow', bg='#FF0000',
        relief='raised', width=30, height=15)
        self.popupErrorLabel.place(relx=0.5, rely=0.3, anchor="center")
        self.backBorrowButton = Button(self.container, text="Back to Borrow Function", padx=20, pady=20, 
            command=self.closeError, bg="#27c0ab",borderwidth=5, highlightthickness=4, highlightbackground="#ecb606", relief="raised")
        self.backBorrowButton.place(relx=0.5, rely=0.65, anchor="center")

    def go_to_borrowedError(self):
        sql_statement = "SELECT * FROM loan WHERE BorrowedBookAccession = '{}' AND ReturnedDate IS NULL".format(self.AN_entry.get())
        data_BookBorrowed = self.cursor.execute(sql_statement).fetchall()
        self.popupErrorLabel = Label(self.container, text="Error!\n\n Book currently on Loan until:\n" + str(data_BookBorrowed[0][2] + timedelta(days=14)), 
        fg='yellow', bg='#FF0000',
        relief='raised', width=30, height=15)
        self.popupErrorLabel.place(relx=0.5, rely=0.3, anchor="center")
        self.backBorrowButton = Button(self.container, text="Back to Borrow Function", padx=20, pady=20, 
            command=self.closeError, bg="#27c0ab",borderwidth=5, highlightthickness=4, highlightbackground="#ecb606", relief="raised")
        self.backBorrowButton.place(relx=0.5, rely=0.65, anchor="center")
    
    def go_to_quotaError(self):
        self.popupErrorLabel = Label(self.container, text="Error!\n\n Member loan quota exceeded.",
        fg='yellow', bg='#FF0000',
        relief='raised', width=30, height=15)
        self.popupErrorLabel.place(relx=0.5, rely=0.3, anchor="center")
        self.backBorrowButton = Button(self.container, text="Back to Borrow Function", padx=20, pady=20, 
            command=self.closeError, bg="#27c0ab",borderwidth=5, highlightthickness=4, highlightbackground="#ecb606", relief="raised")
        self.backBorrowButton.place(relx=0.5, rely=0.65, anchor="center")
    
    def go_to_fineError(self):
        self.popupErrorLabel = Label(self.container, text="Error!\n\n Member has outstanding fines.", 
        fg='yellow', bg='#FF0000',
        relief='raised', width=30, height=15)
        self.popupErrorLabel.place(relx=0.5, rely=0.3, anchor="center")
        self.backBorrowButton = Button(self.container, text="Back to Borrow Function", padx=20, pady=20, 
            command=self.closeError, bg="#27c0ab",borderwidth=5, highlightthickness=4, highlightbackground="#ecb606", relief="raised")
        self.backBorrowButton.place(relx=0.5, rely=0.65, anchor="center")

    def closeError(self):
        self.popupErrorLabel.lower()
        self.backBorrowButton.lower()
        
        
    
    def go_to_loans(self):
            Loan(self.root, self.parent, self.engine)
            self.container.grid_forget()  

class Return(Container):
    def __init__(self, root, parent, engine):
            super().__init__(root, 'Book Return')
            self.init_image()
            self.parent = parent
            self.engine = engine
            self.cursor = engine.connect()
            
            #Create title label
            self.label = Label(self.container, text='To Return a Book, Please Enter Information Below:', fg='black', bg='#2dccb6',
                           relief='raised', width=60, height=3)
            self.label.config(font=(FONT, FONT_SIZE, STYLE))
            self.label.place(relx=HEADING_LABEL_X, rely=HEADING_LABEL_Y, anchor="center")  # label is always mid align
            
            # back to loan_menu button
            self.back_btn = Button(self.container, text='Back to Loans Menu', command=self.go_to_loans,
                                 bg='#27c0ab', width=20, height=2, relief='raised', borderwidth=5,
                                 highlightthickness=4, highlightbackground="#eaba2d")
            self.back_btn.config(font=(FONT, FONT_SIZE, STYLE))
            self.back_btn.place(relx=0.7, rely=0.9, anchor="center")

            # return button
            self.return_btn = Button(self.container, text='Return Book', command=self.go_to_confirm,
                                 bg='#27c0ab', width=20, height=2, relief='raised', borderwidth=5,
                                 highlightthickness=4, highlightbackground="#eaba2d")
            self.return_btn.config(font=(FONT, FONT_SIZE, STYLE))
            self.return_btn.place(relx=0.3, rely=0.9, anchor="center")

            # Accession Number box
            self.AN_box = Label(self.container, text='Accession Number', bg='#1391c1', fg='white', height=3, width=20)
            self.AN_box.config(font=(FONT, FONT_SIZE, STYLE))
            self.AN_box.place(relx=MENU_LABEL_X, rely=0.23, anchor='center')
            self.AN_entry = Entry(self.container, font=(FONT, FONT_SIZE, STYLE))
            self.AN_entry.place(relx=REPORT_ENTRY_BOX_X, rely=0.23, anchor='center',
                               width=REPORT_ENTRY_BOX_WIDTH, height=REPORT_ENTRY_BOX_HEIGHT)
            
            # Return date box
            self.RD_box = Label(self.container, text='Return Date', bg='#1391c1', fg='white', height=3, width=20)
            self.RD_box.config(font=(FONT, FONT_SIZE, STYLE))
            self.RD_box.place(relx=MENU_LABEL_X, rely=0.5, anchor='center')
            self.RD_entry = Entry(self.container, font=(FONT, FONT_SIZE, STYLE))
            self.RD_entry.insert(0, (date.today()))
            self.RD_entry.place(relx=REPORT_ENTRY_BOX_X, rely=0.5, anchor='center',
                               width=REPORT_ENTRY_BOX_WIDTH, height=REPORT_ENTRY_BOX_HEIGHT)
            
    
    
    
        
        
        
    def go_to_confirm(self):
        #checking for missing or incomplete fields
        listOfEntrys = [self.AN_entry.get(), self.RD_entry.get()]
        if "" in listOfEntrys: #checks missing
            self.failed()
            #Back to return function button
            self.backReturnButton = Button(self.container, text="Back to Return Function", padx=20, pady=20, 
             bg="#27c0ab",borderwidth=5, highlightthickness=4, highlightbackground="#ecb606", relief="raised", command=self.close_incompleteError)
            self.backReturnButton.place(relx=0.6, rely=0.65, anchor="center")
        else:
            #Prompt
            self.popupPromptLabel = Label(self.container, text="Confirm Return Details To \nBe Correct", 
            width = 30, height=20, font=(FONT), anchor='n')
            self.popupPromptLabel.place(relx=0.5, rely=0.5, anchor='center')
            #AN Entry
            self.input_AN = Label(self.container, text=self.AN_entry.get())
            self.input_AN.place(relx=0.6, rely=0.3, anchor="center")
            #Book title Entry
            sql_statement = "SELECT title FROM books WHERE accession_no = '{}'".format(self.AN_entry.get())
            data_BT = self.cursor.execute(sql_statement).fetchall()[0][0]
            self.input_BT = Label(self.container, text=data_BT) 
            self.input_BT   .place(relx=0.6, rely=0.35, anchor="center")
            #Membership ID Entry
            sql_statement = "SELECT BorrowerID FROM loan WHERE BorrowedBookAccession = '{}'".format(self.AN_entry.get())
            data_ID = self.cursor.execute(sql_statement).fetchall()[0][0]
            self.input_ID = Label(self.container, text=data_ID) 
            self.input_ID.place(relx=0.6, rely=0.4, anchor="center")
            #Member name Entry
            sql_statement = "SELECT name FROM members WHERE memberid = '{}'".format(data_ID)
            data_name = self.cursor.execute(sql_statement).fetchall()[0][0]
            self.input_name = Label(self.container, text=data_name)
            self.input_name.place(relx=0.6, rely=0.45, anchor="center")
            #RD Label
            self.input_RD = Label(self.container, text=self.RD_entry.get())
            self.input_RD.place(relx=0.6, rely=0.5, anchor="center")
            #Fine Label
            sql_statement = "SELECT BorrowDate FROM loan WHERE BorrowedBookAccession = '{}'".format(self.AN_entry.get())
            data_BD = self.cursor.execute(sql_statement).fetchall()[0][0] 
            data_DD = data_BD + timedelta(days=14)
            if datetime.strptime(self.RD_entry.get(), '%Y-%m-%d').date() > data_DD:
                fine_amt = (datetime.strptime(self.RD_entry.get(), '%Y-%m-%d').date() - data_DD).days
            else:
                fine_amt = 0 
            
            self.input_fine = Label(self.container, text="$" + str(fine_amt))
            self.input_fine.place(relx=0.6, rely=0.55, anchor="center")
            #Labels
            self.AN_label = Label(self.container, text = "Accession Number:")
            self.AN_label.place(relx=0.4, rely=0.3, anchor="center")
            self.BT_label = Label(self.container, text = "Book Title:")
            self.BT_label.place(relx=0.4, rely=0.35, anchor="center")
            self.ID_label = Label(self.container, text = "Membership ID:")
            self.ID_label.place(relx=0.4, rely=0.4, anchor="center")
            self.name_label = Label(self.container, text = "Member Name:")
            self.name_label.place(relx=0.4, rely=0.45, anchor="center")
            self.RD_label = Label(self.container, text = "Return Date")
            self.RD_label.place(relx=0.4, rely=0.5, anchor="center")
            self.fine_label = Label(self.container, text = "Fine:")
            self.fine_label.place(relx=0.4, rely=0.55, anchor="center")

            #Confirm Return Button
            self.confirmReturnButton = Button(self.container, text="Confirm Return", padx=20, pady=20, 
            command=self.go_to_error, bg="#27c0ab",borderwidth=5, highlightthickness=4, highlightbackground="#ecb606", relief="raised")
            self.confirmReturnButton.place(relx=0.4, rely=0.65, anchor="center")
             #Back to borrow function button
            self.backBorrowButton = Button(self.container, text="Back to Borrow Function", padx=20, pady=20, 
             bg="#27c0ab",borderwidth=5, highlightthickness=4, highlightbackground="#ecb606", relief="raised", command=self.close_confirmPage)
            self.backBorrowButton.place(relx=0.6, rely=0.65, anchor="center")
            
    def failed(self):   
        self.ErrorPop = Label(self.container, text='Error!\n\n Duplicate, Missing or\nIncomplete fields.',
        fg='yellow', bg='#FF0000',
        relief='raised', width=30, height=15)
        self.ErrorPop.config(font=(FONT, FONT_SIZE, STYLE))
        self.ErrorPop.place(relx=0.5, rely=0.4, anchor="center")
        self.ErrorPop.lift()          

    def close_incompleteError(self):
        self.ErrorPop.lower()
        self.backReturnButton.lower()   
            
    def close_confirmPage(self):
        self.cursor = self.engine.connect()
        #Close confirmation page popup
        self.popupPromptLabel.lower()
        self.confirmReturnButton.lower()
        self.backBorrowButton.lower()
        self.input_AN.lower()
        self.input_BT.lower()
        self.input_ID.lower()   
        self.input_name.lower()
        self.input_RD.lower()
        self.input_fine.lower()
        
        self.AN_label.lower()
        self.BT_label.lower()
        self.ID_label.lower()
        self.name_label.lower()
        self.RD_label.lower()
        self.fine_label.lower()
    
    def go_to_error(self):
        self.cursor = self.engine.connect()
        #Close confirmation page popup
        self.popupPromptLabel.lower()
        self.confirmReturnButton.lower()
        self.backBorrowButton.lower()
        self.input_AN.lower()
        self.input_BT.lower()
        self.input_ID.lower()   
        self.input_name.lower()
        self.input_RD.lower()
        self.input_fine.lower()
        
        self.AN_label.lower()
        self.BT_label.lower()
        self.ID_label.lower()
        self.name_label.lower()
        self.RD_label.lower()
        self.fine_label.lower()
        
        #Update loan with return date
        sql_statement = "UPDATE loan SET ReturnedDate = '{}' WHERE BorrowedBookAccession = '{}'".format(self.RD_entry.get(), self.AN_entry.get())
        self.cursor.execute(sql_statement)
        #Find borrow date
        sql_statement = "SELECT BorrowDate FROM loan WHERE BorrowedBookAccession = '{}'".format(self.AN_entry.get())
        data_BD = self.cursor.execute(sql_statement).fetchall()[0][0] 
        data_DD = data_BD + timedelta(days=14)
        fine_amt =  (datetime.strptime(self.RD_entry.get(), '%Y-%m-%d').date() - data_DD).days
        if fine_amt > 0:
            self.go_to_fineError()
        
    def go_to_fineError(self):
        self.popupErrorLabel = Label(self.container, text="Error!\n\n Book returned successfully but has fines.", 
        fg='yellow', bg='#FF0000',
        relief='raised', width=30, height=15)
        #Find memberid
        sql_statement = "SELECT BorrowerID FROM loan WHERE BorrowedBookAccession = '{}'".format(self.AN_entry.get())
        data_ID = self.cursor.execute(sql_statement).fetchall()[0][0]
        sql_statement = "SELECT BorrowDate FROM loan WHERE BorrowedBookAccession = '{}'".format(self.AN_entry.get())
        data_BD = self.cursor.execute(sql_statement).fetchall()[0][0] 
        data_DD = data_BD + timedelta(days=14)
        fine_amt = (datetime.strptime(self.RD_entry.get(), '%Y-%m-%d').date() - data_DD).days
        self.popupErrorLabel.place(relx=0.5, rely=0.3, anchor="center")
        self.backBorrowButton = Button(self.container, text="Back to Borrow Function", padx=20, pady=20, 
            command=self.closeError, bg="#27c0ab",borderwidth=5, highlightthickness=4, highlightbackground="#ecb606", relief="raised")
        self.backBorrowButton.place(relx=0.5, rely=0.65, anchor="center")
        sql_statement = "SELECT * FROM fine WHERE memberid = '{}'".format(self.ID_entry.get())
        data_fine = self.cursor.execute(sql_statement).fetchall()
        if len(data_fine) == 0:
            sql_statement = "INSERT INTO fine(memberid, amount) VALUES('{}', {})".format(data_ID, fine_amt )
            self.cursor.execute(sql_statement)
        else:
            sql_statement = "UPDATE fine SET amount = amount + {} WHERE memberid = '{}'".format(fine_amt, self.ID_entry.get())
            self.cursor.execute(sql_statement)


    def closeError(self):
        self.popupErrorLabel.lower()
        self.backBorrowButton.lower()
        
    def go_to_loans(self):
            Loan(self.root, self.parent, self.engine)
            self.container.grid_forget()    


