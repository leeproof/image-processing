from PyQt5.QtWidgets import *
import sys
import winsound

class BeepSound(QMainWindow): # BeepSound 클래스 선언
    def __init__(self): #생성자 함수: __init__
        super().__init__()
        self.setWindowTitle('삑 소리 내기') #윈도우 이름과 위치 지정정
        self.setGeometry(200,200,500,100)

        shortBeepButton=QPushButton('짧게 삑',self) #버튼 생성
        longBeepButton=QPushButton('길게 삑',self)
        quitButton=QPushButton('나가기',self)
        self.label=QLabel('환영합니다',self)

        shortBeepButton.setGeometry(10,10,100,30) #버튼 위치와 크기 지정
        longBeepButton.setGeometry(110,10,100,30)
        quitButton.setGeometry(210,10,100,30)
        self.label.setGeometry(10,40,500,70)

        shortBeepButton.clicked.connect(self.shortBeepFunction)
        longBeepButton.clicked.connect(self.longBeepFunction)
        quitButton.clicked.connect(self.quitFunction)

    def shortBeepFunction(self):
        self.label.setText('주파수 1000으로 0.5초 동안 삑 소리를 냅니다.')
        QApplication.processEvents()
        winsound.Beep(1000,500)

    def longBeepFunction(self):
        self.label.setText('주파스 100으로 3초 동안 삑 소리를 냅니다.')
        QApplication.processEvents()
        winsound.Beep(1000,3000)

    def quitFunction(self):
        self.close()

app=QApplication(sys.argv)
win=BeepSound() #beepsound 클래스의 객체 생성
win.show()
app.exec_()