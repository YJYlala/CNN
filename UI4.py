import sys
import  untitled
from PyQt5.QtWidgets import QApplication,QMainWindow
if __name__=='__main__':
    app=QApplication(sys.argv)    #创建应用程序实例
    MainWindow=QMainWindow()    #先生成一个窗体
    ui=untitled.Ui_Dialog()    #创建类对象
    ui.setupUi(MainWindow)      #调用函数
    MainWindow.show()        #展示
    sys.exit(app.exec())     #离开