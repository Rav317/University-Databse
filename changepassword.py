from tkinter import *
from tkinter.ttk import *
from sqlite3 import *
from tkinter import messagebox

class ChangePasswordFrame(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.style = Style()

        self.style.configure('TFrame', background = 'white')

        self.place(relx = .5, rely = .5, anchor = CENTER)

        self.style.configure('TLabel', background = 'white', font = (NONE, 15))

        self.old_password_label = Label(self, text = "Old Password:")
        self.old_password_label.grid(row = 0, column = 0, pady = 10, sticky = W)

        self.old_password_entry = Entry(self, show = '*', font = (NONE, 15))
        self.old_password_entry.grid(row = 0, column = 1)

        self.new_password_label = Label(self, text = "New Password:")
        self.new_password_label.grid(row = 1, column = 0, pady = 10, sticky = W)

        self.new_password_entry = Entry(self, show = '*', font = (NONE, 15))
        self.new_password_entry.grid(row = 1, column = 1)

        self.confirm_password_label = Label(self, text = "Confirm Password:")
        self.confirm_password_label.grid(row = 2, column = 0, pady = 10, sticky = W)

        self.confirm_password_entry = Entry(self, show = '*', font = (NONE, 15))
        self.confirm_password_entry.grid(row = 2, column = 1)

        self.style.configure('TButton', font = (NONE, 15))

        self.change_password_button = Button(self, text = "Change Password",
        width = 20, command = self.change_password_button_click)
        self.change_password_button.grid(row = 3, column = 1, pady = 10)

    def change_password_button_click(self):
        query = """select * from Login where 
        Password = '%s'""" % (self.old_password_entry.get())

        con = connect('alldetails.db')
        cur = con.cursor()
        cur.execute(query)
        record = cur.fetchone()

        if record is not None:
            new_password = self.new_password_entry.get()
            confirm_password = self.confirm_password_entry.get()
            if new_password == confirm_password:
                query = """update Login set Password = '%s'  
                """ % (self.new_password_entry.get())
                cur.execute(query)
                con.commit()
                messagebox.showinfo('Success Message', 'Password is changed successfully')
            else:
                messagebox.showerror('Error Message',
                'New password and confirm password did not match')
        else:
            messagebox.showerror('Error Message', 'Incorrect old password')
        con.close()




