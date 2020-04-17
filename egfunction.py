# -*- coding: utf-8 -*-
# @Author: BlueSand
# @Email: slxxfl000@163.com
# @Web: www.lzmath.cn
# @Blog: https://blog.csdn.net/weixin_41810846
# @Date:   2019-08-20 17:20:12
# @Last Modified by:   BlueSand
# @Last Modified time: 2019-08-20 17:41:29
import sys
from PyQt5 import QtWidgets
from PyQt5 import QtGui
# 定义一个按钮点击处理函数，这个函数可以与按钮btn绑定，处理按钮的按下事件，
# 当然，这种绑定不是唯一的，不同的按钮，甚至不同的其他的控件都可以使用这个函数
# 这是PyQt5 的信号与槽的机制。 这里先不讨论自定义的信号
# 我们可以这样理解，就是一个控件触发了一种操作，这个操作就会发送一个信号，如果有函数与这个号信号绑定，那么就会在
# 信号收到后调用相应的函数
# 绑定的方法 就是控件.事件.connect(处理函数名) ，不要带参数，不要带括号。新手注意了
def btn_clicked():
    btn.setText('我被点了')
app = QtWidgets.QApplication([])  # 申明主程序。
'''
说明一下，这个sys.argv参数是是一个来自命令行的参数列表。
Python脚本可以在shell中运行。这是我们用来控制我们应用启动的一种方法。
这个东西，暂时没用，可以先用着先：sys.argv
'''
# 主窗体的设置
main_window = QtWidgets.QWidget()  # 申明主窗体
main_window.resize(600, 480)  # 定义窗体大小
main_window.setWindowTitle('我的第一个PyQt5程序')  # 设置窗体的标题
icon = QtGui.QIcon('ICO.png')  # 获取ICO图片
main_window.setWindowIcon(icon)  # 传入ICO图片 作为程序主窗体的图标
# 以下是加入新的控件
btn = QtWidgets.QPushButton('这是一个按钮', main_window)
# 以上是申明一个按钮，第一个参数是按钮上显示的文字，
# 第二个参数是父窗体，这里父窗体是主窗体
btn.move(100, 200)  # 设置按钮的在窗体中的位置， 前面的是x，后面的是y
btn.resize(150, 50)  # 设置按钮的大小， 前面的是宽，后面的是高
btn.setToolTip('这是一个按钮')  # 设置当鼠标移动到按钮上的提示（这个不是必须的）不过，考虑到程序的易用性，可以加一下，
btn.setStyleSheet("background-color: rgb(255, 0, 0);")
# 以上代码是设置按钮的样式。这里设置了背景色：红色
btn.clicked.connect(btn_clicked)   # 这里绑定了按钮的按下去事件,clicked:按下，connect函数用来绑定相应的方法：
# 同样的方法可以增加一些其他的控件
main_window.show()  # 显示窗体
app.exec()  # 退出程序 也可以写成sys.exit(app.exec())
