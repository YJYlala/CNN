import tkinter            #导入tkinter模块
MainForm = tkinter.Tk()         #建立窗体实例
MainForm.geometry("250x150")       #设置窗体物理大小（长*高）
MainForm.title("感情分析")          #标题属性
#设置窗体图标属性 eg：MainForm.iconbitmap('D://...')
MainForm['background'] = 'LightSlateGray'   #设置背景颜色 亮石板灰颜色
btn1 = tkinter.Button(MainForm,text="开始",fg="black")  #在窗体上创建btn1按钮  fg=foreground 字体颜色，背景颜色为bg

def turn_property(event):
    event.widget["activeforeground"] = "red"  #鼠标左键按下的时候，标题显示为红色
    event.widget["text"] = "ok"   #鼠标指针接触按钮时，标题变为ok

btn1.bind("<Enter>",turn_property)   #bind绑定鼠标进入事件  <Enter代表鼠标指针接触对应的组件对象时
btn1.pack(side="left")    #pack（）方法将btn1按钮放到窗体上 btn.pack()
MainForm.mainloop()  #启动窗体运行，并等待接收各种事件信息