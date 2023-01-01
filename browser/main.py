import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtWebEngineWidgets  # pip install PyQtWebEngine
import authorization
from about import *
from des import *


# Окно авторизации
class auth_window(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.auth = authorization.Ui_Form()
        self.auth.setupUi(self)
        self.setWindowModality(2)

        # Основные обработчики
        self.validate_flag = False
        self.auth.lineEdit.setPlaceholderText('Password..')
        self.auth.pushButton.clicked.connect(self.check_passw)

    def check_passw(self):
        text = self.auth.lineEdit.text()
        
        if len(text) > 0:
            with open('data\\config.txt') as file:
                reader = file.read()

            if text == reader:
                self.validate_flag = True
                self.close()

    def closeEvent(self, value):
        if not self.validate_flag:
            raise SystemExit
               

# Основной класс интерфейса
class GUI(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Текущая тема
        self.white_theme = True

        # Инициализация WebView
        self.web = QtWebEngineWidgets.QWebEngineView()
        self.ui.gridLayout.addWidget(self.web, 1, 0, 1, 7)

        # Обработчики кнопок
        self.ui.toolButton.clicked.connect(self.back)
        self.ui.toolButton_2.clicked.connect(self.update)
        self.ui.toolButton_3.clicked.connect(self.search)
        self.ui.toolButton_4.clicked.connect(self.about)
        self.ui.toolButton_5.clicked.connect(self.home)
        self.ui.toolButton_6.clicked.connect(self.change_themes)

        # Подсказки
        self.ui.toolButton.setToolTip('Назад')
        self.ui.toolButton_2.setToolTip('Обновить')
        self.ui.toolButton_3.setToolTip('Поиск')
        self.ui.toolButton_4.setToolTip('О программе')
        self.ui.toolButton_5.setToolTip('Главная')
        self.ui.toolButton_6.setToolTip('Сменить тему')


    # Домашняя страница
    def home(self):
        home_page = QtCore.QUrl('https://duckduckgo.com')
        self.web.load(home_page)

    # Обновить страницу
    def update(self):
        self.web.reload()

    # Шаг назад
    def back(self):
        self.web.back()

    # Поиск информации
    def search(self):
        text = self.ui.lineEdit.text()

        if len(text) > 0:
            # Проверка ввода
            if not text.startswith('http'):
                text = QtCore.QUrl('https://duckduckgo.com/?q=' + text)
            else:
                text = QtCore.QUrl(text)
            self.web.load(text)

    # Информация о разработчике
    def about(self):
        window = about_information(self)
        window.setGeometry(QtWidgets.QStyle.alignedRect(QtCore.Qt.LeftToRight, QtCore.Qt.AlignCenter, window.size(), self.geometry()))
        window.show()

    # Выбрать другую тему
    def change_themes(self):
        default_style = '''
            QMainWindow {
            }
            '''
        
        style = '''
            QMainWindow {
                background-color: #3B3B3B;
            }
            '''

        if self.white_theme:
            self.white_theme = False
            self.setStyleSheet(style)
            icon = QtGui.QIcon('icon\\black.png')
            size = QtCore.QSize(20, 20)
            self.ui.toolButton_6.setIcon(icon)
            self.ui.toolButton_6.setIconSize(size)
        else:
            self.white_theme = True
            self.setStyleSheet(default_style)
            icon = QtGui.QIcon('icon\\iconfinder_General_Office_65_2530844.png')
            size = QtCore.QSize(20, 20)
            self.ui.toolButton_6.setIcon(icon)
            self.ui.toolButton_6.setIconSize(size)


# Класс с информацией о разработчике
class about_information(QtWidgets.QWidget):
    def __init__(self, parent = GUI):
        super().__init__(parent, QtCore.Qt.Window)
        self.modal = Ui_Form()
        self.modal.setupUi(self)
        self.setWindowModality(2)



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mywin = GUI()
    auth = auth_window()
    mywin.show()
    auth.show()
    sys.exit(app.exec_())

