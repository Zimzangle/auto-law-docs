import requests
import re

import sys
from PyQt5.QtWidgets import QApplication, QMessageBox


from a_gui_from_ui import *
import sys
import openpyxl


# запускаем гуй после конвертации ui в py
class Mywindow(QtWidgets.QMainWindow, Ui_MainWindow, QMessageBox):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Инициализируем пользовательский интерфейс

        # добавляем функционал кнопок - ссылка на функции парсинг и сохр в эксель
        self.pushButton_Parse.clicked.connect(self.inn_check)
        self.pushButton_Record_to_Excel.clicked.connect(self.save_to_excel)

    def inn_check(self):
        inn = self.lineEdit_INN_QT_INPUT.text()

        # проверка правильности ввода ИНН

        if len(inn) == 10 or len(inn) == 12 or len(inn) == 13 or len(inn) == 15:
            self.parse(inn)
        else:
            print('Ошибка в ИНН/ОГРН. Попробуйте еще раз')
            self.show_error_notification()

    def parse(self, inn):
        # сам парсинг
        url = 'https://egrul.nalog.ru'
        url_1 = 'https://egrul.nalog.ru/search-result/'

        r = requests.post(url, data={'query': inn})  # вставить инн в url в раздел дата
        r1 = requests.get(url_1 + r.json()['t'])
        r2 = r1.json()

        self.add_to_gui_parse_results(inn, r2)

    def add_to_gui_parse_results (self, inn, r2):
        if len(inn) == 10 or len(inn) == 13:
            adressOOO = str(r2['rows'][0]['a'])
            nameOOO = str(r2['rows'][0]['c'])  # название контрагента ООО "КТото"
            nameOOO_first = re.search(r'(?<=").*?(?=")', nameOOO)  # найти текст между кавычек # print(nameOOO_first[0]) нужен индекс
            nameOOO_second = re.split(r'"', nameOOO)  # разделить строку на словарь по символу " # print(nameOOO_last[0])

            seoOOO = str(r2['rows'][0]['g'])
            seoOOO_name = re.split(r': ', seoOOO)  # print(seoOOO_name [0]) и print(seoOOO_seo [1])
            seoOOO_name_DIRECTOR1 = str(seoOOO_name[0])
            seoOOO_name_Direcor2 = seoOOO_name_DIRECTOR1.capitalize()

            innOOO = str(r2['rows'][0]['i'])
            ogrnOOO = str(r2['rows'][0]['o'])
            kppOOO = str(r2['rows'][0]['p'])

        elif len(inn) == 12 or len(inn) == 15:
            nameOOO_IP = str.title(r2['rows'][0]['n'])  # str.title - первая буква заглавнаяу ФИО ИП
            ogrnOOO_IP = str(r2['rows'][0]['o'])
            innOOO_IP = str(r2['rows'][0]['i'])
        else:
            print("Ошибка в ИНН/ОГРН")

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

    def show_error_notification(self):
        error_box = QMessageBox()  # Создаем окно уведомления
        error_box.setIcon(QMessageBox.Critical)  # Устанавливаем иконку ошибки
        error_box.setWindowTitle("Ошибка")  # Устанавливаем заголовок окна
        error_box.setText("Ошибка в номере ИНН/ОГРН. Исправьте")  # Устанавливаем текст ошибки
        error_box.exec_()  # Показываем окно уведомления и блокируем основное окно приложения


app = QApplication(sys.argv)
window = Mywindow()
window.show()
sys.exit(app.exec_())