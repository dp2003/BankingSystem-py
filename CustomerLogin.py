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
class CustomerLogin:
	def __init__(self,root):
		self.root=root
		self.root.title("Customer Login")
		self.root.geometry("400x200")

		self.label=Label(root,text="Enter Your Credentials:",font="Times 15 italic")
		self.label.grid(row=0,column=0,sticky=W+E+N+S,padx=20,pady=10)

		self.l1=Label(root,text="User ID:",font="Times 12")
		self.l2=Label(root,text="Password:",font="Times 12")

		self.l1.grid(row=1,column=0,sticky=W+E+N+S,padx=20,pady=10)
		self.l2.grid(row=2,column=0,sticky=W+E+N+S,padx=20,pady=10)

		self.e3=Entry(root)
		self.e4=Entry(root)

		self.e3.grid(row=1,column=1,sticky=W+E+N+S,padx=20,pady=10)
		self.e4.grid(row=2,column=1,sticky=W+E+N+S,padx=20,pady=10)

		bttn3=Button(root,text="Back",font="Times 10 bold",bg='LightSkyBlue1',command=self.BackCust)
		bttn4=Button(root,text="Login",font="Times 10 bold",bg='LightSkyBlue1',command=self.CustomerCheck)

		bttn3.grid(row=4,column=0,padx=20,pady=10)
		bttn4.grid(row=4,column=1,padx=20,pady=10)
	def CustomerCheck(self):
		if self.e3.get()=="" or self.e4.get()=="":
			messagebox.showerror("Error","Please enter all the credentials!!",parent=self.root)
		else:
			try:
				cur.execute("select * from Customer where CustUser=%s and CustPass=%s",(self.e3.get(),self.e4.get()))
				row=cur.fetchone()
				if row == None:
					messagebox.showerror("Error","Invalid Username and Password",parent=self.root)
				else:
					messagebox.showinfo("Welcome","Login Successfulll!!",parent=self.root)	
					self.root.destroy()
					import CustomerSelect	
			except Exception as es:
				messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root)

	def BackCust(self):
		self.root.destroy()
		import Miniproject
root=Tk()
obj=CustomerLogin(root)
root.mainloop()