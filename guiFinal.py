# Form implementation generated from reading ui file 'Finalguis.ui'
#
# Created by: PyQt6 UI code generator 6.5.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.shop_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.shop_button.setGeometry(QtCore.QRect(310, 510, 171, 75))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.shop_button.setFont(font)
        self.shop_button.setObjectName("shop_button")
        self.exit_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.exit_button.setGeometry(QtCore.QRect(540, 530, 241, 61))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.exit_button.setFont(font)
        self.exit_button.setIconSize(QtCore.QSize(13, 13))
        self.exit_button.setObjectName("exit_button")
        self.shop_frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.shop_frame.setGeometry(QtCore.QRect(0, 0, 801, 501))
        self.shop_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.shop_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.shop_frame.setObjectName("shop_frame")
        self.water_qty = QtWidgets.QLineEdit(parent=self.shop_frame)
        self.water_qty.setGeometry(QtCore.QRect(580, 270, 113, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.water_qty.setFont(font)
        self.water_qty.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.water_qty.setObjectName("water_qty")
        self.sand_radio = QtWidgets.QRadioButton(parent=self.shop_frame)
        self.sand_radio.setGeometry(QtCore.QRect(280, 230, 250, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.sand_radio.setFont(font)
        self.sand_radio.setAutoExclusive(False)
        self.sand_radio.setObjectName("sand_radio")
        self.sand_qty = QtWidgets.QLineEdit(parent=self.shop_frame)
        self.sand_qty.setGeometry(QtCore.QRect(330, 270, 113, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sand_qty.setFont(font)
        self.sand_qty.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.sand_qty.setObjectName("sand_qty")
        self.water_radio = QtWidgets.QRadioButton(parent=self.shop_frame)
        self.water_radio.setGeometry(QtCore.QRect(550, 230, 200, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.water_radio.setFont(font)
        self.water_radio.setAutoExclusive(False)
        self.water_radio.setObjectName("water_radio")
        self.cart_menu = QtWidgets.QLabel(parent=self.shop_frame)
        self.cart_menu.setGeometry(QtCore.QRect(210, 340, 371, 111))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cart_menu.setFont(font)
        self.cart_menu.setText("")
        self.cart_menu.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignTop)
        self.cart_menu.setObjectName("cart_menu")
        self.cookie_qty = QtWidgets.QLineEdit(parent=self.shop_frame)
        self.cookie_qty.setGeometry(QtCore.QRect(90, 270, 113, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cookie_qty.setFont(font)
        self.cookie_qty.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.cookie_qty.setObjectName("cookie_qty")
        self.addcart_button = QtWidgets.QPushButton(parent=self.shop_frame)
        self.addcart_button.setGeometry(QtCore.QRect(270, 300, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.addcart_button.setFont(font)
        self.addcart_button.setObjectName("addcart_button")
        self.cookie_radio = QtWidgets.QRadioButton(parent=self.shop_frame)
        self.cookie_radio.setGeometry(QtCore.QRect(60, 230, 220, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cookie_radio.sizePolicy().hasHeightForWidth())
        self.cookie_radio.setSizePolicy(sizePolicy)
        self.cookie_radio.setMaximumSize(QtCore.QSize(300, 100))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.cookie_radio.setFont(font)
        self.cookie_radio.setIconSize(QtCore.QSize(30, 30))
        self.cookie_radio.setAutoExclusive(False)
        self.cookie_radio.setObjectName("cookie_radio")
        self.check_button = QtWidgets.QPushButton(parent=self.shop_frame)
        self.check_button.setGeometry(QtCore.QRect(270, 460, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.check_button.setFont(font)
        self.check_button.setObjectName("check_button")
        self.goback_button = QtWidgets.QPushButton(parent=self.shop_frame)
        self.goback_button.setGeometry(QtCore.QRect(270, 300, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.goback_button.setFont(font)
        self.goback_button.setObjectName("goback_button")
        self.cookie_image = QtWidgets.QLabel(parent=self.shop_frame)
        self.cookie_image.setGeometry(QtCore.QRect(40, 0, 225, 225))
        self.cookie_image.setObjectName("cookie_image")
        self.sand_image = QtWidgets.QLabel(parent=self.shop_frame)
        self.sand_image.setGeometry(QtCore.QRect(270, 30, 263, 191))
        self.sand_image.setObjectName("sand_image")
        self.water_image = QtWidgets.QLabel(parent=self.shop_frame)
        self.water_image.setGeometry(QtCore.QRect(540, 0, 225, 225))
        self.water_image.setObjectName("water_image")
        self.goback_button.raise_()
        self.water_qty.raise_()
        self.sand_radio.raise_()
        self.sand_qty.raise_()
        self.water_radio.raise_()
        self.cart_menu.raise_()
        self.cookie_qty.raise_()
        self.addcart_button.raise_()
        self.cookie_radio.raise_()
        self.check_button.raise_()
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 530, 241, 61))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.scrollArea = QtWidgets.QScrollArea(parent=self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(10, 9, 781, 491))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignTop)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 779, 489))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.label = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        self.label.setGeometry(QtCore.QRect(30, 20, 721, 451))
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignTop)
        self.label.setObjectName("label")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.receipt = QtWidgets.QLabel(parent=self.centralwidget)
        self.receipt.setGeometry(QtCore.QRect(200, 200, 399, 300))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.receipt.setFont(font)
        self.receipt.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.receipt.setText("")
        self.receipt.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignTop)
        self.receipt.setObjectName("receipt")
        self.welcome_message = QtWidgets.QLabel(parent=self.centralwidget)
        self.welcome_message.setGeometry(QtCore.QRect(10, 9, 781, 491))
        font = QtGui.QFont()
        font.setPointSize(40)
        font.setItalic(False)
        self.welcome_message.setFont(font)
        self.welcome_message.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.welcome_message.setObjectName("welcome_message")
        self.scrollArea.raise_()
        self.exit_button.raise_()
        self.shop_button.raise_()
        self.shop_button.raise_()
        self.exit_button.raise_()
        self.water_image.raise_()
        self.sand_image.raise_()
        self.cookie_image.raise_()
        self.pushButton.raise_()
        self.receipt.raise_()
        self.welcome_message.raise_()
        self.shop_frame.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "It3m Shop"))
        self.shop_button.setText(_translate("MainWindow", "SHOP"))
        self.exit_button.setText(_translate("MainWindow", "Shutdown"))
        self.water_qty.setPlaceholderText(_translate("MainWindow", "Enter Quantity"))
        self.sand_radio.setText(_translate("MainWindow", "SANDWICH - $4.00"))
        self.sand_qty.setPlaceholderText(_translate("MainWindow", "Enter Quantity"))
        self.water_radio.setText(_translate("MainWindow", "WATER - $1.00"))
        self.cookie_qty.setPlaceholderText(_translate("MainWindow", "Enter Quantity"))
        self.addcart_button.setText(_translate("MainWindow", "Create Cart"))
        self.cookie_radio.setText(_translate("MainWindow", "COOKIE - $1.50"))
        self.check_button.setText(_translate("MainWindow", "Checkout"))
        self.goback_button.setText(_translate("MainWindow", "Go Back"))
        self.cookie_image.setText(_translate("MainWindow", "<html><head/><body><p><img src=\"cookie.jpg\"/></p></body></html>"))
        self.sand_image.setText(_translate("MainWindow", "<html><head/><body><p><img src=\"sandwich.jpg\"/></p></body></html>"))
        self.water_image.setText(_translate("MainWindow", "<html><head/><body><p><img src=\"water.jpg\"/></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Session Log"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.welcome_message.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:36pt; font-weight:600;\">Cookies </span></p><p><span style=\" font-size:36pt; font-weight:600;\">Sandwiches </span></p><p><span style=\" font-size:36pt; font-weight:600;\">Water </span></p><p><span style=\" font-size:36pt; text-decoration: underline;\">AND NOTHING ELSE</span></p><p><span style=\" font-size:36pt; font-style:italic;\">Guaranteed!</span></p></body></html>"))
