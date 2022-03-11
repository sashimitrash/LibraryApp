from tkinter import Label, Button, Entry
from sqlalchemy.exc import IntegrityError, DataError, OperationalError
from apps.resources.variables import *
from apps.resources.container import Container

class Membership(Container):
    def __init__(self, root, parent, engine):
        super().__init__(root, 'Member Main Menu')
        self.init_image()
        self.parent = parent
        self.engine = engine

        # reports image
        self.membership = self.open_image('apps/resources/membership.png', SIDE_IMAGE_WIDTH, SIDE_IMAGE_HEIGHT)
        # reinitialize because tkinter would destroy self.report variable after using it
        self.membership_image  = Label(self.container, image=self.membership)
        self.membership_image.place(relx=SIDE_IMAGE_X, rely=SIDE_IMAGE_Y, anchor='center')
        self.membership_text = Label(self.container, text='Membership', font=(FONT, FONT_SIZE, STYLE), fg='white', bg='black')
        self.membership_text.place(relx=SIDE_TEXT_X, rely=SIDE_TEXT_Y, anchor='center')


        # title label
        self.label = Label(self.container, text='Select one of the options below:', fg='black', bg='#2dccb6',
                           relief='raised', width=60, height=3)
        self.label.config(font=(FONT, FONT_SIZE, STYLE))
        self.label.place(relx=HEADING_LABEL_X, rely=HEADING_LABEL_Y, anchor="center")  # label is always mid align
        
        # back to main_menu button
        self.return_btn = Button(self.container, text='Back to Main Menu', command=lambda: parent.return_to_main_menu(self),
                                 bg='#c5e3e5', width=60, height=1, relief='raised', borderwidth=5)
        self.return_btn.config(font=(FONT, FONT_SIZE, STYLE))
        self.return_btn.place(relx=0.5, rely=0.9, anchor="center")  # return_btn is always mid align

        # Membership Creation
        self.member_create_btn = Button(self.container, text='1. Membership Creation', command=self.go_to_create_member,
                            height=3, width=20, wraplength=200)
        self.member_create_btn.config(font=(FONT, FONT_SIZE, STYLE), fg='white', bg='#17a1d5')
        self.member_create_btn.place(relx=0.55, rely=0.26)

        # Membership Deletion
        self.member_delete_btn = Button(self.container, text='2. Membership Deletion', command=self.go_to_delete_member,
                                height=3, width=20, wraplength=200)
        self.member_delete_btn.config(font=(FONT, FONT_SIZE, STYLE), fg='white', bg='#2964e7')
        self.member_delete_btn.place(relx=0.55, rely=0.42)

        # Membership Update
        self.member_update_btn = Button(self.container, text='3. Membership Update', command=self.go_to_update_member,
                                height=3, width=20, wraplength=200)
        self.member_update_btn.config(font=(FONT, FONT_SIZE, STYLE), fg='white', bg='#4e3ddc')
        self.member_update_btn.place(relx=0.55, rely=0.58)

    def go_to_create_member(self):
        MemberCreate(self.root, self.parent, self.engine)
        self.container.grid_forget()
    
    def go_to_delete_member(self):
        MemberDelete(self.root, self.parent, self.engine)
        self.container.grid_forget()

    def go_to_update_member(self):
        MemberUpdate(self.root, self.parent, self.engine)
        self.container.grid_forget()

class MemberCreate(Container):
    def __init__(self, root, parent, engine):
        super().__init__(root, "Create Member Menu")
        self.init_image()
        self.parent = parent
        self.engine = engine

        # Title Label
        self.label = Label(self.container, text='To Create Member, Please Enter Requested Information Below', fg='black', bg='#2dccb6',
                    relief='raised', width=60, height=3)
        self.label.config(font=(FONT, FONT_SIZE, STYLE))
        self.label.place(relx=HEADING_LABEL_X, rely=HEADING_LABEL_Y, anchor="center")  # label is always mid align

        # back to report_menu button
        self.return_btn = Button(self.container, text='Back to Membership Menu', command=self.go_to_membership,
                                 bg='#27c0ab', width=20, height=2, relief='raised', borderwidth=5,
                                 highlightthickness=4, highlightbackground="#eaba2d")
        self.return_btn.config(font=(FONT, 20, STYLE))
        self.return_btn.place(relx=0.7, rely=0.9, anchor="center")

        # book search button
        self.create_member_btn = Button(self.container, text='Create Member', command=self.create_member,
                                 bg='#27c0ab', width=20, height=2, relief='raised', borderwidth=5,
                                 highlightthickness=4, highlightbackground="#eaba2d")
        self.create_member_btn.config(font=(FONT, FONT_SIZE, STYLE))
        self.create_member_btn.place(relx=0.3, rely=0.9, anchor="center")

        # Membership ID box
        self.ID_box = Label(self.container, text='Membership ID', bg='#1391c1', fg='white', height=3, width=20)
        self.ID_box.config(font=(FONT, FONT_SIZE, STYLE))
        self.ID_box.place(relx=MENU_LABEL_X, rely=0.23, anchor='center')
        self.ID_ent = Entry(self.container, font=(FONT, FONT_SIZE, STYLE))
        self.ID_ent.place(relx=REPORT_ENTRY_BOX_X, rely=0.23, anchor='center',
                               width=REPORT_ENTRY_BOX_WIDTH, height=REPORT_ENTRY_BOX_HEIGHT)

        # Name box
        self.name_box = Label(self.container, text='Name', bg='#1fa4df', fg='white', height=3, width=20)
        self.name_box.config(font=(FONT, FONT_SIZE, STYLE))
        self.name_box.place(relx=MENU_LABEL_X, rely=0.36, anchor='center')
        self.name_ent = Entry(self.container, font=(FONT, FONT_SIZE, STYLE))
        self.name_ent.place(relx=REPORT_ENTRY_BOX_X, rely=0.36, anchor='center',
                               width=REPORT_ENTRY_BOX_WIDTH, height=REPORT_ENTRY_BOX_HEIGHT)

        # Faculty box
        self.faculty_box = Label(self.container, text='Faculty', bg='#49abde', fg='white', height=3, width=20)
        self.faculty_box.config(font=(FONT, FONT_SIZE, STYLE))
        self.faculty_box.place(relx=MENU_LABEL_X, rely=0.49, anchor='center')
        self.faculty_ent = Entry(self.container, font=(FONT, FONT_SIZE, STYLE))
        self.faculty_ent.place(relx=REPORT_ENTRY_BOX_X, rely=0.49, anchor='center',
                                width=REPORT_ENTRY_BOX_WIDTH, height=REPORT_ENTRY_BOX_HEIGHT)

        # Phone Number box
        self.phone_box = Label(self.container, text='Phone Number', bg='#71b6df', fg='white', height=3, width=20)
        self.phone_box.config(font=(FONT, FONT_SIZE, STYLE))
        self.phone_box.place(relx=MENU_LABEL_X, rely=0.62, anchor='center')
        self.phone_ent = Entry(self.container, font=(FONT, FONT_SIZE, STYLE))
        self.phone_ent.place(relx=REPORT_ENTRY_BOX_X, rely=0.62, anchor='center',
                                width=REPORT_ENTRY_BOX_WIDTH, height=REPORT_ENTRY_BOX_HEIGHT)

        # Email box
        self.email_box = Label(self.container, text='Email Address', bg='#96c4e3', fg='white', height=3, width=20)
        self.email_box.config(font=(FONT, FONT_SIZE, STYLE))
        self.email_box.place(relx=MENU_LABEL_X, rely=0.75, anchor='center')
        self.email_ent = Entry(self.container, font=(FONT, FONT_SIZE, STYLE))
        self.email_ent.place(relx=REPORT_ENTRY_BOX_X, rely=0.75, anchor='center',
                                width=REPORT_ENTRY_BOX_WIDTH, height=REPORT_ENTRY_BOX_HEIGHT)

    def go_to_membership(self):
        Membership(self.root, self.parent, self.engine)
        self.container.grid_forget()

    def popup(self, response:bool):
        if response:
            popup_text = "Success!\n\n\nALS Membership created."
            popup_bg = "#9ddd58"
            popup_font_color = "#000000"
        
        else:
            popup_text = "Error!\n\n\nMember already exist; Missing or Incomplete fields."
            popup_bg = "#cc0505"
            popup_font_color = "#ffff00"

        self.popup_label = Label(self.container, text=popup_text, bg =popup_bg, fg=popup_font_color, width=40, height=15, wraplength=450)
        self.popup_label.config(font=(FONT,FONT_SIZE, STYLE))
        self.popup_label.place(relx=0.5, rely=0.5, anchor="center")

        self.return_to_create_btn = Button(self.container, text='Back to Create Function', padx=20, pady=20,\
            command=self.close, bg='#27c0ab', borderwidth=5, relief='raised', highlightthickness=4, highlightbackground='#fae420')
        self.return_to_create_btn.config(font=(FONT,FONT_SIZE,STYLE))
        self.return_to_create_btn.place(relx=0.5, rely=0.7, anchor='center')

    def close(self):
        self.popup_label.lower()
        self.return_to_create_btn.lower()

    
    def get_entry(self):
        raw = [self.ID_ent.get(), self.name_ent.get(), self.faculty_ent.get(), self.phone_ent.get(), self.email_ent.get()]
        for item in raw:
            if item == "":
                raise ValueError('Invalid Fields: Entries cannot be empty')
        return raw

    def create_member(self):
        try:
            cursor = self.engine.connect()
            data = self.get_entry()
            sql_statement = """INSERT INTO members VALUES("{}", "{}", "{}", "{}", "{}")""".format(data[0], data[1], data[2], data[3], data[4])
            cursor.execute(sql_statement)
            self.popup(True)

        except (IntegrityError, DataError, ValueError):
            self.popup(False)

class MemberDelete(Container):
    def __init__(self, root, parent, engine):
        super().__init__(root, "Delete Member Menu")
        self.init_image()
        self.parent = parent
        self.engine = engine

        # Title Label
        self.label = Label(self.container, text='To Delete Member, Please Enter Your Membership ID', fg='black', bg='#2dccb6',
                    relief='raised', width=60, height=3)
        self.label.config(font=(FONT, FONT_SIZE, STYLE))
        self.label.place(relx=HEADING_LABEL_X, rely=HEADING_LABEL_Y, anchor="center")  # label is always mid align


        # Delete MembershipID box
        self.ID_box = Label(self.container, text='Membership ID', bg='#49abde', fg='white', height=3, width=20)
        self.ID_box.config(font=(FONT, FONT_SIZE, STYLE))
        self.ID_box.place(relx=MENU_LABEL_X, rely=0.49, anchor='center')
        self.ID_ent = Entry(self.container, font=(FONT, FONT_SIZE, STYLE))
        self.ID_ent.place(relx=REPORT_ENTRY_BOX_X, rely=0.49, anchor='center',
                                width=REPORT_ENTRY_BOX_WIDTH, height=REPORT_ENTRY_BOX_HEIGHT)

        # back to report_menu button
        self.return_btn = Button(self.container, text='Back to Membership Menu', command=self.go_to_membership,
                                 bg='#27c0ab', width=20, height=2, relief='raised', borderwidth=5,
                                 highlightthickness=4, highlightbackground="#eaba2d")
        self.return_btn.config(font=(FONT, 20, STYLE))
        self.return_btn.place(relx=0.7, rely=0.9, anchor="center")

        # book search button
        self.create_member_btn = Button(self.container, text='Delete Member', command=lambda:self.get_member_details(self.ID_ent.get()),
                                 bg='#27c0ab', width=20, height=2, relief='raised', borderwidth=5,
                                 highlightthickness=4, highlightbackground="#eaba2d")
        self.create_member_btn.config(font=(FONT, FONT_SIZE, STYLE))
        self.create_member_btn.place(relx=0.3, rely=0.9, anchor="center")

    def go_to_membership(self):
        Membership(self.root, self.parent, self.engine)
        self.container.grid_forget()
    
    def get_member_details(self, Id:str):
        sql_statement = """SELECT * FROM members WHERE memberid = "{}";""".format(Id)
        cursor = self.engine.connect()
        data = cursor.execute(sql_statement).fetchall()
        if len(data) == 0:
            self.popup(False, 0)
            # return
        else:
            self.popup(True, data[0])
    
    def popup(self, response:bool, info = None):
        if response:
            popup_text = "Please Confirm Details to be Correct."
            popup_bg = "#9ddd58"
            popup_font_color = "#000000"
            memberInfo_format = "Member ID: {}\nName: {}\nFaculty: {}\nPhone Number: {}\nEmail Address: {}".format(info[0], info[1],\
                info[2], info[3], info[4])
            
            self.popup_heading_label = Label(self.container, text=popup_text, bg =popup_bg, fg=popup_font_color, width=35, height=2)
            self.popup_heading_label.config(font=(FONT,FONT_SIZE, STYLE))
            self.popup_heading_label.place(relx=0.5, rely=0.3, anchor="center")

            self.popup_body_label = Label(self.container, text=memberInfo_format, bg =popup_bg, fg=popup_font_color, width=35, height=12)
            self.popup_body_label.config(font=(FONT,FONT_SIZE, STYLE))
            self.popup_body_label.place(relx=0.5, rely=0.55, anchor="center")

            self.confirm_delete_btn = Button(self.container, text='Confirm Delete', padx=10, pady=10,\
                command=lambda:self.delete_member(self.ID_ent.get()), bg='#27c0ab', borderwidth=5, relief='raised', highlightthickness=4, highlightbackground='#fae420')
            self.confirm_delete_btn.config(font=(FONT,15,STYLE))
            self.confirm_delete_btn.place(relx=0.40, rely=0.7, anchor='center')

            self.back_to_delete_btn = Button(self.container, text='Back to Delete Function', padx=10, pady=10,\
                command=lambda:self.close(self.popup_heading_label, self.popup_body_label, self.confirm_delete_btn, self.back_to_delete_btn),\
                     bg='#27c0ab', borderwidth=5, relief='raised', highlightthickness=4, highlightbackground='#fae420')
            self.back_to_delete_btn.config(font=(FONT,15,STYLE), wraplength=300)
            self.back_to_delete_btn.place(relx=0.60, rely=0.7, anchor='center')

        else:
            if info == 0:
                popup_text = "Error!\n\n\nMember does not exist"
            else:
                popup_text = "Error!\n\n\nMember has outstanding loans or fines."
            popup_bg = "#cc0505"
            popup_font_color = "#ffff00"

            self.popup_label = Label(self.container, text=popup_text, bg =popup_bg, fg=popup_font_color, width=40, height=15, wraplength=450)
            self.popup_label.config(font=(FONT,FONT_SIZE, STYLE))
            self.popup_label.place(relx=0.5, rely=0.5, anchor="center")

            self.back_to_delete_btn = Button(self.container, text='Back to Delete Function', padx=20, pady=20,\
                command=lambda:self.close(self.popup_label, self.back_to_delete_btn),\
                     bg='#27c0ab', borderwidth=5, relief='raised', highlightthickness=4, highlightbackground='#fae420')
            self.back_to_delete_btn.config(font=(FONT,FONT_SIZE,STYLE))
            self.back_to_delete_btn.place(relx=0.5, rely=0.7, anchor='center')

    def close(self, *args):
        for element in args:
            element.lower()

    def delete_member(self, id:str):
        try:
            sql_query = """DELETE FROM members WHERE memberid = '{}';""".format(id)
            cursor = self.engine.connect()
            cursor.execute(sql_query)
            self.close(self.popup_heading_label, self.popup_body_label, self.confirm_delete_btn, self.back_to_delete_btn)
        
        except(IntegrityError, DataError):
            self.close(self.popup_heading_label, self.popup_body_label, self.confirm_delete_btn, self.back_to_delete_btn)
            self.popup(False)

class MemberUpdate(Container):
    def __init__(self, root, parent, engine):
        super().__init__(root, "Update Member Menu")
        self.init_image()
        self.parent = parent
        self.engine = engine

        # Title Label
        self.label = Label(self.container, text='To Update Member, Please Enter Your Membership ID', fg='black', bg='#2dccb6',
                    relief='raised', width=60, height=3)
        self.label.config(font=(FONT, FONT_SIZE, STYLE))
        self.label.place(relx=HEADING_LABEL_X, rely=HEADING_LABEL_Y, anchor="center")  # label is always mid align


        # Update MembershipID box
        self.ID_box = Label(self.container, text='Membership ID', bg='#49abde', fg='white', height=3, width=20)
        self.ID_box.config(font=(FONT, FONT_SIZE, STYLE))
        self.ID_box.place(relx=MENU_LABEL_X, rely=0.49, anchor='center')
        self.ID_ent = Entry(self.container, font=(FONT, FONT_SIZE, STYLE))
        self.ID_ent.place(relx=REPORT_ENTRY_BOX_X, rely=0.49, anchor='center',
                                width=REPORT_ENTRY_BOX_WIDTH, height=REPORT_ENTRY_BOX_HEIGHT)

        # back to report_menu button
        self.return_btn = Button(self.container, text='Back to Membership Menu', command=self.go_to_membership,
                                 bg='#27c0ab', width=20, height=2, relief='raised', borderwidth=5,
                                 highlightthickness=4, highlightbackground="#eaba2d")
        self.return_btn.config(font=(FONT, 20, STYLE))
        self.return_btn.place(relx=0.7, rely=0.9, anchor="center")

        # book search button
        self.update_member_btn = Button(self.container, text='Update Member', command=lambda:self.update_info(),
                           bg='#27c0ab', width=20, height=2, relief='raised', borderwidth=5,
                           highlightthickness=4, highlightbackground="#eaba2d")
        self.update_member_btn.config(font=(FONT, FONT_SIZE, STYLE))
        self.update_member_btn.place(relx=0.3, rely=0.9, anchor="center")

    def go_to_membership(self):
        Membership(self.root, self.parent, self.engine)
        self.container.grid_forget()

    def update_info(self):
        sql_statement = """SELECT * FROM members WHERE memberid = "{}";""".format(self.ID_ent.get())
        cursor = self.engine.connect()
        data = cursor.execute(sql_statement).fetchall()

        if len(data) == 0:
            self.popup(False, 0)
        else:
            self.close(self.label, self.ID_box, self.ID_ent, self.update_member_btn, self.return_btn)
            self.label_B = Label(self.container, text='Please Enter Requested Information Below', fg='black', bg='#2dccb6',
                    relief='raised', width=60, height=3)
            self.label_B.config(font=(FONT, FONT_SIZE, STYLE))
            self.label_B.place(relx=HEADING_LABEL_X, rely=HEADING_LABEL_Y, anchor="center")  # label is always mid align

            # Membership ID box
            self.ID_box_header_label = Label(self.container, text='Membership ID', bg='#1391c1', fg='white', height=3, width=20)
            self.ID_box_header_label.config(font=(FONT, FONT_SIZE, STYLE))
            self.ID_box_header_label.place(relx=MENU_LABEL_X, rely=0.23, anchor='center')
            self.ID_box_label = Label(self.container, text=self.ID_ent.get(), bg='#f3f0f1', fg='black', height=3, width=35)
            self.ID_box_label.config(font=(FONT, FONT_SIZE, STYLE))
            self.ID_box_label.place(relx=REPORT_ENTRY_BOX_X, rely=0.23, anchor='center')

            # Name box
            self.name_box = Label(self.container, text='Name', bg='#1fa4df', fg='white', height=3, width=20)
            self.name_box.config(font=(FONT, FONT_SIZE, STYLE))
            self.name_box.place(relx=MENU_LABEL_X, rely=0.36, anchor='center')
            self.name_ent = Entry(self.container, font=(FONT, FONT_SIZE, STYLE))
            self.name_ent.place(relx=REPORT_ENTRY_BOX_X, rely=0.36, anchor='center',
                                width=REPORT_ENTRY_BOX_WIDTH, height=REPORT_ENTRY_BOX_HEIGHT)
            self.name_ent.insert(0, data[0][1])

            # Faculty box
            self.faculty_box = Label(self.container, text='Faculty', bg='#49abde', fg='white', height=3, width=20)
            self.faculty_box.config(font=(FONT, FONT_SIZE, STYLE))
            self.faculty_box.place(relx=MENU_LABEL_X, rely=0.49, anchor='center')
            self.faculty_ent = Entry(self.container, font=(FONT, FONT_SIZE, STYLE))
            self.faculty_ent.place(relx=REPORT_ENTRY_BOX_X, rely=0.49, anchor='center',
                                    width=REPORT_ENTRY_BOX_WIDTH, height=REPORT_ENTRY_BOX_HEIGHT)
            self.faculty_ent.insert(0, data[0][2])

            # Phone Number box
            self.phone_box = Label(self.container, text='Phone Number', bg='#71b6df', fg='white', height=3, width=20)
            self.phone_box.config(font=(FONT, FONT_SIZE, STYLE))
            self.phone_box.place(relx=MENU_LABEL_X, rely=0.62, anchor='center')
            self.phone_ent = Entry(self.container, font=(FONT, FONT_SIZE, STYLE))
            self.phone_ent.place(relx=REPORT_ENTRY_BOX_X, rely=0.62, anchor='center',
                                    width=REPORT_ENTRY_BOX_WIDTH, height=REPORT_ENTRY_BOX_HEIGHT)
            self.phone_ent.insert(0, data[0][3])

            # Email box
            self.email_box = Label(self.container, text='Email Address', bg='#96c4e3', fg='white', height=3, width=20)
            self.email_box.config(font=(FONT, FONT_SIZE, STYLE))
            self.email_box.place(relx=MENU_LABEL_X, rely=0.75, anchor='center')
            self.email_ent = Entry(self.container, font=(FONT, FONT_SIZE, STYLE))
            self.email_ent.place(relx=REPORT_ENTRY_BOX_X, rely=0.75, anchor='center',
                                    width=REPORT_ENTRY_BOX_WIDTH, height=REPORT_ENTRY_BOX_HEIGHT)
            self.email_ent.insert(0, data[0][4])

            self.update_different_btn = Button(self.container, text='Update Different Member', command=lambda:self.update_different_member(),\
                bg='#27c0ab', width=20, height=2, relief='raised', borderwidth=5,highlightthickness=4, highlightbackground="#eaba2d")
            self.update_different_btn.config(font=(FONT, FONT_SIZE, STYLE))
            self.update_different_btn.place(relx=0.7, rely=0.9, anchor="center")

            self.update_records_btn = Button(self.container, text='Update Records', command=lambda:self.get_update_info(),\
                bg='#27c0ab', width=20, height=2, relief='raised', borderwidth=5,\
                highlightthickness=4, highlightbackground="#eaba2d")
            self.update_records_btn.config(font=(FONT, FONT_SIZE, STYLE))
            self.update_records_btn.place(relx=0.3, rely=0.9, anchor="center")

    def update_different_member(self):
        self.open(self.label, self.ID_box, self.ID_ent, self.update_member_btn, self.return_btn)
        self.close(self.label_B, self.ID_box_header_label, self.ID_box_label, self.name_box,\
             self.name_ent, self.faculty_box, self.faculty_ent, self.phone_box, self.phone_ent, self.email_box, self.email_ent,\
                 self.update_different_btn, self.update_records_btn)


    def popup(self, response:bool, info = None):
        if response:
            popup_text = "Please Confirm Details to be Correct."
            popup_bg = "#9ddd58"
            popup_font_color = "#000000"
            memberInfo_format = "Member ID: {}\nName: {}\nFaculty: {}\nPhone Number: {}\nEmail Address: {}".format(self.ID_ent.get(), info[0],\
                info[1], info[2], info[3])

            self.popup_heading_label = Label(self.container, text=popup_text, bg =popup_bg, fg=popup_font_color, width=35, height=2)
            self.popup_heading_label.config(font=(FONT,FONT_SIZE, STYLE))
            self.popup_heading_label.place(relx=0.5, rely=0.3, anchor="center")

            self.popup_body_label = Label(self.container, text=memberInfo_format, bg =popup_bg, fg=popup_font_color, width=35, height=12)
            self.popup_body_label.config(font=(FONT,FONT_SIZE, STYLE))
            self.popup_body_label.place(relx=0.5, rely=0.55, anchor="center")

            self.confirm_update_btn = Button(self.container, text='Confirm Update', padx=10, pady=10,\
                command=lambda:self.update_member(self.ID_ent.get(), info), bg='#27c0ab', borderwidth=5, relief='raised',\
                highlightthickness=4, highlightbackground='#fae420')
            self.confirm_update_btn.config(font=(FONT,15,STYLE))
            self.confirm_update_btn.place(relx=0.40, rely=0.7, anchor='center')

            self.back_to_update_btn = Button(self.container, text='Back to Update Function', padx=10, pady=10,\
                command=lambda:self.close(self.popup_heading_label, self.popup_body_label, self.confirm_update_btn, self.back_to_update_btn),\
                    bg='#27c0ab', borderwidth=5, relief='raised', highlightthickness=4, highlightbackground='#fae420')
            self.back_to_update_btn.config(font=(FONT,15,STYLE), wraplength=300)
            self.back_to_update_btn.place(relx=0.60, rely=0.7, anchor='center')

        else:
            if info == 0:
                popup_text = "Error!\n\n\nMember does not exist"
            else:
                popup_text = "Error!\n\n\nMissing or Invalid fields"
            popup_bg = "#cc0505"
            popup_font_color = "#ffff00"

            self.popup_label = Label(self.container, text=popup_text, bg =popup_bg, fg=popup_font_color, width=40, height=15, wraplength=450)
            self.popup_label.config(font=(FONT,FONT_SIZE, STYLE))
            self.popup_label.place(relx=0.5, rely=0.5, anchor="center")

            self.back_to_update_btn = Button(self.container, text='Back to Update Function', padx=20, pady=20,\
                command=lambda:self.close(self.popup_label, self.back_to_update_btn),\
                    bg='#27c0ab', borderwidth=5, relief='raised', highlightthickness=4, highlightbackground='#fae420')
            self.back_to_update_btn.config(font=(FONT,FONT_SIZE,STYLE))
            self.back_to_update_btn.place(relx=0.5, rely=0.7, anchor='center')

    def success_notif(self):
            popup_text = "Success!\n\n ALS Membership Updated."
            popup_bg = "#9ddd58"
            popup_font_color = "#000000"

            self.popup_heading_label = Label(self.container, text=popup_text, bg =popup_bg, fg=popup_font_color, width=35, height=14)
            self.popup_heading_label.config(font=(FONT,FONT_SIZE, STYLE))
            self.popup_heading_label.place(relx=0.5, rely=0.5, anchor="center")

            self.confirm_update_btn = Button(self.container, text='Update Another Member', padx=10, pady=10,\
                command=lambda:self.go_to_update_member(), bg='#27c0ab', borderwidth=5, relief='raised',\
                highlightthickness=4, highlightbackground='#fae420')
            self.confirm_update_btn.config(font=(FONT,15,STYLE))
            self.confirm_update_btn.place(relx=0.40, rely=0.7, anchor='center')

            self.back_to_update_btn = Button(self.container, text='Back to Update Function', padx=10, pady=10,\
                command=lambda:self.close(self.popup_heading_label, self.popup_body_label, self.confirm_update_btn, self.back_to_update_btn),\
                    bg='#27c0ab', borderwidth=5, relief='raised', highlightthickness=4, highlightbackground='#fae420')
            self.back_to_update_btn.config(font=(FONT,15,STYLE), wraplength=300)
            self.back_to_update_btn.place(relx=0.60, rely=0.7, anchor='center')

    def go_to_update_member(self):
        MemberUpdate(self.root, self.parent, self.engine)
        self.container.grid_forget()

    def close(self, *args):
        for element in args:
            element.lower()

    def open(self, *args):
        for element in args:
            element.lift()

    def get_update_info(self):
        data = [self.name_ent.get(), self.faculty_ent.get(), self.phone_ent.get(), self.email_ent.get()]
        status = True
        for i in data:
            if i == '':
                status = False
        if status:
            self.popup(status, data)
        else:
            self.popup(status)

    def update_member(self, id, update:tuple):
        try:
            sql_query = """UPDATE members SET name='{}', faculty='{}', phoneNumber={}, email='{}' WHERE memberid='{}';""".format(update[0],\
                update[1], update[2], update[3], id)
            cursor = self.engine.connect()
            cursor.execute(sql_query)
            self.close(self.popup_heading_label, self.popup_body_label, self.confirm_update_btn, self.back_to_update_btn)
            self.success_notif()

        except(IntegrityError, DataError, OperationalError):
            self.close(self.popup_heading_label, self.popup_body_label, self.confirm_update_btn, self.back_to_update_btn)
            self.popup(False)