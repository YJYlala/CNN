#import tkinter   两种import 方式不同的区别
from tkinter import  *
master = Tk()
#label 标签组件
show = Label(master,text="JY")
photo = PhotoImage(file="")
show1 = Label(master,image=photo)
show.pack(side="left")
show1.pack(side="left")
#Entry 单行文本组件
eshow = Entry(master,width=100) #创建10个字符宽的单文本输入框
eshow.pack(side="left")
#Text多行文本组件
tshow = Text(master,width=10,height=4)
tshow.pack(side="left")
#checkbutton复选框组件
var = StringVar()  #字符串变量子类，创建对应的实例
cshow = Checkbutton(master,text="选择",variable=var,onvalue="RGB",offvalue="L",fg="blue")
cshow.pack(side="left")
#Radiobutton单选组件
v = IntVar()
rshow = Radiobutton(master,text="one",variable=1,value=1)
rshow.pack(anchor=W)
#Frame 框架组件
fshow = Frame(master,height=200,width=200,bd=1,bg='white',relief=SUNKEN)  #创建框架
fshow.pack(anchor="center")
#labelFrame标签框架组件
LFshow=LabelFrame(master,text="Group",padx=5,pady=5)
LFshow.pack(padx=10,pady=10,expand="yes")
e1=Entry(LFshow,width=10)
e1.pack()
e2=Entry(LFshow,width=10)
e2.pack()
#Listbox列表框组件
lbshow=Listbox(master,bg="yellow",height=5,width=20)
lbshow.pack(side="top")
for item in ["one","two","three","four"]:
    lbshow.insert(END,item)
#Scrollbar滚动条组件
#Scale刻度条组件
#message及button组件
def showMessage(event):
    m1=Message(master,text="非常好！",width=60)  #调用Message组件显示提示信息
    m1.pack()
bshow=Button(master,text="确认",fg="black")
bshow.bind("<Button-1>",showMessage)
bshow.pack(side="left")

#Spinbox组件
sbshow=Spinbox(master,from_=0,to=10)
sbshow.pack(side="left")



master.mainloop()