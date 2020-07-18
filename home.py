from tkinter import *
from tkinter.ttk import *
import changepassword
import login
import managedetails

class HomeWindow(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        self.title("Home")
        self.geometry("1200x600")

        self.style = Style()

        self.style.configure('Header.TFrame', background = 'blue')

        self.header_frame = Frame(self, style = 'Header.TFrame')
        self.header_frame.pack(side = TOP, fill = X)

        self.style.configure('Header.TLabel', background = 'blue',
        foreground = 'white', font = (NONE, 25))

        self.header_label = Label(self.header_frame, text = "University Database",
        style = 'Header.TLabel')
        self.header_label.pack(pady = 10)

        self.navigation_frame = Frame(self, style = 'Header.TFrame')
        self.navigation_frame.pack(side = LEFT, fill = Y)

        self.style.configure('Navigation.TButton', font = (NONE, 15),
        width = 20)

        self.manage_details_button = Button(self.navigation_frame,
        style = 'Navigation.TButton', text = "Manage Details",
        command = self.manage_details_button_click)
        self.manage_details_button.pack(pady = 1, ipady = 10)

        self.change_password_button = Button(self.navigation_frame,
        style='Navigation.TButton', text="Change Password",
        command = self.change_password_button_click)
        self.change_password_button.pack(pady = 1, ipady = 10)

        self.logout_button = Button(self.navigation_frame,
        style='Navigation.TButton', text="Logout",
        command = self.logout_button_click)
        self.logout_button.pack(pady = 1, ipady = 10)

        self.style.configure('Content.TFrame', background = 'white')

        self.content_frame = Frame(self, style = 'Content.TFrame')
        self.content_frame.pack(side = TOP, fill = BOTH, expand = TRUE)

        managedetails.ManageDetailsFrame(self.content_frame)

    def manage_details_button_click(self):
        for inner_frame in self.content_frame.winfo_children():
            inner_frame.destroy()
        managedetails.ManageDetailsFrame(self.content_frame)

    def change_password_button_click(self):
        for inner_frame in self.content_frame.winfo_children():
            inner_frame.destroy()
        changepassword.ChangePasswordFrame(self.content_frame)

    def logout_button_click(self):
        self.destroy()
        login.LoginWindow()
