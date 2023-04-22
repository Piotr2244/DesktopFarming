from PyQt6.QtCore import QTimer
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtWidgets import QPushButton, QApplication


class Plant_Class:
    def __init__(self, time: float = 0, place: QPushButton = None, picture: QPixmap = None, index: int = 0,
                 growPicture: QPixmap = None):
        if time and place and picture and growPicture:
            self.time = time
            self.place = place
            self.picture = picture
            self.index = index
            self.growPicture = growPicture
            self.place.setIcon(QIcon(self.growPicture))
            self.ready = False
            self.icon_changed = 0
            self.timer = QTimer()
            self.timer.timeout.connect(self.plant_ready)
            QApplication.processEvents()
            self.timer.start(time)
        else:
            self.time = None
            self.place = None
            self.picture = None
            self.index = None
            self.growPicture = None
            self.ready = None
            self.icon_changed = None
            self.timer = None

    def plant_ready(self):
        self.ready = True
        self.icon_changed += 1
        if self.icon_changed == 1:
            self.icon_changed += 1
            self.place.setIcon(QIcon(self.picture))
