# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'data_py/gui/untitled_a.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(745, 639)
        font = QtGui.QFont()
        font.setStrikeOut(False)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("data_py/gui\\favicon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit_INN_QT_INPUT = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_INN_QT_INPUT.setGeometry(QtCore.QRect(280, 90, 201, 21))
        self.lineEdit_INN_QT_INPUT.setObjectName("lineEdit_INN_QT_INPUT")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(300, 70, 141, 20))
        self.label.setObjectName("label")
        self.pushButton_Record_to_Excel = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Record_to_Excel.setGeometry(QtCore.QRect(430, 490, 111, 21))
        self.pushButton_Record_to_Excel.setStyleSheet("  background-color: #3498db;")
        self.pushButton_Record_to_Excel.setObjectName("pushButton_Record_to_Excel")
        self.pushButton_Parse = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Parse.setGeometry(QtCore.QRect(520, 80, 151, 31))
        self.pushButton_Parse.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_Parse.setObjectName("pushButton_Parse")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 10, 281, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(450, 20, 271, 20))
        font = QtGui.QFont()
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_4.setStyleSheet("color: blue;")
        self.label_4.setOpenExternalLinks(True)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(620, 40, 91, 16))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.comboBox_xslm_choice = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_xslm_choice.setGeometry(QtCore.QRect(40, 90, 171, 22))
        self.comboBox_xslm_choice.setObjectName("comboBox_xslm_choice")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(60, 70, 121, 16))
        self.label_6.setObjectName("label_6")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(500, 430, 141, 20))
        self.label_14.setObjectName("label_14")
        self.comboBox_docfate = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_docfate.setGeometry(QtCore.QRect(460, 460, 211, 21))
        self.comboBox_docfate.setEditable(True)
        self.comboBox_docfate.setObjectName("comboBox_docfate")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(30, 180, 361, 351))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.textEdit_adress = QtWidgets.QTextEdit(self.tab)
        self.textEdit_adress.setGeometry(QtCore.QRect(10, 80, 321, 61))
        self.textEdit_adress.setObjectName("textEdit_adress")
        self.lineEdit_NAME_organization = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_NAME_organization.setGeometry(QtCore.QRect(10, 30, 321, 31))
        self.lineEdit_NAME_organization.setObjectName("lineEdit_NAME_organization")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(110, 10, 121, 16))
        self.label_2.setObjectName("label_2")
        self.label_18 = QtWidgets.QLabel(self.tab)
        self.label_18.setGeometry(QtCore.QRect(140, 60, 47, 13))
        self.label_18.setObjectName("label_18")
        self.lineEdit_seo_director_position = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_seo_director_position.setGeometry(QtCore.QRect(10, 280, 321, 31))
        self.lineEdit_seo_director_position.setObjectName("lineEdit_seo_director_position")
        self.label_12 = QtWidgets.QLabel(self.tab)
        self.label_12.setGeometry(QtCore.QRect(120, 140, 91, 16))
        self.label_12.setObjectName("label_12")
        self.lineEdit_form = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_form.setGeometry(QtCore.QRect(10, 160, 321, 31))
        self.lineEdit_form.setObjectName("lineEdit_form")
        self.label_11 = QtWidgets.QLabel(self.tab)
        self.label_11.setGeometry(QtCore.QRect(110, 260, 141, 16))
        self.label_11.setObjectName("label_11")
        self.label_10 = QtWidgets.QLabel(self.tab)
        self.label_10.setGeometry(QtCore.QRect(120, 200, 101, 16))
        self.label_10.setObjectName("label_10")
        self.lineEdit_seo_name = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_seo_name.setGeometry(QtCore.QRect(10, 220, 321, 31))
        self.lineEdit_seo_name.setObjectName("lineEdit_seo_name")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.lineEdit_NAME_organization_2 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_NAME_organization_2.setGeometry(QtCore.QRect(20, 30, 321, 31))
        self.lineEdit_NAME_organization_2.setObjectName("lineEdit_NAME_organization_2")
        self.label_16 = QtWidgets.QLabel(self.tab_2)
        self.label_16.setGeometry(QtCore.QRect(160, 10, 31, 16))
        self.label_16.setObjectName("label_16")
        self.textEdit_adress_2 = QtWidgets.QTextEdit(self.tab_2)
        self.textEdit_adress_2.setGeometry(QtCore.QRect(20, 90, 321, 61))
        self.textEdit_adress_2.setObjectName("textEdit_adress_2")
        self.label_19 = QtWidgets.QLabel(self.tab_2)
        self.label_19.setGeometry(QtCore.QRect(160, 70, 47, 13))
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.tab_2)
        self.label_20.setGeometry(QtCore.QRect(110, 160, 161, 16))
        self.label_20.setObjectName("label_20")
        self.textEdit_pasport = QtWidgets.QTextEdit(self.tab_2)
        self.textEdit_pasport.setGeometry(QtCore.QRect(20, 180, 321, 61))
        self.textEdit_pasport.setObjectName("textEdit_pasport")
        self.tabWidget.addTab(self.tab_2, "")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget_2.setGeometry(QtCore.QRect(430, 320, 271, 111))
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.label_21 = QtWidgets.QLabel(self.tab_3)
        self.label_21.setGeometry(QtCore.QRect(40, 40, 171, 20))
        self.label_21.setObjectName("label_21")
        self.lineEdit_number_email = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_number_email.setGeometry(QtCore.QRect(10, 60, 211, 20))
        self.lineEdit_number_email.setObjectName("lineEdit_number_email")
        self.lineEdit_time_to_pay = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_time_to_pay.setGeometry(QtCore.QRect(50, 20, 113, 20))
        self.lineEdit_time_to_pay.setObjectName("lineEdit_time_to_pay")
        self.label_15 = QtWidgets.QLabel(self.tab_3)
        self.label_15.setGeometry(QtCore.QRect(50, 0, 121, 16))
        self.label_15.setObjectName("label_15")
        self.tabWidget_2.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.lineEdit_debt_sum = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_debt_sum.setGeometry(QtCore.QRect(70, 30, 101, 20))
        self.lineEdit_debt_sum.setObjectName("lineEdit_debt_sum")
        self.label_23 = QtWidgets.QLabel(self.tab_4)
        self.label_23.setGeometry(QtCore.QRect(20, 10, 201, 16))
        self.label_23.setObjectName("label_23")
        self.tabWidget_2.addTab(self.tab_4, "")
        self.comboBox_type_doc = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_type_doc.setGeometry(QtCore.QRect(430, 220, 261, 21))
        self.comboBox_type_doc.setEditable(True)
        self.comboBox_type_doc.setObjectName("comboBox_type_doc")
        self.lineEdit_number_docs = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_number_docs.setGeometry(QtCore.QRect(520, 170, 191, 20))
        self.lineEdit_number_docs.setObjectName("lineEdit_number_docs")
        self.lineEdit_date = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_date.setGeometry(QtCore.QRect(430, 170, 71, 20))
        self.lineEdit_date.setObjectName("lineEdit_date")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(420, 150, 91, 20))
        self.label_8.setObjectName("label_8")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(580, 150, 101, 20))
        self.label_7.setObjectName("label_7")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(530, 200, 81, 16))
        self.label_13.setObjectName("label_13")
        self.label_22 = QtWidgets.QLabel(self.centralwidget)
        self.label_22.setGeometry(QtCore.QRect(500, 300, 141, 16))
        self.label_22.setObjectName("label_22")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(400, 140, 20, 441))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(40, 50, 671, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_25 = QtWidgets.QLabel(self.centralwidget)
        self.label_25.setGeometry(QtCore.QRect(510, 250, 111, 16))
        self.label_25.setObjectName("label_25")
        self.comboBox_name_doc = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_name_doc.setGeometry(QtCore.QRect(430, 270, 261, 21))
        self.comboBox_name_doc.setEditable(True)
        self.comboBox_name_doc.setObjectName("comboBox_name_doc")
        self.pushButton_cancel_record = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_cancel_record.setEnabled(False)
        self.pushButton_cancel_record.setGeometry(QtCore.QRect(600, 490, 101, 21))
        self.pushButton_cancel_record.setStyleSheet("background-color: rgb(255, 156, 158);")
        self.pushButton_cancel_record.setObjectName("pushButton_cancel_record")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(40, 130, 671, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.checkBox_no_parser = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_no_parser.setGeometry(QtCore.QRect(300, 120, 151, 17))
        self.checkBox_no_parser.setObjectName("checkBox_no_parser")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(30, 150, 351, 16))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.checkBox_number = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_number.setGeometry(QtCore.QRect(50, 117, 211, 20))
        self.checkBox_number.setChecked(True)
        self.checkBox_number.setObjectName("checkBox_number")
        self.pushButton_open_excel = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_open_excel.setEnabled(True)
        self.pushButton_open_excel.setGeometry(QtCore.QRect(530, 570, 101, 21))
        self.pushButton_open_excel.setStyleSheet("background-color: rgb(243, 255, 105);")
        self.pushButton_open_excel.setObjectName("pushButton_open_excel")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(390, 0, 331, 16))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(350, 0, 3, 61))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.label_24 = QtWidgets.QLabel(self.centralwidget)
        self.label_24.setGeometry(QtCore.QRect(430, 530, 61, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.textBrowser_result = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_result.setEnabled(False)
        self.textBrowser_result.setGeometry(QtCore.QRect(500, 520, 201, 41))
        self.textBrowser_result.setObjectName("textBrowser_result")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 745, 21))
        self.menubar.setObjectName("menubar")
        self.menu_excel = QtWidgets.QMenu(self.menubar)
        self.menu_excel.setObjectName("menu_excel")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        self.menu_4 = QtWidgets.QMenu(self.menubar)
        self.menu_4.setObjectName("menu_4")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action123 = QtWidgets.QAction(MainWindow)
        self.action123.setObjectName("action123")
        self.action_settings = QtWidgets.QAction(MainWindow)
        self.action_settings.setObjectName("action_settings")
        self.action_open_excel = QtWidgets.QAction(MainWindow)
        self.action_open_excel.setObjectName("action_open_excel")
        self.action_readme = QtWidgets.QAction(MainWindow)
        self.action_readme.setObjectName("action_readme")
        self.action_clear_default = QtWidgets.QAction(MainWindow)
        self.action_clear_default.setObjectName("action_clear_default")
        self.action_clear_all = QtWidgets.QAction(MainWindow)
        self.action_clear_all.setObjectName("action_clear_all")
        self.action_clear_inn = QtWidgets.QAction(MainWindow)
        self.action_clear_inn.setObjectName("action_clear_inn")
        self.action_info_author = QtWidgets.QAction(MainWindow)
        self.action_info_author.setObjectName("action_info_author")
        self.actionTelegram = QtWidgets.QAction(MainWindow)
        self.actionTelegram.setObjectName("actionTelegram")
        self.actionInstagram = QtWidgets.QAction(MainWindow)
        self.actionInstagram.setObjectName("actionInstagram")
        self.actionPixelpravo_ru = QtWidgets.QAction(MainWindow)
        self.actionPixelpravo_ru.setObjectName("actionPixelpravo_ru")
        self.action_text_for_letter = QtWidgets.QAction(MainWindow)
        self.action_text_for_letter.setObjectName("action_text_for_letter")
        self.actionYouTube = QtWidgets.QAction(MainWindow)
        self.actionYouTube.setObjectName("actionYouTube")
        self.menu_excel.addAction(self.action_open_excel)
        self.menu_excel.addAction(self.action_text_for_letter)
        self.menu_2.addAction(self.action_readme)
        self.menu_2.addAction(self.action_info_author)
        self.menu_2.addAction(self.action_settings)
        self.menu_3.addAction(self.action_clear_default)
        self.menu_3.addAction(self.action_clear_inn)
        self.menu_3.addAction(self.action_clear_all)
        self.menu_4.addAction(self.actionTelegram)
        self.menu_4.addAction(self.actionInstagram)
        self.menu_4.addAction(self.actionPixelpravo_ru)
        self.menu_4.addAction(self.actionYouTube)
        self.menubar.addAction(self.menu_excel.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menubar.addAction(self.menu_4.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Zimzangle: Реестр договоров и писем"))
        self.label.setText(_translate("MainWindow", "2. Введите ИНН или ОГРН"))
        self.pushButton_Record_to_Excel.setText(_translate("MainWindow", "Записать в excel"))
        self.pushButton_Parse.setText(_translate("MainWindow", "3. Подтвердить ввод ИНН"))
        self.label_3.setText(_translate("MainWindow", "Zimzangle: Реестр договоров и писем"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><a href=\"https://www.pixelpravo.ru\"><span style=\" text-decoration: underline; color:#0000ff;\">© Nikolai Slesarenko (юрист), Мой сайт: pixelpravo.ru</span></a></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "3221208@mail.ru"))
        self.label_6.setText(_translate("MainWindow", "1. Выбирите excel файл"))
        self.label_14.setText(_translate("MainWindow", "Что сделано с документом"))
        self.label_2.setText(_translate("MainWindow", "Название организации"))
        self.label_18.setText(_translate("MainWindow", "Адрес"))
        self.label_12.setText(_translate("MainWindow", "Форма общетсва"))
        self.label_11.setText(_translate("MainWindow", "Должность руководителя"))
        self.label_10.setText(_translate("MainWindow", "ФИО руководителя"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Организации"))
        self.label_16.setText(_translate("MainWindow", "ФИО"))
        self.label_19.setText(_translate("MainWindow", "Адрес"))
        self.label_20.setText(_translate("MainWindow", "Паспорт и другие документы"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Индивидуальные предприниматели и Физ. лица"))
        self.label_21.setText(_translate("MainWindow", "Электронная почта получателя"))
        self.label_15.setText(_translate("MainWindow", "Срок отсрочки оплаты"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), _translate("MainWindow", "Договоры"))
        self.label_23.setText(_translate("MainWindow", "Сумма задолженности для претензии"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), _translate("MainWindow", "Письма и претензии"))
        self.label_8.setText(_translate("MainWindow", "Дата документа"))
        self.label_7.setText(_translate("MainWindow", "Номер документа"))
        self.label_13.setText(_translate("MainWindow", "Тип документа"))
        self.label_22.setText(_translate("MainWindow", "Дополнительные сведения"))
        self.label_25.setText(_translate("MainWindow", "Название документа"))
        self.pushButton_cancel_record.setText(_translate("MainWindow", "Отменить запись"))
        self.checkBox_no_parser.setToolTip(_translate("MainWindow", "При нажатой галочке не надо подтверждать ввод ИНН через кнопку"))
        self.checkBox_no_parser.setText(_translate("MainWindow", "Записать без ввода ИНН"))
        self.label_9.setText(_translate("MainWindow", "* Запись в excel  производится в зависимости от активной вкладки"))
        self.checkBox_number.setToolTip(_translate("MainWindow", "При нажатой галочке можно изменить значения в настройках в разделе [Alphabit Code]"))
        self.checkBox_number.setText(_translate("MainWindow", "свои буквы для номера документов"))
        self.pushButton_open_excel.setText(_translate("MainWindow", "Открыть Excel"))
        self.label_17.setText(_translate("MainWindow", "<html><head/><body><p>Пожертвования (переводом на карту) : <span style=\" font-weight:600;\">4276 5000 1042 4123</span></p></body></html>"))
        self.label_24.setText(_translate("MainWindow", "Результат"))
        self.menu_excel.setTitle(_translate("MainWindow", "Основное"))
        self.menu_2.setTitle(_translate("MainWindow", "Инструкция / Справка / Настройки"))
        self.menu_3.setTitle(_translate("MainWindow", "Очистить записи"))
        self.menu_4.setTitle(_translate("MainWindow", "Обновления"))
        self.action123.setText(_translate("MainWindow", "123"))
        self.action_settings.setText(_translate("MainWindow", "Открыть настройки"))
        self.action_open_excel.setText(_translate("MainWindow", "Открыть текущий excel файл"))
        self.action_readme.setText(_translate("MainWindow", "Открыть инструкцию"))
        self.action_clear_default.setText(_translate("MainWindow", "По умолчанию"))
        self.action_clear_all.setText(_translate("MainWindow", "Очистить все поля"))
        self.action_clear_inn.setText(_translate("MainWindow", "Очистить сведения о контрагенте"))
        self.action_info_author.setText(_translate("MainWindow", "О программе и авторе"))
        self.actionTelegram.setText(_translate("MainWindow", "Telegram"))
        self.actionInstagram.setText(_translate("MainWindow", "Instagram"))
        self.actionPixelpravo_ru.setText(_translate("MainWindow", "Pixelpravo.ru"))
        self.action_text_for_letter.setText(_translate("MainWindow", "Текст для отправки письма"))
        self.actionYouTube.setText(_translate("MainWindow", "YouTube"))
