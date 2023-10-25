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

class CustomerSelect:
	def __init__(self,root):
		self.root=root
		self.root.title("Customer")
		self.root.geometry("300x250")

		self.label=Label(root,text="Select Option:",font="Times 15 italic")
		self.label.grid(row=0,column=0,sticky=W+E+N+S,padx=20,pady=10)

		bttn1=Button(root,text="Transaction",font="Times 12 ",bg='LightSkyBlue1',command=self.Withdraw_Deposit,width=10)
		bttn4=Button(root,text="Exit",font="Times 12 ",bg='LightSkyBlue1',command=self.Exit_CustomerSelect,width=10)

	
		bttn1.grid(row=4,column=0,padx=100,pady=10)
		bttn4.grid(row=5,column=0,padx=100,pady=10)

	def Withdraw_Deposit(self):
		self.root.destroy()
		import WithdrawDeposit

	def Exit_CustomerSelect(self):
		self.root.destroy()
		import CustomerSelect

root=Tk()
obj=CustomerSelect(root)
root.mainloop()