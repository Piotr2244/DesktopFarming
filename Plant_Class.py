from PyQt6.QtCore import QTimer
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtWidgets import QPushButton, QApplication


# class represents a single growing crop, stores info about plant index, growth time, button representing planting
# spot, plant picture, and more information. After time, plant grows and can be ready to harvest
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
            self.icon_changed = False
            self.timer = QTimer()
            self.timer.timeout.connect(self.plant_ready)
            QApplication.processEvents()
            self.timer.start(time)
        else:  # no-argument constructor
            self.time = None
            self.place = None
            self.picture = None
            self.index = None
            self.growPicture = None
            self.ready = None
            self.icon_changed = None
            self.timer = None

    # method happens after growth time pass, determines that plant is ready to pick
    def plant_ready(self):
        self.ready = True
        if not self.icon_changed:
            self.icon_changed = True
            self.place.setIcon(QIcon(self.picture))
