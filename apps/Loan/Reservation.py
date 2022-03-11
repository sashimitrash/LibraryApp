from tkinter import *
from PIL import Image, ImageTk
from apps.resources.variables import *
from apps.resources.container import Container
from datetime import *

class Reservation(Container):
    def __init__(self, root, parent, engine):
        super().__init__(root, 'Reservation Main Menu')
        self.init_image()
        self.parent = parent
        self.engine = engine
        
        # reservations image
        self.reservation = self.open_image('apps/resources/reservation.png', SIDE_IMAGE_WIDTH, SIDE_IMAGE_HEIGHT)
        # reinitialize because tkinter would destroy self.report variable after using it
        self.reservation_image  = Label(self.container, image=self.reservation)
        self.reservation_image .place(relx=SIDE_IMAGE_X, rely=SIDE_IMAGE_Y, anchor='center')
        self.reservation_text = Label(self.container, text='Reservations', font=(FONT, FONT_SIZE, STYLE), fg='white', bg='black')
        self.reservation_text.place(relx=SIDE_TEXT_X, rely=SIDE_TEXT_Y, anchor='center')
        
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

        # Book reserve button
        self.book_reserve = Button(self.container, text='8. Reserve a Book', command=self.book_reserve,
                                  height=3, width=20,wraplength=200)
        self.book_reserve.config(font=(FONT, FONT_SIZE, STYLE), fg='white', bg='#17a1d5')
        self.book_reserve.place(relx=0.55, rely=0.35)

        # Book cancel button
        self.cancel = Button(self.container, text='9. Cancel Reservation', command=self.cancel,
                                height=3, width=20, wraplength=200)
        self.cancel.config(font=(FONT, FONT_SIZE, STYLE), fg='white', bg='#2964e7')
        self.cancel.place(relx=0.55, rely=0.55)

    def open_image(self, image_path, resized_width, resized_height):
        path = image_path
        image = Image.open(path)
        resized_image = image.resize((resized_width, resized_height), Image.ANTIALIAS)
        resized_image = ImageTk.PhotoImage(resized_image)
        return resized_image

    def book_reserve(self):
        Reserve(self.root, self.parent, self.engine)
        self.container.grid_forget()
    
    def cancel(self):
        Cancel(self.root, self.parent, self.engine)
        self.container.grid_forget()
        
class Reserve(Container):
    def __init__(self, root, parent, engine):
            super().__init__(root, 'Book Reserve')
            self.init_image()
            self.parent = parent
            self.engine = engine
            self.cursor = engine.connect()
            
            #Create title label
            self.label = Label(self.container, text='To Reserve a Book, Please Enter Information Below:', fg='black', bg='#2dccb6',
                           relief='raised', width=60, height=3)
            self.label.config(font=(FONT, FONT_SIZE, STYLE))
            self.label.place(relx=HEADING_LABEL_X, rely=HEADING_LABEL_Y, anchor="center")  # label is always mid align
            
            # back to reservation_menu button
            self.back_btn = Button(self.container, text='Back to Reservations Menu', command=self.go_to_reservations,
                                 bg='#27c0ab', width=25, height=2, relief='raised', borderwidth=5,
                                   wraplength=600, highlightthickness=4, highlightbackground="#eaba2d")
            self.back_btn.config(font=(FONT, FONT_SIZE, STYLE))
            self.back_btn.place(relx=0.7, rely=0.9, anchor="center")

            # reserve button
            self.reserve_btn = Button(self.container, text='Reserve Book', command=self.go_to_confirm,
                                 bg='#27c0ab', width=20, height=2, relief='raised', borderwidth=5,
                                 highlightthickness=4, highlightbackground="#eaba2d")
            self.reserve_btn.config(font=(FONT, FONT_SIZE, STYLE))
            self.reserve_btn.place(relx=0.3, rely=0.9, anchor="center")

            # Accession Number box
            self.AN_box = Label(self.container, text='Accession Number', bg='#1391c1', fg='white', height=3, width=20)
            self.AN_box.config(font=(FONT, FONT_SIZE, STYLE))
            self.AN_box.place(relx=MENU_LABEL_X, rely=0.35, anchor='center')
            self.AN_entry = Entry(self.container, font=(FONT, FONT_SIZE, STYLE))
            self.AN_entry.place(relx=REPORT_ENTRY_BOX_X, rely=0.35, anchor='center',
                               width=REPORT_ENTRY_BOX_WIDTH, height=REPORT_ENTRY_BOX_HEIGHT)
            
            # Membership ID box
            self.ID_box = Label(self.container, text='Membership ID', bg='#49abde', fg='white', height=3, width=20)
            self.ID_box.config(font=(FONT, FONT_SIZE, STYLE))
            self.ID_box.place(relx=MENU_LABEL_X, rely=0.48, anchor='center')
            self.ID_entry = Entry(self.container, font=(FONT, FONT_SIZE, STYLE))
            self.ID_entry.place(relx=REPORT_ENTRY_BOX_X, rely=0.48, anchor='center',
                               width=REPORT_ENTRY_BOX_WIDTH, height=REPORT_ENTRY_BOX_HEIGHT)
            
            # Reserve date box
            self.RD_box = Label(self.container, text='Reserve Date', bg='#96c4e3', fg='white', height=3, width=20)
            self.RD_box.config(font=(FONT, FONT_SIZE, STYLE))
            self.RD_box.place(relx=MENU_LABEL_X, rely=0.61, anchor='center')
            self.RD_entry = Entry(self.container, font=(FONT, FONT_SIZE, STYLE))
            self.RD_entry.insert(0, (date.today()))
            self.RD_entry.place(relx=REPORT_ENTRY_BOX_X, rely=0.61, anchor='center',
                               width=REPORT_ENTRY_BOX_WIDTH, height=REPORT_ENTRY_BOX_HEIGHT)

    def go_to_confirm(self):
            #incomplete entry error
            listOfEntrys = [self.AN_entry.get(), self.ID_entry.get(), self.RD_entry.get()]
            if "" in listOfEntrys: #checks missing
                self.failed()
                #Back to reserve function button
                self.backReserveButton = Button(self.container, text="Back to Reserve Function", padx=20, pady=20, 
                                                bg="#27c0ab",borderwidth=5, highlightthickness=4, highlightbackground="#ecb606",
                                                relief="raised", command=self.close_incompleteError,
                                                font=(FONT, FONT_SIZE, STYLE))
                self.backReserveButton.place(relx=0.5, rely=0.7, anchor="center")
            else:
                #Prompt
                self.popupPromptLabel = Label(self.container, text="Confirm Reservation Details To \nBe Correct", 
                width = 40, height=16, font=(FONT, FONT_SIZE, STYLE), anchor='n', bg='#9ddd58')
                self.popupPromptLabel.place(relx=0.5, rely=0.5, anchor='center')
                #AN Label
                self.input_AN = Label(self.container, text=self.AN_entry.get(), font=(FONT, FONT_SIZE, STYLE), bg='#9ddd58')
                self.input_AN.place(relx=0.6, rely=0.35, anchor="center")
                #Book title Label
                sql_statement = "SELECT title FROM books WHERE accession_no = '{}'".format(self.AN_entry.get(), bg='#9ddd58')
                data_BT = self.cursor.execute(sql_statement).fetchall()[0][0]
                self.input_BT = Label(self.container, text=data_BT, font=(FONT, FONT_SIZE, STYLE), bg='#9ddd58')
                self.input_BT.place(relx=0.6, rely=0.42, anchor="center")
                #Membership ID Label
                self.input_ID = Label(self.container, text=self.ID_entry.get(), font=(FONT, FONT_SIZE, STYLE), bg='#9ddd58')
                self.input_ID.place(relx=0.6, rely=0.49, anchor="center")
                #Member name Label
                sql_statement = "SELECT name FROM members WHERE memberid = '{}'".format(self.ID_entry.get(), bg='#9ddd58')
                data_name = self.cursor.execute(sql_statement).fetchall()[0][0]
                self.input_name = Label(self.container, text=data_name, font=(FONT, FONT_SIZE, STYLE), bg='#9ddd58')
                self.input_name.place(relx=0.6, rely=0.56, anchor="center")
                #Reserve date Label
                self.input_RD = Label(self.container, text=self.RD_entry.get(), font=(FONT, FONT_SIZE, STYLE), bg='#9ddd58')
                self.input_RD.place(relx=0.6, rely=0.63, anchor="center")

                #Labels
                self.AN_label = Label(self.container, text = "Accession Number:", font=(FONT, FONT_SIZE, STYLE), bg='#9ddd58')
                self.AN_label.place(relx=0.45, rely=0.35, anchor="center")
                self.BT_label = Label(self.container, text = "Book Title:", font=(FONT, FONT_SIZE, STYLE), bg='#9ddd58')
                self.BT_label.place(relx=0.45, rely=0.42, anchor="center")
                self.ID_label = Label(self.container, text = "Membership ID:", font=(FONT, FONT_SIZE, STYLE), bg='#9ddd58')
                self.ID_label.place(relx=0.45, rely=0.49, anchor="center")
                self.name_label = Label(self.container, text = "Member Name:", font=(FONT, FONT_SIZE, STYLE), bg='#9ddd58')
                self.name_label.place(relx=0.42, rely=0.56, anchor="center")
                self.RD_label = Label(self.container, text = "Reserve Date", font=(FONT, FONT_SIZE, STYLE), bg='#9ddd58')
                self.RD_label.place(relx=0.45, rely=0.63, anchor="center")
            

                #Confirm Reservation Button
                self.confirmReservationButton = Button(self.container, text="Confirm Reservation", padx=20, pady=20,
                                                wraplength=300,
                                                command=self.go_to_error, bg="#27c0ab",borderwidth=5, highlightthickness=4,
                                                highlightbackground="#ecb606", relief="raised", font=(FONT, FONT_SIZE, STYLE))
                self.confirmReservationButton.place(relx=0.37, rely=0.73, anchor="center")
                #Back to reserve function button
                self.backBorrowButton = Button(self.container, text="Back to Reserve Function", padx=20, pady=20,
                                                wraplength=400,
                                                bg="#27c0ab",borderwidth=5, highlightthickness=4,
                                               highlightbackground="#ecb606", relief="raised",
                                               command=self.close_confirmPage, font=(FONT, FONT_SIZE, STYLE))
                self.backBorrowButton.place(relx=0.6, rely=0.73, anchor="center")

    def failed(self):   
        self.ErrorPop = Label(self.container, text='Error!\n\n Duplicate, Missing or\nIncomplete fields.',
        fg='yellow', bg='#cc0505',
        relief='raised', width=30, height=15)
        self.ErrorPop.config(font=(FONT, FONT_SIZE, STYLE))
        self.ErrorPop.place(relx=0.5, rely=0.5, anchor="center")

    def close_incompleteError(self):
        self.ErrorPop.lower()
        self.backReserveButton.lower()  
           
    def close_confirmPage(self):
        self.cursor = self.engine.connect()
        #Close confirmation page popup
        self.popupPromptLabel.lower()
        self.confirmReservationButton.lower()
        self.backBorrowButton.lower()
        self.input_AN.lower()
        self.input_BT.lower()
        self.input_ID.lower()   
        self.input_name.lower()
        self.input_RD.lower()
        
        self.AN_label.lower()
        self.BT_label.lower()
        self.ID_label.lower()
        self.name_label.lower()
        self.RD_label.lower()
        
    
    def go_to_error(self):
        self.cursor = self.engine.connect()
        #Close confirmation page popup
        self.popupPromptLabel.lower()
        self.confirmReservationButton.lower()
        self.backBorrowButton.lower()
        self.input_AN.lower()
        self.input_BT.lower()
        self.input_ID.lower()   
        self.input_name.lower()
        self.input_RD.lower()
        
        self.AN_label.lower()
        self.BT_label.lower()
        self.ID_label.lower()
        self.name_label.lower()
        self.RD_label.lower()
        
        for x in range(1):
            #Reservation quota error
            sql_statement = "Select ReserverID FROM reservation WHERE ReserverID = '{}'".format(self.ID_entry.get())
            data_BookReserved = self.cursor.execute(sql_statement).fetchall()
            if len(data_BookReserved) >= 2:
                self.go_to_quotaError()
                break
            #Outstanding fine error
            sql_statement = "Select amount FROM fine WHERE memberid = '{}'".format(self.ID_entry.get())
            data_fine = self.cursor.execute(sql_statement).fetchall()
            if len(data_fine) > 0:
                self.go_to_fineError()      
                break
            sql_statement = "INSERT INTO reservation(ReserverID, ReservedBookAccession, ReservedDate) VALUES('{}', '{}', '{}')".format(self.ID_entry.get(), self.AN_entry.get(), self.RD_entry.get())
            self.cursor.execute(sql_statement)       
    
    
    def go_to_quotaError(self):
        self.popupErrorLabel = Label(self.container, text="Error!\n\n Member currently has 2 Books on Reservation.",
        fg='yellow', bg='#FF0000',
        relief='raised', width=30, height=15)
        self.popupErrorLabel.place(relx=0.5, rely=0.3, anchor="center")
        self.backReserveButton = Button(self.container, text="Back to Reserve Function", padx=20, pady=20, 
            command=self.closeError, bg="#27c0ab",borderwidth=5, highlightthickness=4, highlightbackground="#ecb606", relief="raised")
        self.backReserveButton.place(relx=0.5, rely=0.7, anchor="center")
    
    def go_to_fineError(self):
        sql_statement = "Select amount FROM fine WHERE memberid = '{}'".format(self.ID_entry.get())
        data_fine = self.cursor.execute(sql_statement).fetchall()
        total_fine = 0
        for x in range(len(data_fine)):
            total_fine += data_fine[x][0]
        print(total_fine)
        
        self.popupErrorLabel = Label(self.container, text="Error!\n\n Member has outstanding Fine of:\n ${}".format(total_fine), 
        fg='yellow', bg='#FF0000',
        relief='raised', width=30, height=15)
        self.popupErrorLabel.place(relx=0.5, rely=0.3, anchor="center")
        self.backBorrowButton = Button(self.container, text="Back to Borrow Function", padx=20, pady=20, 
            command=self.closeError, bg="#27c0ab",borderwidth=5, highlightthickness=4, highlightbackground="#ecb606", relief="raised")
        self.backBorrowButton.place(relx=0.5, rely=0.7, anchor="center")

    def closeError(self):
        self.popupErrorLabel.lower()
        self.backBorrowButton.lower()

    def go_to_reservations(self):
            Reservation(self.root, self.parent, self.engine)
            self.container.grid_forget()  

class Cancel(Container):
    def __init__(self, root, parent, engine):
            super().__init__(root, 'Cancel Reservation')
            self.init_image()
            self.parent = parent
            self.engine = engine
            self.cursor = engine.connect()
            
            #Create title label
            self.label = Label(self.container, text='To Cancel a Reservation, Please Enter Information Below:', fg='black', bg='#2dccb6',
                           relief='raised', width=60, height=3)
            self.label.config(font=(FONT, FONT_SIZE, STYLE))
            self.label.place(relx=HEADING_LABEL_X, rely=HEADING_LABEL_Y, anchor="center")  # label is always mid align
            
            # back to reservations_menu button
            self.back_btn = Button(self.container, text='Back to Reservations Menu', command=self.go_to_reservations,
                                 bg='#27c0ab', width=25, height=2, relief='raised', borderwidth=5,
                                   wraplength=600,
                                 highlightthickness=4, highlightbackground="#eaba2d")
            self.back_btn.config(font=(FONT, FONT_SIZE, STYLE))
            self.back_btn.place(relx=0.7, rely=0.9, anchor="center")

            # return button
            self.cancel_btn = Button(self.container, text='Cancel Reservation', command=self.go_to_confirm,
                                 bg='#27c0ab', width=20, height=2, relief='raised', borderwidth=5,
                                 highlightthickness=4, highlightbackground="#eaba2d")
            self.cancel_btn.config(font=(FONT, FONT_SIZE, STYLE))
            self.cancel_btn.place(relx=0.3, rely=0.9, anchor="center")

            # Accession Number box
            self.AN_box = Label(self.container, text='Accession Number', bg='#1391c1', fg='white', height=3, width=20)
            self.AN_box.config(font=(FONT, FONT_SIZE, STYLE))
            self.AN_box.place(relx=MENU_LABEL_X, rely=0.35, anchor='center')
            self.AN_entry = Entry(self.container, font=(FONT, FONT_SIZE, STYLE))
            self.AN_entry.place(relx=REPORT_ENTRY_BOX_X, rely=0.35, anchor='center',
                               width=REPORT_ENTRY_BOX_WIDTH, height=REPORT_ENTRY_BOX_HEIGHT)
            
            # Membership ID box
            self.ID_box = Label(self.container, text='Membership ID', bg='#1391c1', fg='white', height=3, width=20)
            self.ID_box.config(font=(FONT, FONT_SIZE, STYLE))
            self.ID_box.place(relx=MENU_LABEL_X, rely=0.48, anchor='center')
            self.ID_entry = Entry(self.container, font=(FONT, FONT_SIZE, STYLE))
            self.ID_entry.place(relx=REPORT_ENTRY_BOX_X, rely=0.48, anchor='center',
                               width=REPORT_ENTRY_BOX_WIDTH, height=REPORT_ENTRY_BOX_HEIGHT)
            
            # Cancel date box
            self.CD_box = Label(self.container, text='Cancel Date', bg='#1391c1', fg='white', height=3, width=20)
            self.CD_box.config(font=(FONT, FONT_SIZE, STYLE))
            self.CD_box.place(relx=MENU_LABEL_X, rely=0.61, anchor='center')
            self.CD_entry = Entry(self.container, font=(FONT, FONT_SIZE, STYLE))
            self.CD_entry.insert(0, (date.today()))
            self.CD_entry.place(relx=REPORT_ENTRY_BOX_X, rely=0.61, anchor='center',
                               width=REPORT_ENTRY_BOX_WIDTH, height=REPORT_ENTRY_BOX_HEIGHT)
            
    def go_to_confirm(self):
        #checking for missing or incomplete fields
        listOfEntrys = [self.AN_entry.get(), self.ID_entry.get(), self.CD_entry.get()]
        if "" in listOfEntrys: #checks missing
            self.failed()
            #Back to cancel function button
            self.backCancelButton = Button(self.container, text="Back to Cancellation Function", padx=20, pady=20, 
             bg="#27c0ab",borderwidth=5, highlightthickness=4, highlightbackground="#ecb606", relief="raised", command=self.close_incompleteError)
            self.backCancelButton.config(font=(FONT, FONT_SIZE, STYLE))
            self.backCancelButton.place(relx=0.5, rely=0.7, anchor="center")
            
        else:
            #Prompt
            self.popupPromptLabel = Label(self.container, text="Confirm Cancellation Details To \nBe Correct", 
            width=40, height=16, font=(FONT, FONT_SIZE, STYLE), anchor='n', bg='#9ddd58')
            self.popupPromptLabel.place(relx=0.5, rely=0.5, anchor='center')
            #AN Label
            self.input_AN = Label(self.container, text=self.AN_entry.get(), font=(FONT, FONT_SIZE, STYLE), bg='#9ddd58')
            self.input_AN.place(relx=0.6, rely=0.35, anchor="center")
            #Book title Label
            sql_statement = "SELECT title FROM books WHERE accession_no = '{}'".format(self.AN_entry.get())
            data_BT = self.cursor.execute(sql_statement).fetchall()[0][0]
            self.input_BT = Label(self.container, text=data_BT, font=(FONT, FONT_SIZE, STYLE), bg='#9ddd58')
            self.input_BT.place(relx=0.6, rely=0.42, anchor="center")
            #Membership ID Label
            self.input_ID = Label(self.container, text=self.ID_entry.get(), font=(FONT, FONT_SIZE, STYLE), bg='#9ddd58')
            self.input_ID.place(relx=0.6, rely=0.49, anchor="center")
            #Member name Label
            sql_statement = "SELECT name FROM members WHERE memberid = '{}'".format(self.ID_entry.get())
            data_name = self.cursor.execute(sql_statement).fetchall()[0][0]
            self.input_name = Label(self.container, text=data_name, font=(FONT, FONT_SIZE, STYLE), bg='#9ddd58')
            self.input_name.place(relx=0.6, rely=0.56, anchor="center")
            #Cancel date Label
            self.input_CD = Label(self.container, text=self.CD_entry.get(), font=(FONT, FONT_SIZE, STYLE), bg='#9ddd58')
            self.input_CD.place(relx=0.6, rely=0.63, anchor="center")
            #Labels
            self.AN_label = Label(self.container, text = "Accession Number:", font=(FONT, FONT_SIZE, STYLE), bg='#9ddd58')
            self.AN_label.place(relx=0.4, rely=0.35, anchor="center")
            self.BT_label = Label(self.container, text = "Book Title:", font=(FONT, FONT_SIZE, STYLE), bg='#9ddd58')
            self.BT_label.place(relx=0.4, rely=0.42, anchor="center")
            self.ID_label = Label(self.container, text = "Membership ID:", font=(FONT, FONT_SIZE, STYLE), bg='#9ddd58')
            self.ID_label.place(relx=0.4, rely=0.49, anchor="center")
            self.name_label = Label(self.container, text = "Member Name:", font=(FONT, FONT_SIZE, STYLE), bg='#9ddd58')
            self.name_label.place(relx=0.4, rely=0.56, anchor="center")
            self.CD_label = Label(self.container, text = "Cancellation Date", font=(FONT, FONT_SIZE, STYLE), bg='#9ddd58')
            self.CD_label.place(relx=0.4, rely=0.63, anchor="center")
           
            #Confirm Cancellation Button
            self.confirmCancellationButton = Button(self.container, text="Confirm Cancellation", padx=20, pady=20,
                                                    wraplength=300,
                                                    command=self.go_to_error, bg="#27c0ab",borderwidth=5, highlightthickness=4,
                                                    highlightbackground="#ecb606", relief="raised", font=(FONT, FONT_SIZE, STYLE))
            self.confirmCancellationButton.place(relx=0.37, rely=0.73, anchor="center")
            #Back to cancel function button
            self.backBorrowButton = Button(self.container, text="Back to Cancellation Function", padx=20, pady=20,
                                           wraplength=400,
                                            bg="#27c0ab",borderwidth=5, highlightthickness=4,
                                           highlightbackground="#ecb606", relief="raised", command=self.close_confirmPage, font=(FONT, FONT_SIZE, STYLE))
            self.backBorrowButton.place(relx=0.6, rely=0.73, anchor="center")
            
    def failed(self):   
        self.ErrorPop = Label(self.container, text='Error!\n\n Duplicate, Missing or\nIncomplete fields.',
        fg='yellow', bg='#cc0505',
        relief='raised', width=30, height=15)
        self.ErrorPop.config(font=(FONT, FONT_SIZE, STYLE))
        self.ErrorPop.place(relx=0.5, rely=0.4, anchor="center")

    def close_incompleteError(self):
        self.ErrorPop.lower()
        self.backCancelButton.lower()          
           
    def close_confirmPage(self):
        self.cursor = self.engine.connect()
        #Close confirmation page popup
        self.popupPromptLabel.lower()
        self.confirmCancellationButton.lower()
        self.backBorrowButton.lower()
        self.input_AN.lower()
        self.input_BT.lower()
        self.input_ID.lower()   
        self.input_name.lower()
        self.input_CD.lower()
        
        self.AN_label.lower()
        self.BT_label.lower()
        self.ID_label.lower()
        self.name_label.lower()
        self.CD_label.lower()
    
    def go_to_error(self):
        self.cursor = self.engine.connect()
        #Close confirmation page popup
        self.popupPromptLabel.lower()
        self.confirmCancellationButton.lower()
        self.backBorrowButton.lower()
        self.input_AN.lower()
        self.input_BT.lower()
        self.input_ID.lower()   
        self.input_name.lower()
        self.input_CD.lower()
        
        self.AN_label.lower()
        self.BT_label.lower()
        self.ID_label.lower()
        self.name_label.lower()
        self.CD_label.lower()
        for x in range(1):
            #Member has no such reservation
            sql_statement = "Select * FROM reservation WHERE ReservedBookAccession = '{}' AND ReserverID = '{}'".format(self.AN_entry.get(), self.ID_entry.get())
            data_reservations = self.cursor.execute(sql_statement).fetchall()
            if len(data_reservations) == 0:  
                self.go_to_cancelError()
                break
            else:
                sql_statement = "DELETE FROM reservation WHERE ReserverID = '{}' AND ReservedBookAccession = '{}'".format(self.ID_entry.get(), self.AN_entry.get())
                self.cursor.execute(sql_statement)     

    def go_to_cancelError(self):
        self.popupErrorLabel = Label(self.container, text="Error!\n\n Member has no such reservation.", 
        fg='yellow', bg='#cc0505',
        relief='raised', width=30, height=15)
        self.popupErrorLabel.place(relx=0.5, rely=0.3, anchor="center")
        self.backBorrowButton = Button(self.container, text="Back to Cancellation Function", padx=20, pady=20, 
            command=self.closeError, bg="#27c0ab",borderwidth=5, highlightthickness=4, highlightbackground="#ecb606", relief="raised")
        self.backBorrowButton.place(relx=0.5, rely=0.65, anchor="center")

    def closeError(self):
        self.popupErrorLabel.lower()
        self.backBorrowButton.lower()
      
    def go_to_reservations(self):
            Reservation(self.root, self.parent, self.engine)
            self.container.grid_forget()    


