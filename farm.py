from PyQt6.QtCore import QTimer
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QPixmap, QIcon
import random
from Plant_Class import Plant_Class


class Ui_Form(object):

    def __init__(self):

        self.inventory = [0, 0, 0, 0, 0, 0, 0, 0]  # each index represents current amount of distinct plant
        self.buy_prices = [2, 5, 10, 25, 50, 100, 250, 800]  # current prices for each plant
        self.sell_prices = [1, 3, 5, 12, 25, 50, 125, 400]  # current sell prices for each plant
        self.grow_time = [5000, 10000, 20000, 30000, 50000, 60000, 90000,
                          120000]  # growth time for each plant in milliseconds

        self.planting_List = []  # Contains 25 buttons representing planting fields. Player can grow plants on them
        self.display_List = []  # Contains 8 display panels representing current inventory status
        self.sell_price_display_list = []  # Contains 8 display panels representing current sell prices for every plant
        self.buy_price_display_list = []  # Contains 8 display panels representing current prices for every plant
        self.pictures = []  # Contains plant pictures imported from assets folder
        self.chosen_plant_list = []  # Contains 8 buttons, clicking on them changes current chosen plant

        self.current_Money = 100  # Player current money
        self.chosen_plant = 0  # currently chosen plant index to placed on an empty field
        self.already_planted = [False for i in
                                range(25)]  # 25 bool values for planting field. If true, field is unoccupied
        self.plant_class_list = [Plant_Class() for _ in range(25)]  # 25 Plant_Class objects, one for every field

        self.timer = QTimer()
        self.timer.timeout.connect(self.rerollValues)  # that makes all prices change every 10 seconds
        self.timer.start(10000)  # 10 seconds

        self.setupUi(Form)  # sets up the whole GUI
        self.begin_procedure()  # initialise fields values

    # method mostly created by PyQt6 UI code generator, initialises all gui elements and connects buttons with a
    # proper game methods
    def setupUi(self, Form):

        Form.setObjectName("Form")
        Form.resize(692, 390)
        Form.setStyleSheet("QWidget {\n"
                           "background-color:\"#aaff7f\"\n"
                           "\n"
                           "}\n"
                           "\n"
                           "")
        self.slot1 = QtWidgets.QPushButton(parent=Form)
        self.slot1.setGeometry(QtCore.QRect(20, 20, 51, 51))
        self.slot1.setStyleSheet("QPushButton {\n"
                                 "background-color: #de6f00;\n"
                                 "}")
        self.slot1.setText("")
        self.slot1.setObjectName("slot1")
        self.slot1.clicked.connect(lambda: self.place_plant(0))
        self.slot1.setIconSize(QtCore.QSize(64, 64))
        self.slot2 = QtWidgets.QPushButton(parent=Form)
        self.slot2.setGeometry(QtCore.QRect(90, 20, 51, 51))
        self.slot2.setStyleSheet("QPushButton {\n"
                                 "background-color: #de6f00;\n"
                                 "}")
        self.slot2.setText("")
        self.slot2.setObjectName("slot2")
        self.slot2.setIconSize(QtCore.QSize(64, 64))
        self.slot2.clicked.connect(lambda: self.place_plant(1))
        self.slot3 = QtWidgets.QPushButton(parent=Form)
        self.slot3.setGeometry(QtCore.QRect(160, 20, 51, 51))
        self.slot3.setStyleSheet("QPushButton {\n"
                                 "background-color: #de6f00;\n"
                                 "}")
        self.slot3.setText("")
        self.slot3.setObjectName("slot3")
        self.slot3.setIconSize(QtCore.QSize(64, 64))
        self.slot3.clicked.connect(lambda: self.place_plant(2))
        self.slot4 = QtWidgets.QPushButton(parent=Form)
        self.slot4.setGeometry(QtCore.QRect(230, 20, 51, 51))
        self.slot4.setStyleSheet("QPushButton {\n"
                                 "background-color: #de6f00;\n"
                                 "}")
        self.slot4.setText("")
        self.slot4.setObjectName("slot4")
        self.slot4.setIconSize(QtCore.QSize(64, 64))
        self.slot4.clicked.connect(lambda: self.place_plant(3))
        self.slot5 = QtWidgets.QPushButton(parent=Form)
        self.slot5.setGeometry(QtCore.QRect(300, 20, 51, 51))
        self.slot5.setStyleSheet("QPushButton {\n"
                                 "background-color: #de6f00;\n"
                                 "}")
        self.slot5.setText("")
        self.slot5.setObjectName("slot5")
        self.slot5.setIconSize(QtCore.QSize(64, 64))
        self.slot5.clicked.connect(lambda: self.place_plant(4))
        self.slot10 = QtWidgets.QPushButton(parent=Form)
        self.slot10.setGeometry(QtCore.QRect(300, 90, 51, 51))
        self.slot10.setStyleSheet("QPushButton {\n"
                                  "background-color: #de6f00;\n"
                                  "}")
        self.slot10.setText("")
        self.slot10.setObjectName("slot10")
        self.slot10.setIconSize(QtCore.QSize(64, 64))
        self.slot10.clicked.connect(lambda: self.place_plant(9))
        self.slot7 = QtWidgets.QPushButton(parent=Form)
        self.slot7.setGeometry(QtCore.QRect(90, 90, 51, 51))
        self.slot7.setStyleSheet("QPushButton {\n"
                                 "background-color: #de6f00;\n"
                                 "}")
        self.slot7.setText("")
        self.slot7.setObjectName("slot7")
        self.slot7.setIconSize(QtCore.QSize(64, 64))
        self.slot7.clicked.connect(lambda: self.place_plant(6))
        self.slot9 = QtWidgets.QPushButton(parent=Form)
        self.slot9.setGeometry(QtCore.QRect(230, 90, 51, 51))
        self.slot9.setStyleSheet("QPushButton {\n"
                                 "background-color: #de6f00;\n"
                                 "}")
        self.slot9.setText("")
        self.slot9.setObjectName("slot9")
        self.slot9.setIconSize(QtCore.QSize(64, 64))
        self.slot9.clicked.connect(lambda: self.place_plant(8))
        self.slot6 = QtWidgets.QPushButton(parent=Form)
        self.slot6.setGeometry(QtCore.QRect(20, 90, 51, 51))
        self.slot6.setStyleSheet("QPushButton {\n"
                                 "background-color: #de6f00;\n"
                                 "}")
        self.slot6.setText("")
        self.slot6.setObjectName("slot6")
        self.slot6.setIconSize(QtCore.QSize(64, 64))
        self.slot6.clicked.connect(lambda: self.place_plant(5))
        self.slot8 = QtWidgets.QPushButton(parent=Form)
        self.slot8.setGeometry(QtCore.QRect(160, 90, 51, 51))
        self.slot8.setStyleSheet("QPushButton {\n"
                                 "background-color: #de6f00;\n"
                                 "}")
        self.slot8.setText("")
        self.slot8.setObjectName("slot8")
        self.slot8.setIconSize(QtCore.QSize(64, 64))
        self.slot8.clicked.connect(lambda: self.place_plant(7))
        self.slot15 = QtWidgets.QPushButton(parent=Form)
        self.slot15.setGeometry(QtCore.QRect(300, 160, 51, 51))
        self.slot15.setStyleSheet("QPushButton {\n"
                                  "background-color: #de6f00;\n"
                                  "}")
        self.slot15.setText("")
        self.slot15.setObjectName("slot15")
        self.slot15.setIconSize(QtCore.QSize(64, 64))
        self.slot15.clicked.connect(lambda: self.place_plant(14))
        self.slot12 = QtWidgets.QPushButton(parent=Form)
        self.slot12.setGeometry(QtCore.QRect(90, 160, 51, 51))
        self.slot12.setStyleSheet("QPushButton {\n"
                                  "background-color: #de6f00;\n"
                                  "}")
        self.slot12.setText("")
        self.slot12.setObjectName("slot12")
        self.slot12.setIconSize(QtCore.QSize(64, 64))
        self.slot12.clicked.connect(lambda: self.place_plant(11))
        self.slot14 = QtWidgets.QPushButton(parent=Form)
        self.slot14.setGeometry(QtCore.QRect(230, 160, 51, 51))
        self.slot14.setStyleSheet("QPushButton {\n"
                                  "background-color: #de6f00;\n"
                                  "}")
        self.slot14.setText("")
        self.slot14.setObjectName("slot14")
        self.slot14.setIconSize(QtCore.QSize(64, 64))
        self.slot14.clicked.connect(lambda: self.place_plant(13))
        self.slot11 = QtWidgets.QPushButton(parent=Form)
        self.slot11.setGeometry(QtCore.QRect(20, 160, 51, 51))
        self.slot11.setStyleSheet("QPushButton {\n"
                                  "background-color: #de6f00;\n"
                                  "}")
        self.slot11.setText("")
        self.slot11.setObjectName("slot11")
        self.slot11.setIconSize(QtCore.QSize(64, 64))
        self.slot11.clicked.connect(lambda: self.place_plant(10))
        self.slot13 = QtWidgets.QPushButton(parent=Form)
        self.slot13.setGeometry(QtCore.QRect(160, 160, 51, 51))
        self.slot13.setStyleSheet("QPushButton {\n"
                                  "background-color: #de6f00;\n"
                                  "}")
        self.slot13.setText("")
        self.slot13.setObjectName("slot13")
        self.slot13.setIconSize(QtCore.QSize(64, 64))
        self.slot13.clicked.connect(lambda: self.place_plant(12))
        self.slot20 = QtWidgets.QPushButton(parent=Form)
        self.slot20.setGeometry(QtCore.QRect(300, 230, 51, 51))
        self.slot20.setStyleSheet("QPushButton {\n"
                                  "background-color: #de6f00;\n"
                                  "}")
        self.slot20.setText("")
        self.slot20.setObjectName("slot20")
        self.slot20.setIconSize(QtCore.QSize(64, 64))
        self.slot20.clicked.connect(lambda: self.place_plant(19))
        self.slot17 = QtWidgets.QPushButton(parent=Form)
        self.slot17.setGeometry(QtCore.QRect(90, 230, 51, 51))
        self.slot17.setStyleSheet("QPushButton {\n"
                                  "background-color: #de6f00;\n"
                                  "}")
        self.slot17.setText("")
        self.slot17.setObjectName("slot17")
        self.slot17.setIconSize(QtCore.QSize(64, 64))
        self.slot17.clicked.connect(lambda: self.place_plant(16))
        self.slot19 = QtWidgets.QPushButton(parent=Form)
        self.slot19.setGeometry(QtCore.QRect(230, 230, 51, 51))
        self.slot19.setStyleSheet("QPushButton {\n"
                                  "background-color: #de6f00;\n"
                                  "}")
        self.slot19.setText("")
        self.slot19.setObjectName("slot19")
        self.slot19.setIconSize(QtCore.QSize(64, 64))
        self.slot19.clicked.connect(lambda: self.place_plant(18))
        self.slot16 = QtWidgets.QPushButton(parent=Form)
        self.slot16.setGeometry(QtCore.QRect(20, 230, 51, 51))
        self.slot16.setStyleSheet("QPushButton {\n"
                                  "background-color: #de6f00;\n"
                                  "}")
        self.slot16.setText("")
        self.slot16.setObjectName("slot16")
        self.slot16.setIconSize(QtCore.QSize(64, 64))
        self.slot16.clicked.connect(lambda: self.place_plant(15))
        self.slot18 = QtWidgets.QPushButton(parent=Form)
        self.slot18.setGeometry(QtCore.QRect(160, 230, 51, 51))
        self.slot18.setStyleSheet("QPushButton {\n"
                                  "background-color: #de6f00;\n"
                                  "}")
        self.slot18.setText("")
        self.slot18.setObjectName("slot18")
        self.slot18.setIconSize(QtCore.QSize(64, 64))
        self.slot18.clicked.connect(lambda: self.place_plant(17))
        self.slot25 = QtWidgets.QPushButton(parent=Form)
        self.slot25.setGeometry(QtCore.QRect(300, 300, 51, 51))
        self.slot25.setStyleSheet("QPushButton {\n"
                                  "background-color: #de6f00;\n"
                                  "}")
        self.slot25.setText("")
        self.slot25.setObjectName("slot25")
        self.slot25.setIconSize(QtCore.QSize(64, 64))
        self.slot25.clicked.connect(lambda: self.place_plant(24))
        self.slot22 = QtWidgets.QPushButton(parent=Form)
        self.slot22.setGeometry(QtCore.QRect(90, 300, 51, 51))
        self.slot22.setStyleSheet("QPushButton {\n"
                                  "background-color: #de6f00;\n"
                                  "}")
        self.slot22.setText("")
        self.slot22.setObjectName("slot22")
        self.slot22.setIconSize(QtCore.QSize(64, 64))
        self.slot22.clicked.connect(lambda: self.place_plant(21))
        self.slot24 = QtWidgets.QPushButton(parent=Form)
        self.slot24.setGeometry(QtCore.QRect(230, 300, 51, 51))
        self.slot24.setStyleSheet("QPushButton {\n"
                                  "background-color: #de6f00;\n"
                                  "}")
        self.slot24.setText("")
        self.slot24.setObjectName("slot24")
        self.slot24.setIconSize(QtCore.QSize(64, 64))
        self.slot24.clicked.connect(lambda: self.place_plant(23))
        self.slot21 = QtWidgets.QPushButton(parent=Form)
        self.slot21.setGeometry(QtCore.QRect(20, 300, 51, 51))
        self.slot21.setStyleSheet("QPushButton {\n"
                                  "background-color: #de6f00;\n"
                                  "}")
        self.slot21.setText("")
        self.slot21.setObjectName("slot21")
        self.slot21.setIconSize(QtCore.QSize(64, 64))
        self.slot21.clicked.connect(lambda: self.place_plant(20))
        self.slot23 = QtWidgets.QPushButton(parent=Form)
        self.slot23.setGeometry(QtCore.QRect(160, 300, 51, 51))
        self.slot23.setStyleSheet("QPushButton {\n"
                                  "background-color: #de6f00;\n"
                                  "}")
        self.slot23.setText("")
        self.slot23.setObjectName("slot23")
        self.slot23.setIconSize(QtCore.QSize(64, 64))
        self.slot23.clicked.connect(lambda: self.place_plant(22))
        self.plant1 = QtWidgets.QPushButton(parent=Form)
        self.plant1.setGeometry(QtCore.QRect(370, 70, 31, 31))
        self.plant1.setAutoFillBackground(False)
        self.plant1.setStyleSheet("QPushButton {\n"
                                  "background-color: #79b359;\n"
                                  "}")
        self.plant1.setText("")
        self.plant1.setIconSize(QtCore.QSize(32, 32))
        self.plant1.setObjectName("plant1")
        self.plant1.clicked.connect(lambda: self.chosen_plant_change(0))
        self.plant2 = QtWidgets.QPushButton(parent=Form)
        self.plant2.setGeometry(QtCore.QRect(370, 110, 31, 31))
        self.plant2.setStyleSheet("QPushButton {\n"
                                  "background-color: #79b359;\n"
                                  "}")
        self.plant2.setText("")
        icon = QtGui.QIcon()
        self.plant2.setIcon(icon)
        self.plant2.setIconSize(QtCore.QSize(32, 32))
        self.plant2.setObjectName("plant2")
        self.plant2.clicked.connect(lambda: self.chosen_plant_change(1))
        self.plant4 = QtWidgets.QPushButton(parent=Form)
        self.plant4.setGeometry(QtCore.QRect(370, 190, 31, 31))
        self.plant4.setStyleSheet("QPushButton {\n"
                                  "background-color: #79b359;\n"
                                  "}")
        self.plant4.setText("")
        icon1 = QtGui.QIcon()
        self.plant4.setIcon(icon1)
        self.plant4.setIconSize(QtCore.QSize(32, 32))
        self.plant4.setObjectName("plant4")
        self.plant4.clicked.connect(lambda: self.chosen_plant_change(3))
        self.plant3 = QtWidgets.QPushButton(parent=Form)
        self.plant3.setGeometry(QtCore.QRect(370, 150, 31, 31))
        self.plant3.setStyleSheet("QPushButton {\n"
                                  "background-color: #79b359;\n"
                                  "}")
        self.plant3.setText("")
        self.plant3.setIconSize(QtCore.QSize(32, 32))
        self.plant3.setObjectName("plant3")
        self.plant3.clicked.connect(lambda: self.chosen_plant_change(2))
        self.plant6 = QtWidgets.QPushButton(parent=Form)
        self.plant6.setGeometry(QtCore.QRect(370, 270, 31, 31))
        self.plant6.setStyleSheet("QPushButton {\n"
                                  "background-color: #79b359;\n"
                                  "}")
        self.plant6.setText("")
        icon2 = QtGui.QIcon()
        self.plant6.setIcon(icon2)
        self.plant6.setIconSize(QtCore.QSize(32, 32))
        self.plant6.setObjectName("plant6")
        self.plant6.clicked.connect(lambda: self.chosen_plant_change(5))
        self.plant8 = QtWidgets.QPushButton(parent=Form)
        self.plant8.setGeometry(QtCore.QRect(370, 350, 31, 31))
        self.plant8.setStyleSheet("QPushButton {\n"
                                  "background-color: #79b359;\n"
                                  "}")
        self.plant8.setText("")
        icon3 = QtGui.QIcon()
        self.plant8.setIcon(icon3)
        self.plant8.setIconSize(QtCore.QSize(32, 32))
        self.plant8.setObjectName("plant8")
        self.plant8.clicked.connect(lambda: self.chosen_plant_change(7))
        self.plant7 = QtWidgets.QPushButton(parent=Form)
        self.plant7.setGeometry(QtCore.QRect(370, 310, 31, 31))
        self.plant7.setStyleSheet("QPushButton {\n"
                                  "background-color: #79b359;\n"
                                  "}")
        self.plant7.setText("")
        icon4 = QtGui.QIcon()
        self.plant7.setIcon(icon4)
        self.plant7.setIconSize(QtCore.QSize(32, 32))
        self.plant7.setObjectName("plant7")
        self.plant7.clicked.connect(lambda: self.chosen_plant_change(6))
        self.plant5 = QtWidgets.QPushButton(parent=Form)
        self.plant5.setGeometry(QtCore.QRect(370, 230, 31, 31))
        self.plant5.setStyleSheet("QPushButton {\n"
                                  "background-color: #79b359;\n"
                                  "}")
        self.plant5.setText("")
        icon5 = QtGui.QIcon()
        self.plant5.setIcon(icon5)
        self.plant5.setIconSize(QtCore.QSize(32, 32))
        self.plant5.setObjectName("plant5")
        self.plant5.clicked.connect(lambda: self.chosen_plant_change(4))
        self.amount1 = QtWidgets.QLCDNumber(parent=Form)
        self.amount1.setGeometry(QtCore.QRect(410, 70, 51, 31))
        self.amount1.setStyleSheet("background-color: rgb(0, 99, 0);\n"
                                   "border-color: rgb(0, 42, 0);")
        self.amount1.setObjectName("amount1")
        self.amount2 = QtWidgets.QLCDNumber(parent=Form)
        self.amount2.setGeometry(QtCore.QRect(410, 110, 51, 31))
        self.amount2.setStyleSheet("background-color: rgb(0, 99, 0);\n"
                                   "border-color: rgb(0, 42, 0);")
        self.amount2.setObjectName("amount2")
        self.amount3 = QtWidgets.QLCDNumber(parent=Form)
        self.amount3.setGeometry(QtCore.QRect(410, 150, 51, 31))
        self.amount3.setStyleSheet("background-color: rgb(0, 99, 0);\n"
                                   "border-color: rgb(0, 42, 0);")
        self.amount3.setObjectName("amount3")
        self.amount4 = QtWidgets.QLCDNumber(parent=Form)
        self.amount4.setGeometry(QtCore.QRect(410, 190, 51, 31))
        self.amount4.setStyleSheet("background-color: rgb(0, 99, 0);\n"
                                   "border-color: rgb(0, 42, 0);")
        self.amount4.setObjectName("amount4")
        self.amount5 = QtWidgets.QLCDNumber(parent=Form)
        self.amount5.setGeometry(QtCore.QRect(410, 230, 51, 31))
        self.amount5.setStyleSheet("background-color: rgb(0, 99, 0);\n"
                                   "border-color: rgb(0, 42, 0);")
        self.amount5.setObjectName("amount5")
        self.amount6 = QtWidgets.QLCDNumber(parent=Form)
        self.amount6.setGeometry(QtCore.QRect(410, 270, 51, 31))
        self.amount6.setStyleSheet("background-color: rgb(0, 99, 0);\n"
                                   "border-color: rgb(0, 42, 0);")
        self.amount6.setObjectName("amount6")
        self.amount7 = QtWidgets.QLCDNumber(parent=Form)
        self.amount7.setGeometry(QtCore.QRect(410, 310, 51, 31))
        self.amount7.setStyleSheet("background-color: rgb(0, 99, 0);\n"
                                   "border-color: rgb(0, 42, 0);")
        self.amount7.setObjectName("amount7")
        self.amount8 = QtWidgets.QLCDNumber(parent=Form)
        self.amount8.setGeometry(QtCore.QRect(410, 350, 51, 31))
        self.amount8.setStyleSheet("background-color: rgb(0, 99, 0);\n"
                                   "border-color: rgb(0, 42, 0);")
        self.amount8.setObjectName("amount8")
        self.pb8 = QtWidgets.QLCDNumber(parent=Form)
        self.pb8.setGeometry(QtCore.QRect(470, 350, 51, 31))
        self.pb8.setStyleSheet("background-color: rgb(0, 99, 0);\n"
                               "border-color: rgb(0, 42, 0);")
        self.pb8.setObjectName("pb8")
        self.pb5 = QtWidgets.QLCDNumber(parent=Form)
        self.pb5.setGeometry(QtCore.QRect(470, 230, 51, 31))
        self.pb5.setStyleSheet("background-color: rgb(0, 99, 0);\n"
                               "border-color: rgb(0, 42, 0);")
        self.pb5.setObjectName("pb5")
        self.pb7 = QtWidgets.QLCDNumber(parent=Form)
        self.pb7.setGeometry(QtCore.QRect(470, 310, 51, 31))
        self.pb7.setStyleSheet("background-color: rgb(0, 99, 0);\n"
                               "border-color: rgb(0, 42, 0);")
        self.pb7.setObjectName("pb7")
        self.pb3 = QtWidgets.QLCDNumber(parent=Form)
        self.pb3.setGeometry(QtCore.QRect(470, 150, 51, 31))
        self.pb3.setStyleSheet("background-color: rgb(0, 99, 0);\n"
                               "border-color: rgb(0, 42, 0);")
        self.pb3.setObjectName("pb3")
        self.pb1 = QtWidgets.QLCDNumber(parent=Form)
        self.pb1.setGeometry(QtCore.QRect(470, 70, 51, 31))
        self.pb1.setStyleSheet("background-color: rgb(0, 99, 0);\n"
                               "border-color: rgb(0, 42, 0);")
        self.pb1.setObjectName("pb1")
        self.pb4 = QtWidgets.QLCDNumber(parent=Form)
        self.pb4.setGeometry(QtCore.QRect(470, 190, 51, 31))
        self.pb4.setStyleSheet("background-color: rgb(0, 99, 0);\n"
                               "border-color: rgb(0, 42, 0);")
        self.pb4.setObjectName("pb4")
        self.pb6 = QtWidgets.QLCDNumber(parent=Form)
        self.pb6.setGeometry(QtCore.QRect(470, 270, 51, 31))
        self.pb6.setStyleSheet("background-color: rgb(0, 99, 0);\n"
                               "border-color: rgb(0, 42, 0);")
        self.pb6.setObjectName("pb6")
        self.pb2 = QtWidgets.QLCDNumber(parent=Form)
        self.pb2.setGeometry(QtCore.QRect(470, 110, 51, 31))
        self.pb2.setStyleSheet("background-color: rgb(0, 99, 0);\n"
                               "border-color: rgb(0, 42, 0);")
        self.pb2.setObjectName("pb2")
        self.ps8 = QtWidgets.QLCDNumber(parent=Form)
        self.ps8.setGeometry(QtCore.QRect(530, 350, 51, 31))
        self.ps8.setStyleSheet("background-color: rgb(0, 99, 0);\n"
                               "border-color: rgb(0, 42, 0);")
        self.ps8.setObjectName("ps8")
        self.ps5 = QtWidgets.QLCDNumber(parent=Form)
        self.ps5.setGeometry(QtCore.QRect(530, 230, 51, 31))
        self.ps5.setStyleSheet("background-color: rgb(0, 99, 0);\n"
                               "border-color: rgb(0, 42, 0);")
        self.ps5.setObjectName("ps5")
        self.ps7 = QtWidgets.QLCDNumber(parent=Form)
        self.ps7.setGeometry(QtCore.QRect(530, 310, 51, 31))
        self.ps7.setStyleSheet("background-color: rgb(0, 99, 0);\n"
                               "border-color: rgb(0, 42, 0);")
        self.ps7.setObjectName("ps7")
        self.ps3 = QtWidgets.QLCDNumber(parent=Form)
        self.ps3.setGeometry(QtCore.QRect(530, 150, 51, 31))
        self.ps3.setStyleSheet("background-color: rgb(0, 99, 0);\n"
                               "border-color: rgb(0, 42, 0);")
        self.ps3.setObjectName("ps3")
        self.ps1 = QtWidgets.QLCDNumber(parent=Form)
        self.ps1.setGeometry(QtCore.QRect(530, 70, 51, 31))
        self.ps1.setStyleSheet("background-color: rgb(0, 99, 0);\n"
                               "border-color: rgb(0, 42, 0);")
        self.ps1.setObjectName("ps1")
        self.ps4 = QtWidgets.QLCDNumber(parent=Form)
        self.ps4.setGeometry(QtCore.QRect(530, 190, 51, 31))
        self.ps4.setStyleSheet("background-color: rgb(0, 99, 0);\n"
                               "border-color: rgb(0, 42, 0);")
        self.ps4.setObjectName("ps4")
        self.ps6 = QtWidgets.QLCDNumber(parent=Form)
        self.ps6.setGeometry(QtCore.QRect(530, 270, 51, 31))
        self.ps6.setStyleSheet("background-color: rgb(0, 99, 0);\n"
                               "border-color: rgb(0, 42, 0);")
        self.ps6.setObjectName("ps6")
        self.ps2 = QtWidgets.QLCDNumber(parent=Form)
        self.ps2.setGeometry(QtCore.QRect(530, 110, 51, 31))
        self.ps2.setStyleSheet("background-color: rgb(0, 99, 0);\n"
                               "border-color: rgb(0, 42, 0);")
        self.ps2.setObjectName("ps2")
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setGeometry(QtCore.QRect(410, 50, 47, 14))
        self.label.setObjectName("label")
        self.buy1 = QtWidgets.QPushButton(parent=Form)
        self.buy1.setGeometry(QtCore.QRect(590, 70, 31, 31))
        self.buy1.setAutoFillBackground(False)
        self.buy1.setStyleSheet("QPushButton {\n"
                                "background-color: #48d900;\n"
                                "}")
        self.buy1.setObjectName("buy1")
        self.buy1.clicked.connect(lambda: self.item_bought(0))
        self.buy2 = QtWidgets.QPushButton(parent=Form)
        self.buy2.setGeometry(QtCore.QRect(590, 110, 31, 31))
        self.buy2.setAutoFillBackground(False)
        self.buy2.setStyleSheet("QPushButton {\n"
                                "background-color: #48d900;\n"
                                "}")
        self.buy2.setObjectName("buy2")
        self.buy2.clicked.connect(lambda: self.item_bought(1))
        self.buy3 = QtWidgets.QPushButton(parent=Form)
        self.buy3.setGeometry(QtCore.QRect(590, 150, 31, 31))
        self.buy3.setAutoFillBackground(False)
        self.buy3.setStyleSheet("QPushButton {\n"
                                "background-color: #48d900;\n"
                                "}")
        self.buy3.setObjectName("buy3")
        self.buy3.clicked.connect(lambda: self.item_bought(2))
        self.buy4 = QtWidgets.QPushButton(parent=Form)
        self.buy4.setGeometry(QtCore.QRect(590, 190, 31, 31))
        self.buy4.setAutoFillBackground(False)
        self.buy4.setStyleSheet("QPushButton {\n"
                                "background-color: #48d900;\n"
                                "}")
        self.buy4.setObjectName("buy4")
        self.buy4.clicked.connect(lambda: self.item_bought(3))
        self.buy8 = QtWidgets.QPushButton(parent=Form)
        self.buy8.setGeometry(QtCore.QRect(590, 350, 31, 31))
        self.buy8.setAutoFillBackground(False)
        self.buy8.setStyleSheet("QPushButton {\n"
                                "background-color: #48d900;\n"
                                "}")
        self.buy8.setObjectName("buy8")
        self.buy8.clicked.connect(lambda: self.item_bought(7))
        self.buy7 = QtWidgets.QPushButton(parent=Form)
        self.buy7.setGeometry(QtCore.QRect(590, 310, 31, 31))
        self.buy7.setAutoFillBackground(False)
        self.buy7.setStyleSheet("QPushButton {\n"
                                "background-color: #48d900;\n"
                                "}")
        self.buy7.setObjectName("buy7")
        self.buy7.clicked.connect(lambda: self.item_bought(6))
        self.buy5 = QtWidgets.QPushButton(parent=Form)
        self.buy5.setGeometry(QtCore.QRect(590, 230, 31, 31))
        self.buy5.setAutoFillBackground(False)
        self.buy5.setStyleSheet("QPushButton {\n"
                                "background-color: #48d900;\n"
                                "}")
        self.buy5.setObjectName("buy5")
        self.buy5.clicked.connect(lambda: self.item_bought(4))
        self.buy6 = QtWidgets.QPushButton(parent=Form)
        self.buy6.setGeometry(QtCore.QRect(590, 270, 31, 31))
        self.buy6.setAutoFillBackground(False)
        self.buy6.setStyleSheet("QPushButton {\n"
                                "background-color: #48d900;\n"
                                "}")
        self.buy6.setObjectName("buy6")
        self.buy6.clicked.connect(lambda: self.item_bought(5))
        self.sell3 = QtWidgets.QPushButton(parent=Form)
        self.sell3.setGeometry(QtCore.QRect(630, 150, 31, 31))
        self.sell3.setAutoFillBackground(False)
        self.sell3.setStyleSheet("QPushButton {\n"
                                 "background-color: #48d900;\n"
                                 "}")
        self.sell3.setObjectName("sell3")
        self.sell3.clicked.connect(lambda: self.item_sold(2))
        self.sell4 = QtWidgets.QPushButton(parent=Form)
        self.sell4.setGeometry(QtCore.QRect(630, 190, 31, 31))
        self.sell4.setAutoFillBackground(False)
        self.sell4.setStyleSheet("QPushButton {\n"
                                 "background-color: #48d900;\n"
                                 "}")
        self.sell4.setObjectName("sell4")
        self.sell4.clicked.connect(lambda: self.item_sold(3))
        self.sell5 = QtWidgets.QPushButton(parent=Form)
        self.sell5.setGeometry(QtCore.QRect(630, 230, 31, 31))
        self.sell5.setAutoFillBackground(False)
        self.sell5.setStyleSheet("QPushButton {\n"
                                 "background-color: #48d900;\n"
                                 "}")
        self.sell5.setObjectName("sell5")
        self.sell5.clicked.connect(lambda: self.item_sold(4))
        self.sell6 = QtWidgets.QPushButton(parent=Form)
        self.sell6.setGeometry(QtCore.QRect(630, 270, 31, 31))
        self.sell6.setAutoFillBackground(False)
        self.sell6.setStyleSheet("QPushButton {\n"
                                 "background-color: #48d900;\n"
                                 "}")
        self.sell6.setObjectName("sell6")
        self.sell6.clicked.connect(lambda: self.item_sold(5))
        self.sell1 = QtWidgets.QPushButton(parent=Form)
        self.sell1.setGeometry(QtCore.QRect(630, 70, 31, 31))
        self.sell1.setAutoFillBackground(False)
        self.sell1.setStyleSheet("QPushButton {\n"
                                 "background-color: #48d900;\n"
                                 "}")
        self.sell1.setObjectName("sell1")
        self.sell1.clicked.connect(lambda: self.item_sold(0))
        self.sell7 = QtWidgets.QPushButton(parent=Form)
        self.sell7.setGeometry(QtCore.QRect(630, 310, 31, 31))
        self.sell7.setAutoFillBackground(False)
        self.sell7.setStyleSheet("QPushButton {\n"
                                 "background-color: #48d900;\n"
                                 "}")
        self.sell7.setObjectName("sell7")
        self.sell7.clicked.connect(lambda: self.item_sold(6))
        self.sell2 = QtWidgets.QPushButton(parent=Form)
        self.sell2.setGeometry(QtCore.QRect(630, 110, 31, 31))
        self.sell2.setAutoFillBackground(False)
        self.sell2.setStyleSheet("QPushButton {\n"
                                 "background-color: #48d900;\n"
                                 "}")
        self.sell2.setObjectName("sell2")
        self.sell2.clicked.connect(lambda: self.item_sold(1))
        self.sell8 = QtWidgets.QPushButton(parent=Form)
        self.sell8.setGeometry(QtCore.QRect(630, 350, 31, 31))
        self.sell8.setAutoFillBackground(False)
        self.sell8.setStyleSheet("QPushButton {\n"
                                 "background-color: #48d900;\n"
                                 "}")
        self.sell8.setObjectName("sell8")
        self.sell8.clicked.connect(lambda: self.item_sold(7))
        self.label_2 = QtWidgets.QLabel(parent=Form)
        self.label_2.setGeometry(QtCore.QRect(470, 50, 41, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=Form)
        self.label_3.setGeometry(QtCore.QRect(530, 50, 61, 16))
        self.label_3.setObjectName("label_3")
        self.money = QtWidgets.QLCDNumber(parent=Form)
        self.money.setGeometry(QtCore.QRect(563, 10, 91, 31))
        self.money.setStyleSheet("background-color: rgb(149, 104, 13);")
        self.money.setObjectName("money")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    ########################################################################################################################

    # method filling structures with displays, buttons and pictures, also prints beginning values and icons on buttons
    def begin_procedure(self):

        self.pictures = ['assets/04_Cucumber.png', 'assets/03_Cranberry.png',
                         'assets/22_Strawberry.png', 'assets/23_Watermelon.png',
                         'assets/11_Grapes_Green.png', 'assets/14_Kiwi.png',
                         'assets/15_Lemon.png', 'assets/09_Fig.png'
                         ]

        self.chosen_plant_list = [self.plant1, self.plant2, self.plant3, self.plant4,
                                  self.plant5, self.plant6, self.plant7, self.plant8]

        self.planting_List = [self.slot1, self.slot2, self.slot3, self.slot4, self.slot5,
                              self.slot6, self.slot7, self.slot8, self.slot9, self.slot10,
                              self.slot11, self.slot12, self.slot13, self.slot14, self.slot15,
                              self.slot16, self.slot17, self.slot18, self.slot19, self.slot20,
                              self.slot21, self.slot22, self.slot23, self.slot24, self.slot25]

        self.display_List = [self.amount1, self.amount2, self.amount3, self.amount4,
                             self.amount5, self.amount6, self.amount7, self.amount8]

        self.buy_price_display_list = [self.pb1, self.pb2, self.pb3, self.pb4,
                                       self.pb5, self.pb6, self.pb7, self.pb8, ]

        self.sell_price_display_list = [self.ps1, self.ps2, self.ps3, self.ps4,
                                        self.ps5, self.ps6, self.ps7, self.ps8]

        for x in range(8):  # display first prices and put icons on buttons
            self.buy_price_display_list[x].display(self.buy_prices[x])
            self.sell_price_display_list[x].display(self.sell_prices[x])
            self.chosen_plant_list[x].setIcon(QIcon(QPixmap(self.pictures[x])))

        self.money.display(self.current_Money)

    # method to buy new crops from store to inventory
    def item_bought(self, index):
        if (self.current_Money - self.buy_prices[index]) >= 0:
            self.inventory[index] = self.inventory[index] + 1
            self.display_List[index].display(self.inventory[index])
            self.current_Money -= self.buy_prices[index]
            self.money.display(self.current_Money)

    # method to sell own crops from inventory to store
    def item_sold(self, index):
        if self.inventory[index] > 0:
            self.inventory[index] = self.inventory[index] - 1
            self.display_List[index].display(self.inventory[index])
            self.current_Money += self.sell_prices[index]
            self.money.display(self.current_Money)

    # making buy and sell values change, happens every 20 seconds and sets new random values
    def rerollValues(self):
        random_buy_price = [1, 2, 3, 4, 5, 10, 20, 30]
        random_sell_price = [1, 2, 3, 4, 4, 8, 15, 20]

        for x in range(8):
            random_buy = random.randint(-random_buy_price[x], random_buy_price[x])
            random_sell = random.randint(-random_sell_price[x], random_sell_price[x])

            self.buy_prices[x] = self.buy_prices[x] + random_buy
            if self.buy_prices[x] <= 0:
                self.buy_prices[x] = 1
            self.sell_prices[x] = self.sell_prices[x] + random_sell
            if self.sell_prices[x] <= 0:
                self.sell_prices[x] = 1
            if x == 4:
                if self.buy_prices[x] < 10:
                    self.buy_prices[x] = 10
            if x == 5:
                if self.buy_prices[x] < 50:
                    self.buy_prices[x] = 50
            if x == 6:
                if self.buy_prices[x] < 100:
                    self.buy_prices[x] = 100
            if x == 7:
                if self.buy_prices[x] < 200:
                    self.buy_prices[x] = 200
            if self.sell_prices[x] > self.buy_prices[x]:
                self.sell_prices[x] = self.buy_prices[x]

            self.buy_price_display_list[x].display(self.buy_prices[x])
            self.sell_price_display_list[x].display(self.sell_prices[x])

    # setting currently chosen plant, after clicking on plant picture and then, on planting spot, a chosen plant will
    # be placed there
    def chosen_plant_change(self, index):
        self.chosen_plant = index

    # method that happens after collecting ready crops, two new crops will be added to inventory and plant picture
    # will be changed to an empty one. Also displays present inventory status
    def harvest(self, plant):
        if self.plant_class_list[plant].ready == True:
            self.inventory[self.plant_class_list[plant].index] += 2
            self.display_List[self.plant_class_list[plant].index].display(
                self.inventory[self.plant_class_list[plant].index])
            self.plant_class_list[plant].place.setIcon(QIcon(QPixmap('assets/empty.png')))

    # method that happens after clicking on an empty planting file. if it isnt occupied, currently chosen plant will
    # be placed there as a crop, new class controls if crop is already ready to harvest, if so, icon will be
    # changed. If the field is already occupied and the plant is ready to harvest, a proper methods will clear this
    # place and add crops to the inventory
    def place_plant(self, place_index):
        if self.already_planted[place_index] == False:
            if self.inventory[self.chosen_plant] > 0:
                crop1 = Plant_Class(self.grow_time[self.chosen_plant], self.planting_List[place_index],
                                    self.pictures[self.chosen_plant],
                                    self.chosen_plant,
                                    QPixmap('assets/icons2.png'))
                self.inventory[self.chosen_plant] -= 1
                self.update_display()
                self.plant_class_list[place_index] = crop1
                self.already_planted[place_index] = True
        elif self.already_planted[place_index] == True:
            self.harvest(place_index)
            if self.plant_class_list[place_index].ready == True:
                self.already_planted[place_index] = False

    # method to update all inventory displays
    def update_display(self):
        for x in range(8):
            self.display_List[x].display(self.inventory[x])

    ########################################################################################################################
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Desktop Farm"))
        self.label.setText(_translate("Form", "owned:"))
        self.buy1.setText(_translate("Form", "buy"))
        self.buy2.setText(_translate("Form", "buy"))
        self.buy3.setText(_translate("Form", "buy"))
        self.buy4.setText(_translate("Form", "buy"))
        self.buy8.setText(_translate("Form", "buy"))
        self.buy7.setText(_translate("Form", "buy"))
        self.buy5.setText(_translate("Form", "buy"))
        self.buy6.setText(_translate("Form", "buy"))
        self.sell3.setText(_translate("Form", "sell"))
        self.sell4.setText(_translate("Form", "sell"))
        self.sell5.setText(_translate("Form", "sell"))
        self.sell6.setText(_translate("Form", "sell"))
        self.sell1.setText(_translate("Form", "sell"))
        self.sell7.setText(_translate("Form", "sell"))
        self.sell2.setText(_translate("Form", "sell"))
        self.sell8.setText(_translate("Form", "sell"))
        self.label_2.setText(_translate("Form", "buy for:"))
        self.label_3.setText(_translate("Form", "sell for:"))


# start program
if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    Form.show()

    sys.exit(app.exec())
