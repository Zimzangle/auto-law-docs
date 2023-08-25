import requests
import re
import os

import sys
from PyQt5.QtWidgets import QApplication, QMessageBox, QComboBox


from a_gui_from_ui import *
import sys
from datetime import datetime
from openpyxl import load_workbook


# запускаем гуй после конвертации ui в py
class Mywindow(QtWidgets.QMainWindow, Ui_MainWindow, QMessageBox, QComboBox):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Инициализируем пользовательский интерфейс

        # добавляем функционал кнопок - ссылка на функции парсинг и сохр в эксель
        self.pushButton_Parse.clicked.connect(self.inn_check)
        self.pushButton_Record_to_Excel.clicked.connect(self.save_to_excel)

        # для выбора xlsm файла
        self.add_files_to_combo()

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
            nameOOO = str(r2['rows'][0]['c'])  # название контрагента ООО "КТото"
            nameOOO_here = re.search(r'(?<=").*?(?=")', nameOOO)  # найти текст между кавычек # print(nameOOO_first[0]) нужен индекс
            self.lineEdit_NAME_organization.setText(nameOOO_here[0])

            nameOOO_form = re.split(r'"', nameOOO)  # разделить строку на словарь по символу " # print(nameOOO_last[0])
            self.lineEdit_form.setText(nameOOO_form[0])

            adressOOO = str(r2['rows'][0]['a'])
            self.textEdit_adress.setText(adressOOO)

            seoOOO = str(r2['rows'][0]['g'])
            seoOOO_name = re.split(r': ', seoOOO)  # print(seoOOO_name [0]) и print(seoOOO_seo [1])
            self.lineEdit_seo_name.setText(seoOOO_name[1])

            seoOOO_director_position = str(seoOOO_name[0]).capitalize()
            self.lineEdit_seo_director_position.setText(seoOOO_director_position)

            # self добавляем чтобы можно было использовать из другого метода(другой функции) класса
            self.innOOO = str(r2['rows'][0]['i'])
            self.ogrnOOO = str(r2['rows'][0]['o'])
            self.kppOOO = str(r2['rows'][0]['p'])
        # для ИП
        elif len(inn) == 12 or len(inn) == 15:
            nameOOO = str.title(r2['rows'][0]['n'])  # str.title - первая буква заглавнаяу ФИО ИП
            self.lineEdit_NAME_organization.setText(nameOOO)

            self.ogrnOOO = str(r2['rows'][0]['o'])
            self.innOOO = str(r2['rows'][0]['i'])
        else:
            print("Ошибка в ИНН/ОГРН")

        #выбор xlsm файла
    def add_files_to_combo(self):
        current_directory = os.path.dirname(os.path.abspath(__file__))

        for filename in os.listdir(current_directory):
            if filename.endswith(".xlsm"):
                self.comboBox_xslm_choice.addItem(filename)


    def save_to_excel(self):
        selected_xlsm = self.comboBox_xslm_choice.currentText()
        choice_my_organization = re.search(r' (?P<found_text>.*?)\.', selected_xlsm)[1] # найти текст между пробелом и точкой а [1] убирает пробел

        wb = load_workbook(selected_xlsm, read_only=False, keep_vba=True)  # после фн аргументы, чтобы можно было читать xlsm с макросами
        ws = wb['BD']  # имя листа
        last_record = (int(ws.max_row) + 1)  # найти номер незаполненной строки

        # print(str('A') + str(last_record)) # номер ячейки
        # ячейка А
        dogovor_excel_formula = str('=CONCATENATE(' + str("S" + str(last_record))) + str('," Договор № ",E') + str(
            last_record) + str('," от ",TEXT(F') + str(last_record) + str(',"ДД.ММ.ГГ "),D') + str(last_record) + str(
            ')')
        ws[str('A') + str(last_record)] = dogovor_excel_formula

        # переделать В и С
        ws[str('B') + str(last_record)] = "-"
        ws[str('C') + str(last_record)] = '-'

        # ячейки парсера забираем из введенного текста в форму
        ws[str('D') + str(last_record)] = self.lineEdit_NAME_organization.text()
        ws[str('J') + str(last_record)] = self.lineEdit_form.text()
        ws[str('L') + str(last_record)] = self.lineEdit_seo_director_position.text()
        ws[str('N') + str(last_record)] = self.lineEdit_seo_name.text()
        # ws[str('V') + str(last_record)] = self.kppOOO # не может найти у ип и крашится
        ws[str('W') + str(last_record)] = self.textEdit_adress.toPlainText()
        ws[str('U') + str(last_record)] = self.ogrnOOO
        ws[str('T') + str(last_record)] = self.innOOO



        # Сохраняем файл
        wb.save(selected_xlsm)

        print("Текст сохранен в ячейке A1")
        print(self.innOOO)

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