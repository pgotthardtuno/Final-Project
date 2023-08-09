from logicFinal import *


def main():
    """
    This function launches the main window powered by PyQt, the Logic class determines how the gui script is executed
    :return:
    """
    application = QApplication([])
    window = Logic()
    window.show()
    application.exec()


if __name__ == '__main__':
    main()
