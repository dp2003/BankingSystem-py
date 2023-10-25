from tkinter import*
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk

import mysql.connector

con = mysql.connector.connect(
		host="localhost",
		user="root",
		password="",
		database="bank"
		)
cur= con.cursor()

class ShowData:
	def __init__(self,root):
		self.root=root
		self.root.title("List")
		self.root.geometry("1100x500")

		cur.execute("Select * from customer")

		self.tree=ttk.Treeview(self.root)

		self.tree['show']='headings'

		self.tree["columns"]=("id","FullName","Age","Address","Mobile","Occupation","AccountNo","AccountType","Balance")

		self.tree.column("id",width=100,minwidth=100,anchor=tk.CENTER)
		self.tree.column("FullName",width=150,minwidth=150,anchor=tk.CENTER)
		self.tree.column("Age",width=50,minwidth=50,anchor=tk.CENTER)
		self.tree.column("Address",width=200,minwidth=200,anchor=tk.CENTER)
		self.tree.column("Mobile",width=80,minwidth=80,anchor=tk.CENTER)
		self.tree.column("Occupation",width=150,minwidth=150,anchor=tk.CENTER)
		self.tree.column("AccountNo",width=80,minwidth=80,anchor=tk.CENTER)
		self.tree.column("AccountType",width=100,minwidth=100,anchor=tk.CENTER)
		self.tree.column("Balance",width=100,minwidth=100,anchor=tk.CENTER)

		self.tree.heading("id",text="ID",anchor=tk.CENTER)
		self.tree.heading("FullName",text="Full Name",anchor=tk.CENTER)
		self.tree.heading("Age",text="Age",anchor=tk.CENTER)
		self.tree.heading("Address",text="Address",anchor=tk.CENTER)
		self.tree.heading("Mobile",text="Mobile No.",anchor=tk.CENTER)
		self.tree.heading("Occupation",text="Occupation",anchor=tk.CENTER)
		self.tree.heading("AccountNo",text="Account Number",anchor=tk.CENTER)
		self.tree.heading("AccountType",text="Account Type",anchor=tk.CENTER)
		self.tree.heading("Balance",text="Balance",anchor=tk.CENTER)	

		i=0
		for ro in cur:
			self.tree.insert('',i,text="",values=(ro[0],ro[1],ro[2],ro[3],ro[4],ro[5],ro[6],ro[7],ro[8]))
			i=i+1

		self.tree.pack()

		bttn=Button(root,text="Exit",font="Times 15 bold",bg='LightSkyBlue1',command=self.ExitData,width=10)
		bttn.pack()

	def ExitData(self):
		self.root.destroy()
		import AdminSelect



root=Tk()
obj=ShowData(root)
root.mainloop()




