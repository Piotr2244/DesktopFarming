from PyQt6.QtWidgets import QApplication, QWidget
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Desktop Farming")
        self.setFixedHeight(620)
        self.setFixedWidth(620)
        self.setStyleSheet("background-color: #c5e1a5;")




app = QApplication([])
window = Window()
window.show()
sys.exit(app.exec())
