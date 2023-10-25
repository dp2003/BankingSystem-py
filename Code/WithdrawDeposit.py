from tkinter import*
from tkinter import messagebox
import mysql.connector

class WithdrawDeposit:
	def __init__(self,root):
		self.bal=0
		self.root=root
		self.root.title("Deposit and Withdraw")
		self.root.geometry("550x310")

		self.label=Label(root,text="Perform Transactions:",font="Times 15 italic")
		self.label.grid(row=0,column=0,sticky=W+E+N+S,padx=20,pady=10)

		self.depositWithdraw=Label(root,text="Enter Amount to Diposit/Withdraw : ",font="Times 12")
		self.current_bal=Label(root,text="Current Balance:",font="Times 12")

		self.depositWithdraw.grid(row=2,column=0,sticky=W+E+N+S,padx=20,pady=10)
		self.current_bal.grid(row=3,column=0,sticky=W+E+N+S,padx=20,pady=10)

		self.in_depositWithdraw=Entry(root)
		self.in_depositWithdraw.grid(row=2,column=1,sticky=W+E+N+S,padx=20,pady=10)
		
		self.in_current_bal=Entry()
		self.in_current_bal.grid(row=3,column=1,sticky=W+E+N+S,padx=20,pady=10)


		bttn1=Button(root,text="Withdraw",font="Times 10 bold",bg='LightSkyBlue1',width=10,command=self.Withdraw)
		bttn2=Button(root,text="Deposit",font="Times 10 bold",bg='LightSkyBlue1',width=10,command=self.Deposit)
		bttn3=Button(root,text="Clear",font="Times 10 bold",bg='LightSkyBlue1',width=10,command=self.Clear)
		bttn4=Button(root,text="Exit",font="Times 10 bold",bg='LightSkyBlue1',width=10)

		bttn1.grid(row=9,column=0,padx=10,pady=10)
		bttn2.grid(row=9,column=2,padx=10,pady=10)
		bttn3.grid(row=10,column=0,padx=10,pady=10)
		bttn4.grid(row=10,column=2,padx=10,pady=10)

	def Deposit(self):
		if self.in_depositWithdraw.get()=="":
			messagebox.showerror("Error","Please enter the amount!!",parent=self.root)
		else:
			self.dep=float(self.in_depositWithdraw.get())

			self.result=self.bal+self.dep

			self.in_current_bal.insert(0,str(self.result))

	def Withdraw(self):
		self.curr_bal=self.in_current_bal.get()
		self.withdraw=float(self.in_depositWithdraw.get())
		if self.bal<self.withdraw:
			messagebox.showerror("Error","Not Enough Money to Withdraw",parent=self.root)
		else:
			self.result=self.curr_bal-self.withdraw
			self.in_current_bal.insert(0,str(self.result))
			self.in_current_bal.config(state=DISABLED)

	def Clear(self):
		self.in_depositWithdraw.delete(0,END)
	


			
root=Tk()
obj=WithdrawDeposit(root)
root.mainloop()