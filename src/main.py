from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6 import QtWidgets
from FokusMain import Ui_Main_Window
import sys


class MainWindow(QMainWindow, Ui_Main_Window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Main_Window = MainWindow()
    Main_Window.show()
    sys.exit(app.exec())

