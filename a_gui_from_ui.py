# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(828, 675)
        font = QtGui.QFont()
        font.setStrikeOut(False)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit_INN_QT_INPUT = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_INN_QT_INPUT.setGeometry(QtCore.QRect(20, 70, 211, 31))
        self.lineEdit_INN_QT_INPUT.setObjectName("lineEdit_INN_QT_INPUT")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 50, 121, 20))
        self.label.setObjectName("label")
        self.pushButton_Record_to_Excel = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Record_to_Excel.setGeometry(QtCore.QRect(560, 520, 111, 21))
        self.pushButton_Record_to_Excel.setObjectName("pushButton_Record_to_Excel")
        self.pushButton_Parse = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Parse.setGeometry(QtCore.QRect(240, 70, 131, 31))
        self.pushButton_Parse.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_Parse.setObjectName("pushButton_Parse")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(310, 10, 201, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(580, 0, 231, 16))
        font = QtGui.QFont()
        font.setUnderline(True)
        self.label_4.setFont(font)
        self.label_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_4.setStyleSheet("color: blue;")
        self.label_4.setOpenExternalLinks(True)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(660, 20, 91, 16))
        self.label_5.setObjectName("label_5")
        self.comboBox_xslm_choice = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_xslm_choice.setGeometry(QtCore.QRect(70, 130, 191, 22))
        self.comboBox_xslm_choice.setObjectName("comboBox_xslm_choice")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(110, 110, 121, 16))
        self.label_6.setObjectName("label_6")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(550, 440, 141, 20))
        self.label_14.setObjectName("label_14")
        self.comboBox_docfate = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_docfate.setGeometry(QtCore.QRect(510, 470, 211, 31))
        self.comboBox_docfate.setEditable(True)
        self.comboBox_docfate.setObjectName("comboBox_docfate")
        self.comboBox_docfate.addItem("")
        self.comboBox_docfate.addItem("")
        self.comboBox_docfate.addItem("")
        self.comboBox_docfate.addItem("")
        self.lineEdit_result = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_result.setGeometry(QtCore.QRect(450, 570, 331, 20))
        self.lineEdit_result.setObjectName("lineEdit_result")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(550, 550, 121, 16))
        self.label_15.setObjectName("label_15")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(20, 180, 361, 421))
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
        self.lineEdit_ustav = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_ustav.setGeometry(QtCore.QRect(10, 350, 321, 31))
        self.lineEdit_ustav.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit_ustav.setAutoFillBackground(False)
        self.lineEdit_ustav.setObjectName("lineEdit_ustav")
        self.label_9 = QtWidgets.QLabel(self.tab)
        self.label_9.setGeometry(QtCore.QRect(110, 320, 141, 16))
        self.label_9.setObjectName("label_9")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.lineEdit_NAME_organization_2 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_NAME_organization_2.setGeometry(QtCore.QRect(20, 30, 321, 31))
        self.lineEdit_NAME_organization_2.setObjectName("lineEdit_NAME_organization_2")
        self.label_16 = QtWidgets.QLabel(self.tab_2)
        self.label_16.setGeometry(QtCore.QRect(150, 10, 41, 16))
        self.label_16.setObjectName("label_16")
        self.textEdit_adress_2 = QtWidgets.QTextEdit(self.tab_2)
        self.textEdit_adress_2.setGeometry(QtCore.QRect(20, 90, 321, 61))
        self.textEdit_adress_2.setObjectName("textEdit_adress_2")
        self.label_19 = QtWidgets.QLabel(self.tab_2)
        self.label_19.setGeometry(QtCore.QRect(160, 70, 47, 13))
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.tab_2)
        self.label_20.setGeometry(QtCore.QRect(160, 160, 47, 13))
        self.label_20.setObjectName("label_20")
        self.textEdit_pasport = QtWidgets.QTextEdit(self.tab_2)
        self.textEdit_pasport.setGeometry(QtCore.QRect(20, 180, 321, 61))
        self.textEdit_pasport.setObjectName("textEdit_pasport")
        self.tabWidget.addTab(self.tab_2, "")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget_2.setGeometry(QtCore.QRect(430, 250, 351, 191))
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.textEdit_bill = QtWidgets.QTextEdit(self.tab_3)
        self.textEdit_bill.setGeometry(QtCore.QRect(20, 30, 321, 71))
        self.textEdit_bill.setObjectName("textEdit_bill")
        self.label_17 = QtWidgets.QLabel(self.tab_3)
        self.label_17.setGeometry(QtCore.QRect(140, 10, 91, 16))
        self.label_17.setObjectName("label_17")
        self.label_21 = QtWidgets.QLabel(self.tab_3)
        self.label_21.setGeometry(QtCore.QRect(100, 110, 171, 20))
        self.label_21.setObjectName("label_21")
        self.lineEdit_number_email = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_number_email.setGeometry(QtCore.QRect(20, 130, 321, 20))
        self.lineEdit_number_email.setObjectName("lineEdit_number_email")
        self.tabWidget_2.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.lineEdit_date_2 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_date_2.setGeometry(QtCore.QRect(80, 30, 101, 20))
        self.lineEdit_date_2.setObjectName("lineEdit_date_2")
        self.label_23 = QtWidgets.QLabel(self.tab_4)
        self.label_23.setGeometry(QtCore.QRect(20, 10, 201, 16))
        self.label_23.setObjectName("label_23")
        self.tabWidget_2.addTab(self.tab_4, "")
        self.comboBox_type_doc = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_type_doc.setGeometry(QtCore.QRect(440, 120, 341, 31))
        self.comboBox_type_doc.setEditable(True)
        self.comboBox_type_doc.setObjectName("comboBox_type_doc")
        self.lineEdit_number_docs = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_number_docs.setGeometry(QtCore.QRect(540, 70, 81, 20))
        self.lineEdit_number_docs.setObjectName("lineEdit_number_docs")
        self.lineEdit_date = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_date.setGeometry(QtCore.QRect(442, 70, 81, 20))
        self.lineEdit_date.setObjectName("lineEdit_date")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(440, 50, 91, 20))
        self.label_8.setObjectName("label_8")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(540, 50, 91, 16))
        self.label_7.setObjectName("label_7")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(570, 100, 81, 16))
        self.label_13.setObjectName("label_13")
        self.label_22 = QtWidgets.QLabel(self.centralwidget)
        self.label_22.setGeometry(QtCore.QRect(540, 230, 141, 16))
        self.label_22.setObjectName("label_22")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(400, 40, 20, 561))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(300, 30, 211, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_24 = QtWidgets.QLabel(self.centralwidget)
        self.label_24.setGeometry(QtCore.QRect(680, 50, 81, 16))
        self.label_24.setObjectName("label_24")
        self.comboBox_letter_code = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_letter_code.setGeometry(QtCore.QRect(660, 70, 121, 22))
        self.comboBox_letter_code.setObjectName("comboBox_letter_code")
        self.label_25 = QtWidgets.QLabel(self.centralwidget)
        self.label_25.setGeometry(QtCore.QRect(570, 160, 111, 16))
        self.label_25.setObjectName("label_25")
        self.comboBox_name_doc = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_name_doc.setGeometry(QtCore.QRect(440, 180, 341, 31))
        self.comboBox_name_doc.setEditable(True)
        self.comboBox_name_doc.setObjectName("comboBox_name_doc")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 828, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_excel = QtWidgets.QMenu(self.menubar)
        self.menu_excel.setObjectName("menu_excel")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
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
        self.menu.addAction(self.action_settings)
        self.menu_excel.addAction(self.action_open_excel)
        self.menu_2.addAction(self.action_readme)
        self.menubar.addAction(self.menu_excel.menuAction())
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Укажите ИНН или ОГРН"))
        self.pushButton_Record_to_Excel.setText(_translate("MainWindow", "Запись в excel"))
        self.pushButton_Parse.setText(_translate("MainWindow", "Подтвердить ввод ИНН"))
        self.label_3.setText(_translate("MainWindow", "Реестр договоров и писем"))
        self.label_4.setText(_translate("MainWindow", "<a href=\"https://www.pixelpravo.ru\">© created by Nikolai Slesarenko, pixelpravo.ru</a>"))
        self.label_5.setText(_translate("MainWindow", "3221208@mail.ru"))
        self.label_6.setText(_translate("MainWindow", "Выбирите excel файл"))
        self.label_14.setText(_translate("MainWindow", "Что сделано с документом"))
        self.comboBox_docfate.setItemText(0, _translate("MainWindow", "Направлен по электронной почте"))
        self.comboBox_docfate.setItemText(1, _translate("MainWindow", "Получен скан"))
        self.comboBox_docfate.setItemText(2, _translate("MainWindow", "Передан нарочно"))
        self.comboBox_docfate.setItemText(3, _translate("MainWindow", "Оригинал получен"))
        self.label_15.setText(_translate("MainWindow", "Результат выплнения"))
        self.label_2.setText(_translate("MainWindow", "Название организации"))
        self.label_18.setText(_translate("MainWindow", "Адрес"))
        self.label_12.setText(_translate("MainWindow", "Форма общетсва"))
        self.label_11.setText(_translate("MainWindow", "Должность руководителя"))
        self.label_10.setText(_translate("MainWindow", "ФИО руководителя"))
        self.lineEdit_ustav.setText(_translate("MainWindow", "Устава"))
        self.label_9.setText(_translate("MainWindow", "Устав или доверенность"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Организации"))
        self.label_16.setText(_translate("MainWindow", "ФИО ИП"))
        self.label_19.setText(_translate("MainWindow", "Адрес"))
        self.label_20.setText(_translate("MainWindow", "Паспорт"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Индивидуальные предприниматели"))
        self.label_17.setText(_translate("MainWindow", "Реквизиты счета"))
        self.label_21.setText(_translate("MainWindow", "Электронная почта получателя"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), _translate("MainWindow", "Договоры"))
        self.label_23.setText(_translate("MainWindow", "Сумма задолженности для претензии"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), _translate("MainWindow", "Письма и претензии"))
        self.label_8.setText(_translate("MainWindow", "Дата документа"))
        self.label_7.setText(_translate("MainWindow", "Номер документа"))
        self.label_13.setText(_translate("MainWindow", "Тип документа"))
        self.label_22.setText(_translate("MainWindow", "Дополнительные сведения"))
        self.label_24.setToolTip(_translate("MainWindow", "Буквенный код своей организации из config.ini раздел [Letter code]"))
        self.label_24.setText(_translate("MainWindow", "Буквенный код"))
        self.label_25.setText(_translate("MainWindow", "Название документа"))
        self.menu.setTitle(_translate("MainWindow", "Настройки"))
        self.menu_excel.setTitle(_translate("MainWindow", "Открыть excel"))
        self.menu_2.setTitle(_translate("MainWindow", "Инструкция"))
        self.action123.setText(_translate("MainWindow", "123"))
        self.action_settings.setText(_translate("MainWindow", "Открыть настройки"))
        self.action_open_excel.setText(_translate("MainWindow", "Открыть excel"))
        self.action_readme.setText(_translate("MainWindow", "Открыть инструкцию"))
