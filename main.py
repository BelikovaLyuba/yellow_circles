import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton
from PyQt5.QtGui import QPainter, QColor
from random import randint


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(400, 400, 400, 400)

        self.c = False

        self.pb = QPushButton(self)
        self.pb.setText('Показать')
        self.pb.move(10, 10)
        self.pb.clicked.connect(self.a)

    def a(self):
        self.c = True
        self.repaint()

    def paintEvent(self, event):
        if self.c:
            qp = QPainter()
            qp.begin(self)
            d = randint(0, 200)
            r, g, b = randint(0, 255), randint(0, 255), randint(0, 255)
            qp.setPen(QColor(r, g, b))
            qp.drawArc(100, 100, d, d, 10000, 10000)
            qp.end()
            self.c = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())