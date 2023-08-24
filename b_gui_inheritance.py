import requests
import re

import sys
from PyQt5.QtWidgets import QApplication


from a_gui_from_ui import *
import sys
import openpyxl


# запускаем гуй после конвертации ui в py
class Mywindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Инициализируем пользовательский интерфейс

        # добавляем свой функционал в GUI
        self.pushButton_Record_to_Excel.clicked.connect(self.save_to_excel)

    def parse(self):
        inn = self.lineEdit_INN_QT_INPUT.text()

        url = 'https://egrul.nalog.ru'
        url_1 = 'https://egrul.nalog.ru/search-result/'

        r = requests.post(url, data={'query': inn})  # вставить инн в url в раздел дата
        r1 = requests.get(url_1 + r.json()['t'])
        print(r1.json())

    def save_to_excel(self):
        text_to_save = self.lineEdit_INN_QT_INPUT.text()

        # Открываем существующий файл или создаем новый
        wb = openpyxl.Workbook()
        sheet = wb.active

        # Записываем текст в ячейку A1
        sheet["A1"] = text_to_save

        # Сохраняем файл
        wb.save("example.xlsx")

        print("Текст сохранен в ячейке A1")

app = QApplication(sys.argv)
window = Mywindow()
window.show()
sys.exit(app.exec_())