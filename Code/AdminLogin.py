from tkinter import*
from tkinter import messagebox
import mysql.connector

con = mysql.connector.connect(
		host="localhost",
		user="root",
		password="",
		database="bank"
		)
cur= con.cursor()

class AdminLogin:
	def __init__(self,root):
		self.root=root
		self.root.title("Admin Login")
		self.root.geometry("400x200")
		
		self.label=Label(root,text="Enter Your Credentials:",font="Times 15 italic")
		self.label.grid(row=0,column=0,sticky=W+E+N+S,padx=20,pady=10)

		self.l1=Label(root,text="Admin ID:",font="Times 12")
		self.l2=Label(root,text="Password:",font="Times 12")

		self.l1.grid(row=1,column=0,sticky=W+E+N+S,padx=20,pady=10)
		self.l2.grid(row=2,column=0,sticky=W+E+N+S,padx=20,pady=10)

		self.e1=Entry(root)
		self.e2=Entry(root)

		self.e1.grid(row=1,column=1,sticky=W+E+N+S,padx=20,pady=10)
		self.e2.grid(row=2,column=1,sticky=W+E+N+S,padx=20,pady=10)


		bttn1=Button(root,text="Back",font="Times 10 bold",bg='LightSkyBlue1',command=self.BackAdmin)
		bttn2=Button(root,text="Login",font="Times 10 bold",bg='LightSkyBlue1',command=self.AdminCheck)

		bttn1.grid(row=4,column=0,padx=20,pady=10)
		bttn2.grid(row=4,column=1,padx=20,pady=10)

	def AdminCheck(self):
		if self.e1.get()=="" or self.e2.get()=="":
			messagebox.showerror("Error","Please enter all the credentials!!",parent=self.root)
		else:
			try:
				cur.execute("select * from adminlogin where AdminUser=%s and AdminPass=%s",(self.e1.get(),self.e2.get()))
				row=cur.fetchone()
				if row == None:
					messagebox.showerror("Error","Invalid Username and Password",parent=self.root)
				else:
					messagebox.showinfo("Welcome","Login Successfulll!!",parent=self.root)
					self.root.destroy()
					import AdminSelect
			except Exception as es:
				messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root)

	def BackAdmin(self):
		self.root.destroy()
		import Miniproject

root=Tk()
obj=AdminLogin(root)
root.mainloop()