# -*- coding: utf-8 -*-

import sys, ui
import PyQt5
import math
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class MainDialog(QDialog, ui.Ui_Form):
    def __init__(self):
        QDialog.__init__(self, None)
        self.setupUi(self)

        self.pushButton1.clicked.connect(lambda state, button=self.pushButton1: self.NumClicked(state, button))
        self.pushButton2.clicked.connect(lambda state, button=self.pushButton2: self.NumClicked(state, button))
        self.pushButton3.clicked.connect(lambda state, button=self.pushButton3: self.NumClicked(state, button))
        self.pushButton4.clicked.connect(lambda state, button=self.pushButton4: self.NumClicked(state, button))
        self.pushButton5.clicked.connect(lambda state, button=self.pushButton5: self.NumClicked(state, button))
        self.pushButton6.clicked.connect(lambda state, button=self.pushButton6: self.NumClicked(state, button))
        self.pushButton7.clicked.connect(lambda state, button=self.pushButton7: self.NumClicked(state, button))
        self.pushButton8.clicked.connect(lambda state, button=self.pushButton8: self.NumClicked(state, button))
        self.pushButton9.clicked.connect(lambda state, button=self.pushButton9: self.NumClicked(state, button))
        self.pushButton0.clicked.connect(lambda state, button=self.pushButton0: self.NumClicked(state, button))

        self.pushButton_sign1.clicked.connect(lambda state, button=self.pushButton_sign1: self.NumClicked(state, button))
        self.pushButton_sign2.clicked.connect(lambda state, button=self.pushButton_sign2: self.NumClicked(state, button))
        self.pushButton_sign3.clicked.connect(lambda state, button=self.pushButton_sign3: self.NumClicked(state, button))
        self.pushButton_sign4.clicked.connect(lambda state, button=self.pushButton_sign4: self.NumClicked(state, button))

        self.pushButton_per.clicked.connect(lambda state, button=self.pushButton_per: self.NumClicked(state, button))
        self.pushButton_dot.clicked.connect(lambda state, button=self.pushButton_dot: self.NumClicked(state, button))

        self.pushButton_sign5.clicked.connect(self.Makeresult)
        self.pushButton_Clear.clicked.connect(self.reset)

    def NumClicked(self, state, button):
        if button == self.pushButton_per:
            now_num_text = '*0.01'
        else:
            now_num_text = button.text()

        exist_line_text = self.lineEdit_first.text()

        self.lineEdit_first.setText(exist_line_text + now_num_text)

    def Makeresult(self):
        try:
            result = eval(self.lineEdit_first.text())
            self.lineEdit_second.setText(str(result))
        except:
            pass

    def reset(self):
        self.lineEdit_first.clear()
        self.lineEdit_second.setText('0')

app = QApplication(sys.argv)
main_dialog = MainDialog()
main_dialog.show()
app.exec_()