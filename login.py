from tkinter import *
from tkinter.ttk import *
from sqlite3 import *
from tkinter import messagebox
import home
import cv2
from PIL import Image

class LoginWindow(Tk):
	def __init__(self, *args, **kwargs):
	    Tk.__init__(self, *args, **kwargs)

	    self.title("University Database")
	    self.geometry("400x300")

	    self.style = Style()
	    self.style.configure('Header.TFrame', background = 'blue')

	    self.header_frame = Frame(self, style = 'Header.TFrame')
	    self.header_frame.pack(side = TOP, fill = X)

	    self.style.configure('Header.TLabel', background = 'blue',
	    foreground = 'white', font = (NONE, 25))

	    self.header_label = Label(self.header_frame,
	    style = 'Header.TLabel', text = "Login")
	    self.header_label.pack(pady = 10)

	    self.style.configure('Content.TFrame', background = 'white')

	    self.content_frame = Frame(self, style = 'Content.TFrame')
	    self.content_frame.pack(side = TOP, fill = BOTH, expand = TRUE)

	    self.login_frame = Frame(self.content_frame, style = 'Content.TFrame')
	    self.login_frame.place(relx = .5, rely = .5, anchor = CENTER)

	    self.style.configure('TLabel', background = 'white', font = (NONE, 15))

	    self.username_label = Label(self.login_frame, text = "Username: ")
	    self.username_label.grid(row = 0, column = 0, pady = 5)

	    self.username_entry = Entry(self.login_frame, font = (NONE, 15),
	    width = 15)
	    self.username_entry.grid(row = 0, column = 1)
	    self.username_entry.focus()

	    self.password_label = Label(self.login_frame, text="Password: ")
	    self.password_label.grid(row = 1, column = 0, pady = 5)

	    self.password_entry = Entry(self.login_frame, font = (NONE, 15),
	    width = 15, show = '*')
	    self.password_entry.grid(row = 1, column = 1)

	    self.style.configure('TButton', font = (NONE, 15))

	    self.login_button = Button(self.login_frame, text = "Login",
	    width = 15, command = self.login_button_click)
	    self.login_button.grid(row = 2, column = 1, pady = 5)
	    self.login_button.bind('<Return>', self.login_button_click)

	def login_button_click(self, event = None):
		query = """select * from Login where Username = '%s' and Password = '%s'""" % (self.username_entry.get(),self.password_entry.get())
		con = connect('alldetails.db')
		cur = con.cursor()
		cur.execute(query)
		record = cur.fetchone()
		con.close()
		if record is not None:
			self.destroy()
			home.HomeWindow()
		else:
		    camera_port = 0
		    ramp_frames = 30
		    camera = cv2.VideoCapture(camera_port)

		    def get_image():
		        retval, im = camera.read()
		        return im

		    for i in range(ramp_frames):
		        temp = get_image()
		    print("Taking image..")
		    camera_picture = get_image()
		    file = r"R:\Work\University_Database\Capture.png"
		    cv2.imwrite(file,camera_picture)
		    del(camera)

		    img = Image.open(r"R:\Work\University_Database\Capture.png")
		    img.show()
		    

		    messagebox.showerror("Error Message","Invalid username/password")


if __name__ == '__main__':
    login_window = LoginWindow()
    login_window.mainloop()
