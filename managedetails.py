from tkinter import *
from tkinter.ttk import *
from sqlite3 import *
from tkinter import messagebox

class ManageDetailsFrame(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.style = Style()

        self.style.configure('TFrame', background = 'white')

        self.pack(side = TOP, fill = BOTH, expand = TRUE)

        self.con = connect('alldetails.db')
        self.cur = self.con.cursor()

        self.create_view_details_frame()

    def create_view_details_frame(self):
        self.view_details_frame = Frame(self)
        self.view_details_frame.place(relx=.5, rely=.5, anchor=CENTER)

        self.style.configure('TButton', font=(NONE, 15))

        self.add_new_detail_button = Button(self.view_details_frame,
        text = "Add New Detail", width = 20,
        command = self.add_new_detail_button_click)
        self.add_new_detail_button.grid(row=0, column=0,
        columnspan=2, sticky=E, pady=25)

        self.style.configure('TLabel', background = 'white', font = (NONE, 15))

        self.name_label = Label(self.view_details_frame, text = "Name:")
        self.name_label.grid(row=1, column=0, sticky=W, pady=10)

        self.name_entry = Entry(self.view_details_frame, font = (NONE, 15),
        width = 75)
        self.name_entry.grid(row=1, column=1)
        self.name_entry.bind('<KeyRelease>', self.name_entry_text_changed)

        self.style.configure('Treeview.Heading', font=(NONE, 15))
        self.style.configure('Treeview', font = (NONE, 15))

        self.details_treeview = Treeview(self.view_details_frame,
        columns = ('Name', 'MobileNo', 'SRN', 'City'), show = 'headings')
        self.details_treeview.grid(row=2, column=0, columnspan=2,pady=10)
        self.details_treeview.heading('Name', text="Name", anchor=W)
        self.details_treeview.heading('MobileNo', text="Mobile No", anchor=W)
        self.details_treeview.heading('SRN', text="SRN", anchor=W)
        self.details_treeview.heading('City', text="City", anchor=W)
        self.details_treeview.column('Name', width=300)
        self.details_treeview.column('MobileNo', width=250)
        self.details_treeview.column('SRN', width=200)
        self.details_treeview.column('City', width=150)
        self.details_treeview.bind('<<TreeviewSelect>>',
        self.details_treeview_selection)

        query = "select * from Details"
        self.fill_details_treeview(query)

    def details_treeview_selection(self, event):
        contact = self.details_treeview.item(
        self.details_treeview.selection())['values']
        self.view_details_frame.destroy()
        self.create_update_delete_detail_frame(contact)

    def name_entry_text_changed(self, event):
        query = """select * from Details 
        where name like '%{0}%'
        """.format(self.name_entry.get())
        self.fill_details_treeview(query)

    def fill_details_treeview(self, query):
        for detail in self.details_treeview.get_children():
            self.details_treeview.delete(detail)

        self.cur.execute(query)
        details = self.cur.fetchall()

        for detail in details:
            self.details_treeview.insert("", END, values=detail)

    def add_new_detail_button_click(self):
        self.view_details_frame.destroy()
        self.create_add_new_detail_frame()

    def create_add_new_detail_frame(self):
        self.add_new_detail_frame = Frame(self)
        self.add_new_detail_frame.place(relx=.5, rely=.5, anchor=CENTER)

        self.style.configure('TLabel', background='white', font=(NONE, 15))

        self.name_label = Label(self.add_new_detail_frame, text="Name:")
        self.name_label.grid(row=0, column=0, pady=10, sticky=W)

        self.name_entry = Entry(self.add_new_detail_frame, font=(NONE, 15),
        width=30)
        self.name_entry.grid(row=0, column=1)

        self.mobile_no_label = Label(self.add_new_detail_frame, text="Mobile No:")
        self.mobile_no_label.grid(row=1, column=0, pady=10, sticky=W)

        self.mobile_no_entry = Entry(self.add_new_detail_frame, font=(NONE, 15),
        width=30)
        self.mobile_no_entry.grid(row=1, column=1)

        self.srn_label = Label(self.add_new_detail_frame, text="SRN:")
        self.srn_label.grid(row=2, column=0, pady=10, sticky=W)

        self.srn_entry = Entry(self.add_new_detail_frame, font=(NONE, 15),
        width=30)
        self.srn_entry.grid(row=2, column=1)

        self.city_label = Label(self.add_new_detail_frame, text="City:")
        self.city_label.grid(row=3, column=0, pady=10, sticky=W)

        self.city_combobox = Combobox(self.add_new_detail_frame, state='readonly',
        values=('Noida', 'Greater Noida', 'Delhi', 'Mumbai', 'Banglore','Chennai','Pune','Chandigarh','Gurugram','Hyderabad','Kolkata','Jaipur'),
        font=(NONE, 15), width=29)
        self.city_combobox.current(0)
        self.city_combobox.grid(row=3, column=1)

        self.style.configure('TButton', font=(NONE, 15))

        self.add_button = Button(self.add_new_detail_frame, text="Add",
        width=30, command=self.add_button_click)
        self.add_button.grid(row=4, column=1, pady=10)

    def add_button_click(self):
        query = """select * from Details
        where SRN = '%s'""" % (self.srn_entry.get())
        self.cur.execute(query)
        record = self.cur.fetchone()
        if record is None:
            query = """insert into Details 
            values('%s', '%s', '%s', '%s')""" % (
            self.name_entry.get(), self.mobile_no_entry.get(),
            self.srn_entry.get(), self.city_combobox.get())
            self.cur.execute(query)
            self.con.commit()
            messagebox.showinfo('Success Message',
            'Details are saved successfully')
            self.add_new_detail_frame.destroy()
            self.create_view_details_frame()
        else:
            messagebox.showerror('Error Message',
            'Student of SRN ' + self.srn_entry.get() + ' is already added')

    def create_update_delete_detail_frame(self, detail):
        self.update_delete_detail_frame = Frame(self)
        self.update_delete_detail_frame.place(relx=.5, rely=.5, anchor=CENTER)

        self.style.configure('TLabel', background='white', font=(NONE, 15))

        self.name_label = Label(self.update_delete_detail_frame, text="Name:")
        self.name_label.grid(row=0, column=0, pady=10, sticky=W)

        self.name_entry = Entry(self.update_delete_detail_frame, font=(NONE, 15),
        width=30)
        self.name_entry.grid(row=0, column=1, columnspan=2)
        self.name_entry.insert(END, detail[0])

        self.mobile_no_label = Label(self.update_delete_detail_frame,
        text="Mobile No:")
        self.mobile_no_label.grid(row=1, column=0, pady=10, sticky=W)

        self.mobile_no_entry = Entry(self.update_delete_detail_frame, font=(NONE, 15),
        width=30)
        self.mobile_no_entry.grid(row=1, column=1, columnspan=2)
        self.mobile_no_entry.insert(END, detail[1])

        self.srn_label = Label(self.update_delete_detail_frame, text="Email Id:")
        self.srn_label.grid(row=2, column=0, pady=10, sticky=W)

        self.srn_entry = Entry(self.update_delete_detail_frame, font=(NONE, 15),
        width=30)
        self.srn_entry.grid(row=2, column=1, columnspan=2)
        self.srn_entry.insert(END, detail[2])
        self.old_srn = detail[2]

        self.city_label = Label(self.update_delete_detail_frame, text="City:")
        self.city_label.grid(row=3, column=0, pady=10, sticky=W)

        self.city_combobox = Combobox(self.update_delete_detail_frame, state='readonly',
        values=('Noida', 'Greater Noida', 'Delhi', 'Mumbai', 'Banglore','Chennai','Pune','Chandigarh','Gurugram','Hyderabad','Kolkata','Jaipur'),
        font=(NONE, 15), width=29)
        self.city_combobox.current(0)
        self.city_combobox.grid(row=3, column=1, columnspan=2)
        self.city_combobox.set(detail[3])

        self.style.configure('TButton', font=(NONE, 15))

        self.update_button = Button(self.update_delete_detail_frame,
        text="Update", width=14, command = self.update_button_click)
        self.update_button.grid(row=4, column=1, pady=10)

        self.delete_button = Button(self.update_delete_detail_frame,
        text="Delete", width=14, command = self.delete_button_click)
        self.delete_button.grid(row=4, column=2, pady=10)

    def update_button_click(self):
        query = """update Details set Name = '{0}', MobileNo = '{1}',
        SRN = '{2}', City = '{3}' where SRN = '{4}' 
        """.format(self.name_entry.get(), self.mobile_no_entry.get(),
        self.srn_entry.get(), self.city_combobox.get(),
        self.old_srn)
        self.cur.execute(query)
        self.con.commit()
        messagebox.showinfo('Success Message',
        'Details are updated successfully')
        self.update_delete_detail_frame.destroy()
        self.create_view_details_frame()

    def delete_button_click(self):
        if messagebox.askquestion("Confirmation Message",
        "Are you sure to delete?") == 'yes':
            query = """delete from Details 
            where SRN = '{0}'""".format(self.old_srn)
            self.cur.execute(query)
            self.con.commit()
            messagebox.showinfo('Success Message',
            'Details are deleted successfully')
        self.update_delete_detail_frame.destroy()
        self.create_view_details_frame()

