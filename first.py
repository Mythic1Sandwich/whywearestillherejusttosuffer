from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtGui import QIcon

import sys


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi()
    def setupUi(self):
        self.setWindowTitle("DEAD INSIDE")
        self.move(300, 300) # положение окна
        self.resize(800, 600) # размер окна
        self.lbl = QLabel('Добро пожаловать в программу по определению состояния здоровья!', self)
        self.lbl.move(300, 30)
        self.font = QFont()
        self.font.setFamily("Papyrus")
        self.font.setPointSize(17)
        self.font.setUnderline(True)
        self.lbl.setFont(self.font)
        self.setWindowIcon(QIcon('frog.png'))

        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())