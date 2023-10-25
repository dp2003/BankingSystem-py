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

class CreateAccount:
	def __init__(self,root):
		self.root=root
		self.root.title("Admin")
		self.root.geometry("450x600")
		self.label=Label(root,text="Enter Details: ",font="Times 15 italic")
		self.label.grid(row=0,column=0,sticky=W+E+N+S,padx=20,pady=10)

		self.fname=Label(root,text="Enter your Full Name:",font="Times 12")
		self.age=Label(root,text="Enter your Age:",font="Times 12")
		self.add=Label(root,text="Enter your Address:",font="Times 12")
		self.mobno=Label(root,text="Enter your Mobile no.:",font="Times 12")
		self.occp=Label(root,text="Enter your Occupation:",font="Times 12")
		self.accno=Label(root,text="Enter Account Number:",font="Times 12")
		self.acctype=Label(root,text="Enter Account Type (Current/Saving):",font="Times 12")
		self.bal=Label(root,text="Enter Current Balance:",font="Times 12")
		self.custlogin=Label(root,text="Enter Username:",font="Times 12")
		self.custpass=Label(root,text="Enter Pin:",font="Times 12")

		self.fname.grid(row=1,column=0,sticky=W+E+N+S,padx=20,pady=10)
		self.age.grid(row=2,column=0,sticky=W+E+N+S,padx=20,pady=10)
		self.add.grid(row=3,column=0,sticky=W+E+N+S,padx=20,pady=10)
		self.mobno.grid(row=4,column=0,sticky=W+E+N+S,padx=20,pady=10)
		self.occp.grid(row=5,column=0,sticky=W+E+N+S,padx=20,pady=10)
		self.accno.grid(row=6,column=0,sticky=W+E+N+S,padx=20,pady=10)
		self.acctype.grid(row=7,column=0,sticky=W+E+N+S,padx=20,pady=10)
		self.bal.grid(row=8,column=0,sticky=W+E+N+S,padx=20,pady=10)
		self.custlogin.grid(row=9,column=0,sticky=W+E+N+S,padx=20,pady=10)
		self.custpass.grid(row=10,column=0,sticky=W+E+N+S,padx=20,pady=10)

		self.in_fname=Entry(root)
		self.in_age=Entry(root)
		self.in_add=Entry(root)
		self.in_mobno=Entry(root)
		self.in_occp=Entry(root)
		self.in_accno=Entry(root)
		self.in_acctype=Entry(root)
		self.in_bal=Entry(root)
		self.in_custlogin=Entry(root)
		self.in_custpass=Entry(root)




		self.in_fname.grid(row=1,column=1,sticky=W+E+N+S,padx=20,pady=10)
		self.in_age.grid(row=2,column=1,sticky=W+E+N+S,padx=20,pady=10)
		self.in_add.grid(row=3,column=1,sticky=W+E+N+S,padx=20,pady=10)
		self.in_mobno.grid(row=4,column=1,sticky=W+E+N+S,padx=20,pady=10)
		self.in_occp.grid(row=5,column=1,sticky=W+E+N+S,padx=20,pady=10)
		self.in_accno.grid(row=6,column=1,sticky=W+E+N+S,padx=20,pady=10)
		self.in_acctype.grid(row=7,column=1,sticky=W+E+N+S,padx=20,pady=10)
		self.in_bal.grid(row=8,column=1,sticky=W+E+N+S,padx=20,pady=10)
		self.in_custlogin.grid(row=9,column=1,sticky=W+E+N+S,padx=20,pady=10)
		self.in_custpass.grid(row=10,column=1,sticky=W+E+N+S,padx=20,pady=10)

		save=Button(root,text="Save/Create",font="Times 10 bold",bg='LightSkyBlue1',command=self.Create)
		exit=Button(root,text="Exit",font="Times 10 bold",bg='LightSkyBlue1',command=self.Exit_CreateAccount)

		save.grid(row=11,column=0,padx=20,pady=10)
		exit.grid(row=12,column=0,padx=20,pady=10)
	def Create(self):
		if self.in_fname.get()=="" or self.in_age.get()=="" or self.in_add.get()=="" or self.in_mobno=="" or self.in_occp=="" or self.in_accno=="" or self.in_acctype=="" or self.in_bal=="":
			messagebox.showerror("Error","Error All Fields are required",parent=self.root)
		else:
			try:
				cur.execute("insert into customer (FullName,Age,Address,Mobile,Occupation,AccountNo,AccountType,Balance,CustUser,CustPass) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
				(self.in_fname.get(),
				self.in_age.get(),
				self.in_add.get(),
				self.in_mobno.get(),
				self.in_occp.get(),
				self.in_accno.get(),
				self.in_acctype.get(),
				self.in_bal.get(),
				self.in_custlogin.get(),
				self.in_custpass.get()
							))
				con.commit()
				con.close()
				messagebox.showinfo("Success","Account Created")
			except Exception as es:
				messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root)
	def Exit_CreateAccount(self):
		self.root.destroy()
		import AdminSelect
		
root=Tk()
obj=CreateAccount(root)
root.mainloop()
