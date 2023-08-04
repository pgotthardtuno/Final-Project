from PyQt6.QtWidgets import *
from guiFinal import *
import csv

class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.log_create()
        self.cnum = 1

        self.shop_button.clicked.connect(lambda: self.shopsubmit())
        self.addcart_button.clicked.connect(lambda: self.cartsubmit())
        self.exit_button.clicked.connect(lambda: self.exitsubmit())
        self.pushButton.clicked.connect(lambda: self.logsubmit())
        self.check_button.clicked.connect(lambda: self.checksubmit())
        self.goback_button.clicked.connect(lambda: self.gobacksubmit())

        self.shop_frame.hide()
        self.scrollArea.hide()
        self.receipt.hide()

    def shopsubmit(self):
        self.welcome_message.hide()
        self.shop_frame.show()
        self.scrollArea.hide()
        self.receipt.hide()
        self.check_button.hide()
        self.goback_button.hide()
        self.addcart_button.show()
        #cleanup
        self.cart_menu.setText('')
        self.cookie_qty.setText('')
        self.sand_qty.setText('')
        self.water_qty.setText('')
        self.cookie_radio.setChecked(False)
        self.sand_radio.setChecked(False)
        self.water_radio.setChecked(False)

    def cartsubmit(self):
        # check if any radio is selected and that there a quantity in the box
        self.cookieq = self.cookie_qty.text()
        self.sandq = self.sand_qty.text()
        self.waterq = self.water_qty.text()

        if self.cookie_radio.isChecked():
            if self.cookieq == 0 or self.cookieq == '':
                self.cart_menu.setText('Please set a quantity for each selected item')
                return
        if self.sand_radio.isChecked():
            if self.sandq == 0 or self.sandq == '':
                self.cart_menu.setText('Please set a quantity for each selected item')
                return
        if self.water_radio.isChecked():
            if self.waterq == 0 or self.waterq == '':
                self.cart_menu.setText('Please set a quantity for each selected item')
                return
        if self.cookie_radio.isChecked() == False and self.sand_radio.isChecked() == False and self.water_radio.isChecked() == False:
            self.cart_menu.setText('')
            self.cart_menu.setText('Please select at least one item to add to the cart')
            return

        #input box validation
        self.cart_menu.setText('')
        if self.cookieq.isnumeric() != True and self.cookieq != '':
            self.cart_menu.setText('')
            self.cart_menu.setText(f'Quantity needs to be a whole number\ne. g. 10 not -10 or 10.25')
            return
        elif self.cookieq == '':
            self.cookieq = 0

        if self.sandq.isnumeric() != True and self.sandq != '':
            self.cart_menu.setText('')
            self.cart_menu.setText(f'Quantity needs to be a whole number\ne. g. 10 not -10 or 10.25')
            return
        elif self.sandq == '':
            self.sandq = 0

        if self.waterq.isnumeric() != True and self.waterq != '':
            self.cart_menu.setText('')
            self.cart_menu.setText(f'Quantity needs to be a whole number\ne. g. 10 not -10 or 10.25')
            return
        elif self.waterq == '':
            self.waterq = 0

        self.cookiesum = 0.00
        self.sandsum = 0.00
        self.watersum = 0.00

        # math for items purchased
        if self.cookie_radio.isChecked():
            self.cookiesum = float(self.cookieq) * 1.50
        if self.sand_radio.isChecked():
            self.sandsum = float(self.sandq) * 4.00
        if self.water_radio.isChecked():
            self.watersum = float(self.waterq) * 1.00

        self.totalsum = self.cookiesum + self.sandsum + self.watersum

        # cart menu
        self.cart_menu.setText('')
        self.cart_menu.setText(f'Your Shopping Cart'
                               f'\n({self.cookieq}) - Cookie = ${self.cookiesum:.2f}'
                               f'\n({self.sandq}) - Sandwich = ${self.sandsum:.2f}'
                               f'\n({self.waterq}) - Water = ${self.watersum:.2f}'
                               f'\nGRAND TOTAL = ${self.totalsum:.2f}')

        # if all goes well the checkout button will appear
        self.check_button.show()
        self.goback_button.show()
        self.addcart_button.hide()

    def checksubmit(self):
        self.shop_frame.hide()
        self.receipt.setText(f'Thank you!'
                             f'\nYou were customer number {self.cnum}'
                             f'\nToday you purchased:'
                             f'\n({self.cookieq}) - Cookie for ${self.cookiesum:.2f}'
                             f'\n({self.sandq}) - Sandwich for ${self.sandsum:.2f}'
                             f'\n({self.waterq}) - Water for ${self.watersum:.2f}'
                             f'\nYour Grand Total was ${self.totalsum:.2f}')
        self.receipt.show()


        # submit the checkout data to the session's csv log file
        loginput = (self.cnum, self.cookieq, f'{self.cookiesum:.2f}',self.sandq,f'{self.sandsum:.2f}',self.waterq,
                    f'{self.watersum:.2f}',f'{self.totalsum:.2f}')
        with open(f'logs/{self.session_id}.csv','a') as file1:
            writer = csv.writer(file1,lineterminator='')
            writer.writerow('\n')
            writer.writerow(loginput)

        self.cnum += 1


    def gobacksubmit(self):
        self.addcart_button.show()
        self.cart_menu.setText('')
        # clean up
        self.cookie_qty.setText('')
        self.sand_qty.setText('')
        self.water_qty.setText('')
        self.cookie_radio.setChecked(False)
        self.sand_radio.setChecked(False)
        self.water_radio.setChecked(False)
        self.check_button.hide()
        self.goback_button.hide()
    def logsubmit(self):
        self.shop_frame.hide()
        self.receipt.hide()
        self.scrollArea.show()
        start_string = ''
        with open(f'logs/{self.session_id2}.csv','r') as file1:
            reader = csv.reader(file1)
            header = next(reader)
            for line in reader:
                start_string += f'Customer {line[0]} purchased ({line[1]}) COOKIE for ${line[2]}' \
                                f' and ({line[3]}) SANDWICH for ${line[4]}' \
                                f' and ({line[5]}) WATER for ${line[6]}' \
                                f' GRAND TOTAL of ${line[7]}\n'


        self.label.setText(f'{start_string}')
    def exitsubmit(self):
        self.close()

    def log_create(self):
        import os

        # create the logs folder
        from datetime import datetime
        current_directory = os.getcwd()
        new_directory = os.path.join(current_directory, r'logs')
        if not os.path.exists(new_directory):
            os.makedirs(new_directory)

        # create the unique log csv file
        self.session_id = datetime.now().strftime("%H%M-%d%m%Y")
        self.session_id2 = self.session_id
        with open(f'logs/{self.session_id}.csv','w') as file1:
            writer = csv.writer(file1,lineterminator='')
            header = ('Customer_#', 'Cookie_QTY', 'Cookie_SUM', 'Sandwich_QTY', 'Sandwich_SUM', 'Water_QTY', 'Water_SUM', 'GRAND_TOTAL')
            writer.writerow(header)



# todo list
# line things up better
# add in type hinting and descriptions for methods