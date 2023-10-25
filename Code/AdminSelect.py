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

class AdminSelect:
	def __init__(self,root):
		self.root=root
		self.root.title("Admin")
		self.root.geometry("350x350")

		self.label=Label(root,text="Select Option: ",font="Times 15 italic")
		self.label.grid(row=0,column=0,padx=20,pady=10)

		bttn1=Button(root,text="Create New Bank Accout",font="Times 12 ",bg='LightSkyBlue1',command=self.Create_Account)
		bttn2=Button(root,text="Close Bank Account",font="Times 12 ",bg='LightSkyBlue1',command=self.Close_Account)
		bttn3=Button(root,text="All Account Holder List",font="Times 12 ",bg='LightSkyBlue1',command=self.ShowData)
		bttn4=Button(root,text="Exit",font="Times 12 ",bg='LightSkyBlue1',command=self.Exit_AdminSelect)
  

		bttn1.grid(row=4,column=0,padx=100,pady=10)
		bttn2.grid(row=5,column=0,padx=100,pady=10)
		bttn3.grid(row=6,column=0,padx=100,pady=10)
		bttn4.grid(row=7,column=0,padx=100,pady=10)

	def Create_Account(self):
		self.root.destroy()
		import CreateAccount

	def Close_Account(self):
		self.root.destroy()
		import CloseAccount

	def ShowData(self):
		self.root.destroy()
		import ShowData

	def Exit_AdminSelect(self):
		self.root.destroy()
		import AdminLogin

root=Tk()
obj=AdminSelect(root)
root.mainloop()
