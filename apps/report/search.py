from tkinter import Label, Button, Entry
from apps.resources.variables import *
from apps.resources.container import Container
from apps.report.report_pages import Report


class BookSearch(Container):
    def __init__(self, root, parent, engine):
        super().__init__(root, 'Book Search')
        self.init_image()
        self.parent = parent
        self.engine = engine

        # title label
        self.label = Label(self.container, text='Search based on one of the categories below:', fg='black', bg='#2dccb6',
                           relief='raised', width=60, height=3)
        self.label.config(font=(FONT, FONT_SIZE, STYLE))
        self.label.place(relx=HEADING_LABEL_X, rely=HEADING_LABEL_Y, anchor="center")  # label is always mid align

        # back to report_menu button
        self.return_btn = Button(self.container, text='Back to Report Menu', command=self.go_to_report,
                                 bg='#27c0ab', width=20, height=2, relief='raised', borderwidth=5,
                                 highlightthickness=4, highlightbackground="#eaba2d")
        self.return_btn.config(font=(FONT, FONT_SIZE, STYLE))
        self.return_btn.place(relx=0.7, rely=0.9, anchor="center")

        # book search button
        self.search_btn = Button(self.container, text='Search Book', command=self.search_books,
                                 bg='#27c0ab', width=20, height=2, relief='raised', borderwidth=5,
                                 highlightthickness=4, highlightbackground="#eaba2d")
        self.search_btn.config(font=(FONT, FONT_SIZE, STYLE))
        self.search_btn.place(relx=0.3, rely=0.9, anchor="center")

        # title box
        self.title_box = Label(self.container, text='Title', bg='#1391c1', fg='white', height=3, width=20)
        self.title_box.config(font=(FONT, FONT_SIZE, STYLE))
        self.title_box.place(relx=MENU_LABEL_X, rely=0.23, anchor='center')
        self.title_entry = Entry(self.container, font=(FONT, FONT_SIZE, STYLE))
        self.title_entry.place(relx=REPORT_ENTRY_BOX_X, rely=0.23, anchor='center',
                               width=REPORT_ENTRY_BOX_WIDTH, height=REPORT_ENTRY_BOX_HEIGHT)

        # Authors box
        self.author_box = Label(self.container, text='Authors', bg='#1fa4df', fg='white', height=3, width=20)
        self.author_box.config(font=(FONT, FONT_SIZE, STYLE))
        self.author_box.place(relx=MENU_LABEL_X, rely=0.36, anchor='center')
        self.author_entry = Entry(self.container, font=(FONT, FONT_SIZE, STYLE))
        self.author_entry.place(relx=REPORT_ENTRY_BOX_X, rely=0.36, anchor='center',
                               width=REPORT_ENTRY_BOX_WIDTH, height=REPORT_ENTRY_BOX_HEIGHT)

        # ISBN box
        self.isbn_box = Label(self.container, text='ISBN', bg='#49abde', fg='white', height=3, width=20)
        self.isbn_box.config(font=(FONT, FONT_SIZE, STYLE))
        self.isbn_box.place(relx=MENU_LABEL_X, rely=0.49, anchor='center')
        self.isbn_entry = Entry(self.container, font=(FONT, FONT_SIZE, STYLE))
        self.isbn_entry.place(relx=REPORT_ENTRY_BOX_X, rely=0.49, anchor='center',
                                width=REPORT_ENTRY_BOX_WIDTH, height=REPORT_ENTRY_BOX_HEIGHT)

        # Publisher box
        self.publisher_box = Label(self.container, text='Publisher', bg='#71b6df', fg='white', height=3, width=20)
        self.publisher_box.config(font=(FONT, FONT_SIZE, STYLE))
        self.publisher_box.place(relx=MENU_LABEL_X, rely=0.62, anchor='center')
        self.publisher_entry = Entry(self.container, font=(FONT, FONT_SIZE, STYLE))
        self.publisher_entry.place(relx=REPORT_ENTRY_BOX_X, rely=0.62, anchor='center',
                                width=REPORT_ENTRY_BOX_WIDTH, height=REPORT_ENTRY_BOX_HEIGHT)

        # Publication Year box
        self.publication_year_box = Label(self.container, text='Publication Year', bg='#96c4e3', fg='white', height=3, width=20)
        self.publication_year_box.config(font=(FONT, FONT_SIZE, STYLE))
        self.publication_year_box.place(relx=MENU_LABEL_X, rely=0.75, anchor='center')
        self.publication_year_entry = Entry(self.container, font=(FONT, FONT_SIZE, STYLE))
        self.publication_year_entry.place(relx=REPORT_ENTRY_BOX_X, rely=0.75, anchor='center',
                                width=REPORT_ENTRY_BOX_WIDTH, height=REPORT_ENTRY_BOX_HEIGHT)

    def go_to_report(self):
        Report(self.root, self.parent)
        self.container.grid_forget()

    def get_query_parameters(self):
        book_entry = [self.title_entry.get(), self.isbn_entry.get(),
                       self.publication_year_entry.get(), self.publisher_entry.get()]
        book_query_field = ['title', 'isbn', 'publication_year', 'publisher']

        author_entry = [self.author_entry.get()]
        author_query_field = ['author_name']

        book_query = {}
        for entry, field in zip(book_entry, book_query_field):
            if entry != "":
                book_query[field] = entry

        author_query = {}
        for entry, field in zip(author_entry, author_query_field):
            if entry != "":
                author_query[field] = entry

        return book_query, author_query

    def search_books(self):
        book_query, author_query = self.get_query_parameters()

        sql_statement = "SELECT * FROM books"
        keyword = ["WHERE", "AND"]
        keyword_idx = 0
        condition = ""
        if len(author_query) > 0:
            author_conditon = " {} accession_no IN (SELECT book_accession FROM book_author WHERE author_name = '{}')".\
                format(keyword[keyword_idx], author_query['author_name'])
            keyword_idx += 1
            condition += author_conditon

        if len(book_query) > 0:
            for field, value in book_query.items():
                book_condition = " {} {} = '{}'".format(keyword[keyword_idx], field, value)
                if keyword_idx == 0:
                    keyword_idx += 1
                condition += book_condition

        sql_statement += condition

        cursor = self.engine.connect()
        data = cursor.execute(sql_statement).fetchall()
        print(data)
