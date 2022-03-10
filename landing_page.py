from tkinter import Label, Button

from apps.resources.variables import *
from apps.resources.container import Container
from apps.report.report_pages import Report
from apps.member.member_landing import Membership


class LandingPage(Container):
    def __init__(self, root, parent, engine):
        super().__init__(root, 'Library System Landing Page')
        self.init_image()
        self.parent = parent
        self.engine = engine

        # reports option
        self.landing_report_image = self.open_image('apps/resources/reports.png', LANDING_PAGE_ICON_SIZE,
                                                    LANDING_PAGE_ICON_SIZE)
        self.report_button = Button(root, image=self.landing_report_image, command=self.go_to_report)
        self.report_button.place(relx=0.7, rely=0.7, anchor='center')
        self.report_text = Label(root, text='Reports', font=(FONT, LANDING_PAGE_FONT_SIZE, STYLE),
                                 fg='black',
                                 bg='white')
        self.report_text.place(relx=0.7, rely=0.9, anchor='center')

        # Membership option
        self.landing_member_image = self.open_image('apps/resources/reports.png', LANDING_PAGE_ICON_SIZE,
                                            LANDING_PAGE_ICON_SIZE)
        self.member_button = Button(root, image=self.landing_report_image, command=self.go_to_member)
        self.member_button.place(relx=0.2, rely=0.2, anchor='center')
        self.member_text = Label(root, text='Membership', font=(FONT, LANDING_PAGE_FONT_SIZE, STYLE),
                                 fg='black',
                                 bg='white')
        self.member_text.place(relx=0.2, rely=0.4, anchor='center')

    def go_to_report(self):
        Report(self.root, self.parent, self.engine)
        self.container.grid_forget()

    def go_to_member(self):
        Membership(self.root, self.parent, self.engine)
        self.container.grid_forget()