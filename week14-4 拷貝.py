import tkinter as tk
import tkinter.font as tkFont
import math
from PIL import Image
from PIL import ImageTk
class Calculator(tk.Frame):
	shouldreset = True

	def setNumstr(self,content):
		if self.shouldreset == True :
			self.txtNum.delete("1.0",tk.END)
			self.txtNum.insert("1.0",content)
			self.shouldreset=False
		else : 
			self.txtNum.insert(tk.END,content)

	def __init__(self):
		tk.Frame.__init__(self)
		self.grid()
		self.createWidgets()
	def createWidgets(self):
		f1=tkFont.Font(size=48,family="Skia")
		f2=tkFont.Font(size=32,family="Skia")

		self.txtNum = tk.Text(self,height=1,width=7,font=f1)

		self.btnNum1 =tk.Button(self,text="1",command=self.clickBtnNum1,height=1,width=2,font=f2)
		self.btnNum2 =tk.Button(self,text="2",command=self.clickBtnNum2,height=1,width=2,font=f2)
		self.btnNum3 =tk.Button(self,text="3",command=self.clickBtnNum3,height=1,width=2,font=f2)
		self.btnNum4 =tk.Button(self,text="4",command=self.clickBtnNum4,height=1,width=2,font=f2)
		self.btnNum5 =tk.Button(self,text="5",command=self.clickBtnNum5,height=1,width=2,font=f2)
		self.btnNum6 =tk.Button(self,text="6",command=self.clickBtnNum6,height=1,width=2,font=f2)
		self.btnNum7 =tk.Button(self,text="7",command=self.clickBtnNum7,height=1,width=2,font=f2)
		self.btnNum8 =tk.Button(self,text="8",command=self.clickBtnNum8,height=1,width=2,font=f2)
		self.btnNum9 =tk.Button(self,text="9",command=self.clickBtnNum9,height=1,width=2,font=f2)
		self.btnNum0 =tk.Button(self,text="0",command=self.clickBtnNum0,height=1,width=2,font=f2)
		self.btnsqrt =tk.Button(self,text="s",command=self.clickBtnsqrt,height=1,width=2,font=f2)

		image = Image.open("Image002.png")
		image = image.resize((25, 25), Image.ANTIALIAS) #The (250, 250) is (height, width)
		self.imageSqrt = ImageTk.PhotoImage(image)
		# self.imageSqrt = ImageTk.PhotoImage(file="Image002.png",size=1*1)
		self.btnsqrt=tk.Button(self,image=self.imageSqrt,command=self.clickBtnsqrt)
		
		self.txtNum.grid(row=0,column=0,columnspan=3,sticky=tk.NE+tk.SW)

		self.btnNum1.grid(row=1,column=0,sticky=tk.NE+tk.SW)
		self.btnNum2.grid(row=1,column=1,sticky=tk.NE+tk.SW)
		self.btnNum3.grid(row=1,column=2,sticky=tk.NE+tk.SW)
		self.btnNum4.grid(row=2,column=0,sticky=tk.NE+tk.SW)
		self.btnNum5.grid(row=2,column=1,sticky=tk.NE+tk.SW)
		self.btnNum6.grid(row=2,column=2,sticky=tk.NE+tk.SW)
		self.btnNum7.grid(row=3,column=0,sticky=tk.NE+tk.SW)
		self.btnNum8.grid(row=3,column=1,sticky=tk.NE+tk.SW)
		self.btnNum9.grid(row=3,column=2,sticky=tk.NE+tk.SW)
		self.btnNum0.grid(row=4,column=0,columnspan=2,sticky=tk.NE+tk.SW)
		self.btnsqrt.grid(row=4,column=2,sticky=tk.NE+tk.SW)

		



	def clickBtnNum1(self):
		self.setNumstr("1")
	def clickBtnNum2(self):
		self.setNumstr("2")
	def clickBtnNum3(self):
		self.setNumstr("3")
	def clickBtnNum4(self):
		self.setNumstr("4")
	def clickBtnNum5(self):
		self.setNumstr("5")
	def clickBtnNum6(self):
		self.setNumstr("6")
	def clickBtnNum7(self):
		self.setNumstr("7")
	def clickBtnNum8(self):
		self.setNumstr("8")
	def clickBtnNum9(self):
		self.setNumstr("9")
	def clickBtnNum0(self):
		self.setNumstr("0")

	def clickBtnsqrt(self):
		curNum = float(self.txtNum.get("1.0",tk.END))
		self.txtNum.delete("1.0",tk.END)
		self.txtNum.insert("1.0",str(round(math.sqrt(curNum),2)))
		self.shouldreset=True

	




cal=Calculator()
cal.master.title("My Calculator")
cal.mainloop()

