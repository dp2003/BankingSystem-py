from tkinter import *
from tkinter import messagebox
import mysql.connector

con = mysql.connector.connect(
		host="localhost",
		user="root",
		password="",
		database="bank"
		)
cur= con.cursor()

class Main:	
	def __init__(self,root):
		self.root=root
		self.root.geometry("450x300")
		self.root.title("Welcome to SBMP Bank")
		self.label=Label(root,text="Login For:",font="Times 15 italic")
		self.label.grid(row=0,column=10,padx=20,pady=10)

		bttn1=Button(root,text="Bank Executive",font="Times 15 bold",bg='LightSkyBlue1',command=self.Admin_Login)
		bttn1.grid(row=5,column=15,padx=10,pady=10)

		bttn2=Button(root,text="Customer",font="Times 15 bold",bg='LightSkyBlue1',command=self.Customer_Login)
		bttn2.grid(row=6,column=15,padx=10,pady=10)

	def Admin_Login(self):
		self.root.destroy()
		import AdminLogin

	def Customer_Login(self):
		self.root.destroy()

		import CustomerLogin

root = Tk()
obj = Main(root)
root.mainloop()

