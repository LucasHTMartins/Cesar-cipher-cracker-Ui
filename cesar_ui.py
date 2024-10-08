from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(896, 681)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.user_input = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.user_input.setGeometry(QtCore.QRect(20, 80, 311, 351))
        self.user_input.setObjectName("user_input")
        self.user_input_label = QtWidgets.QLabel(self.centralwidget)
        self.user_input_label.setGeometry(QtCore.QRect(110, 40, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.user_input_label.setFont(font)
        self.user_input_label.setAlignment(QtCore.Qt.AlignCenter)
        self.user_input_label.setObjectName("user_input_label")

        self.program_output = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.program_output.setGeometry(QtCore.QRect(560, 80, 311, 351))
        self.program_output.setObjectName("program_output")

        self.program_output_label = QtWidgets.QLabel(self.centralwidget)
        self.program_output_label.setGeometry(QtCore.QRect(630, 40, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.program_output_label.setFont(font)
        self.program_output_label.setAlignment(QtCore.Qt.AlignCenter)
        self.program_output_label.setObjectName("program_output_label")

        self.key_select_spin = QtWidgets.QSpinBox(self.centralwidget)
        self.key_select_spin.setGeometry(QtCore.QRect(420, 310, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.key_select_spin.setFont(font)
        self.key_select_spin.setObjectName("key_select_spin")
        self.key_select_spin.setMaximum(26)
        self.key_select_spin.setMinimum(0)

        self.run_button = QtWidgets.QPushButton(self.centralwidget)
        self.run_button.setGeometry(QtCore.QRect(390, 90, 111, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.run_button.setFont(font)
        self.run_button.setObjectName("run_button")
        self.select_key_label = QtWidgets.QLabel(self.centralwidget)
        self.select_key_label.setGeometry(QtCore.QRect(370, 270, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.select_key_label.setFont(font)
        self.select_key_label.setAlignment(QtCore.Qt.AlignCenter)
        self.select_key_label.setObjectName("select_key_label")
        self.Ke_selection_box = QtWidgets.QGroupBox(self.centralwidget)
        self.Ke_selection_box.setGeometry(QtCore.QRect(370, 190, 161, 211))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Ke_selection_box.setFont(font)
        self.Ke_selection_box.setObjectName("Ke_selection_box")



        self.current_key_label = QtWidgets.QLabel(self.Ke_selection_box)
        self.current_key_label.setGeometry(QtCore.QRect(0, 180, 161, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.current_key_label.setFont(font)
        self.current_key_label.setAlignment(QtCore.Qt.AlignCenter)
        self.current_key_label.setObjectName("current_key_label")
        self.rand_key_button = QtWidgets.QPushButton(self.Ke_selection_box)
        self.rand_key_button.setGeometry(QtCore.QRect(20, 30, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.rand_key_button.setFont(font)
        self.rand_key_button.setObjectName("rand_key_button")
        self.mode_box = QtWidgets.QGroupBox(self.centralwidget)
        self.mode_box.setGeometry(QtCore.QRect(440, 470, 421, 121))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.mode_box.setFont(font)
        self.mode_box.setObjectName("mode_box")
        self.awesome_radio = QtWidgets.QRadioButton(self.mode_box)
        self.awesome_radio.setGeometry(QtCore.QRect(10, 70, 151, 17))
        self.awesome_radio.setObjectName("awesome_radio")
        self.normal_radio = QtWidgets.QRadioButton(self.mode_box)
        self.normal_radio.setGeometry(QtCore.QRect(10, 40, 141, 17))
        self.normal_radio.setObjectName("normal_radio")
        self.awesome_explain_label = QtWidgets.QLabel(self.mode_box)
        self.awesome_explain_label.setGeometry(QtCore.QRect(180, 20, 231, 91))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.awesome_explain_label.setFont(font)
        self.awesome_explain_label.setAlignment(QtCore.Qt.AlignCenter)
        self.awesome_explain_label.setWordWrap(True)
        self.awesome_explain_label.setObjectName("awesome_explain_label")
        self.explanation_box = QtWidgets.QGroupBox(self.centralwidget)
        self.explanation_box.setGeometry(QtCore.QRect(30, 460, 201, 161))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.explanation_box.setFont(font)
        self.explanation_box.setAlignment(QtCore.Qt.AlignCenter)
        self.explanation_box.setObjectName("explanation_box")
        self.how_works_button = QtWidgets.QPushButton(self.explanation_box)
        self.how_works_button.setGeometry(QtCore.QRect(20, 100, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.how_works_button.setFont(font)
        self.how_works_button.setObjectName("how_works_button")
        self.what_is_button = QtWidgets.QPushButton(self.explanation_box)
        self.what_is_button.setGeometry(QtCore.QRect(30, 40, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.what_is_button.setFont(font)
        self.what_is_button.setObjectName("what_is_button")
        self.title_label = QtWidgets.QLabel(self.centralwidget)
        self.title_label.setGeometry(QtCore.QRect(350, 10, 201, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.title_label.setFont(font)
        self.title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.title_label.setObjectName("title_label")
        self.language_box = QtWidgets.QGroupBox(self.centralwidget)
        self.language_box.setGeometry(QtCore.QRect(270, 460, 131, 141))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.language_box.setFont(font)
        self.language_box.setAlignment(QtCore.Qt.AlignCenter)
        self.language_box.setObjectName("language_box")
        self.english_radio = QtWidgets.QRadioButton(self.language_box)
        self.english_radio.setGeometry(QtCore.QRect(10, 40, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.english_radio.setFont(font)
        self.english_radio.setObjectName("english_radio")
        self.portuguese_radio = QtWidgets.QRadioButton(self.language_box)
        self.portuguese_radio.setGeometry(QtCore.QRect(10, 70, 121, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setStrikeOut(True)
        self.portuguese_radio.setFont(font)
        self.portuguese_radio.setObjectName("portuguese_radio")
        self.spanish_radio = QtWidgets.QRadioButton(self.language_box)
        self.spanish_radio.setGeometry(QtCore.QRect(10, 100, 121, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setStrikeOut(True)
        self.spanish_radio.setFont(font)
        self.spanish_radio.setObjectName("spanish_radio")
        self.explanation_box.raise_()
        self.Ke_selection_box.raise_()
        self.mode_box.raise_()
        self.user_input.raise_()
        self.user_input_label.raise_()
        self.program_output.raise_()
        self.program_output_label.raise_()
        self.key_select_spin.raise_()
        self.run_button.raise_()
        self.select_key_label.raise_()
        self.title_label.raise_()
        self.language_box.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 896, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.user_input_label.setText(_translate("MainWindow", "Text Input"))
        self.program_output_label.setText(_translate("MainWindow", "Text Output"))
        self.run_button.setText(_translate("MainWindow", "Run\n"
"---->"))
        self.select_key_label.setText(_translate("MainWindow", "Or Select Key"))
        self.Ke_selection_box.setTitle(_translate("MainWindow", "Key selection"))
        self.current_key_label.setText(_translate("MainWindow", "Current Key: 0"))
        self.rand_key_button.setText(_translate("MainWindow", "Random Key"))
        self.mode_box.setTitle(_translate("MainWindow", "Mode Selection"))
        self.awesome_radio.setText(_translate("MainWindow", "Hyper Awesome mode"))
        self.normal_radio.setText(_translate("MainWindow", "Normal mode"))
        self.awesome_explain_label.setText(_translate("MainWindow", "Hyper Awesome Mode \n"
" While enabled, this program will analyze any encrypted text and come up with the most likely key and solution. The longer the text the more accurate the assesment is."))
        self.explanation_box.setTitle(_translate("MainWindow", "Why and How?"))
        self.how_works_button.setText(_translate("MainWindow", "How does this program work"))
        self.what_is_button.setText(_translate("MainWindow", "What is a Cesar Cipher"))
        self.title_label.setText(_translate("MainWindow", "Cesar Cipher"))
        self.language_box.setTitle(_translate("MainWindow", "Language Selection"))
        self.english_radio.setText(_translate("MainWindow", "English"))
        self.portuguese_radio.setText(_translate("MainWindow", "Portuguese"))
        self.spanish_radio.setText(_translate("MainWindow", "Spanish"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
