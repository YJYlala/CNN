from tkinter import *
from tkinter import ttk
import  time
root=Tk()
root.title("Progressbar组件案例")
root.geometry("200x150")
p1=ttk.Progressbar(root,length=200,mode="determinate",orient=HORIZONTAL)  #创建进度条实例  orient=HORIZONTAL横向显示进度条或者 VERTICAL竖向显示进度条
p1.grid(row=1,column=1)   #使用grid精确设置进度条在窗体上的位置
p1["maximum"]=100         #进度条实际最大进度数
p1["value"]=0             #设置进度条实际进度值
for i in range(100):
    p1["value"]=i+1
    root.update()        #更新一次进度
    time.sleep(0.1)         #循环一次，让进程暂停0.1s
root.mainloop()