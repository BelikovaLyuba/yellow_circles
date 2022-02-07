import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
from random import randrange


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI.ui", self)
        self.c = False
        self.pb.clicked.connect(self.a)

    def a(self):
        self.c = True
        self.repaint()

    def paintEvent(self, event):
        if self.c:
            qp = QPainter()
            qp.begin(self)
            b = randrange(1, 200)
            qp.setPen(QColor(255, 255, 0))
            qp.drawArc(100, 100, b, b, 10000, 10000)
            qp.end()
            self.c = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    sys.excepthook = except_hook
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())