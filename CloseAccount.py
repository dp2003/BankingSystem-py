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
class CloseAccount:
	def __init__(self,root):
		self.root=root
		self.root.title("Close Account")
		self.root.geometry("400x200")

		self.label=Label(root,text="Enter Details: ",font="Times 15 italic")
		self.label.grid(row=0,column=0,sticky=W+E+N+S,padx=20,pady=10)

		self.accno=Label(root,text="Enter your Account Number: ",font="Times 12")
		self.accno.grid(row=2,column=0,sticky=W+E+N+S,padx=20,pady=10)
		self.in_accno=Entry(root)
		self.in_accno.grid(row=2,column=1,sticky=W+E+N+S,padx=20,pady=10)

		bttn1=Button(root,text="Delete",font="Times 10 bold",bg='LightSkyBlue1',command=self.Close)
		bttn2=Button(root,text="Exit",font="Times 10 bold",bg='LightSkyBlue1',command=self.CloseExit)

		bttn1.grid(row=9,column=0,padx=20,pady=10)
		bttn2.grid(row=9,column=1,padx=20,pady=10)

	def Close(self):
		#print(self.in_fname.get())
		#print(self.in_accno.get())
		if self.in_accno.get()=="":
			messagebox.showerror("Error","Error all fields are required")
		else:
			try:
				cur.execute("DELETE from customer where AccountNo = " + self.in_accno.get())
				con.commit()
				con.close()
				messagebox.showinfo("Closed","Your Account has been closed!")
				self.root.destroy()
				import AdminSelect
			except Exception as es:
				messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root)

	def CloseExit(self):
		pass 

root=Tk()
obj=CloseAccount(root)
root.mainloop()