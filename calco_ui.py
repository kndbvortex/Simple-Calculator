# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calco.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(688, 507)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../../Téléchargements/calculate-math.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(20, 43, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setMaximumSize(QtCore.QSize(450, 67))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.label_operation = QtWidgets.QLabel(self.splitter)
        self.label_operation.setMaximumSize(QtCore.QSize(450, 33))
        self.label_operation.setStyleSheet("background-color : white;\n"
"font: 25 18pt \"Exo\";\n"
"")
        self.label_operation.setText("")
        self.label_operation.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_operation.setObjectName("label_operation")
        self.label_resultat = QtWidgets.QLabel(self.splitter)
        self.label_resultat.setMaximumSize(QtCore.QSize(450, 33))
        self.label_resultat.setStyleSheet("background-color : white;\n"
"font: 25 18pt \"Exo\";\n"
"")
        self.label_resultat.setText("")
        self.label_resultat.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_resultat.setObjectName("label_resultat")
        self.verticalLayout_3.addWidget(self.splitter)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem2)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.splitter_3 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName("splitter_3")
        self.comboBox_fonctions = QtWidgets.QComboBox(self.splitter_3)
        self.comboBox_fonctions.setObjectName("comboBox_fonctions")
        self.comboBox_fonctions.addItem("")
        self.comboBox_fonctions.addItem("")
        self.comboBox_fonctions.addItem("")
        self.comboBox_fonctions.addItem("")
        self.comboBox_fonctions.addItem("")
        self.comboBox_fonctions.addItem("")
        self.comboBox_fonctions.addItem("")
        self.comboBox_fonctions.addItem("")
        self.comboBox_fonctions.addItem("")
        self.comboBox_fonctions.addItem("")
        self.comboBox_fonctions.addItem("")
        self.splitter_2 = QtWidgets.QSplitter(self.splitter_3)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.bouton_parenthese_ouvrante = QtWidgets.QPushButton(self.splitter_2)
        self.bouton_parenthese_ouvrante.setStyleSheet("font: 57 12pt \"KacstPen\";")
        self.bouton_parenthese_ouvrante.setObjectName("bouton_parenthese_ouvrante")
        self.bouton_parenthese_fermante = QtWidgets.QPushButton(self.splitter_2)
        self.bouton_parenthese_fermante.setStyleSheet("font: 57 12pt \"KacstPen\";")
        self.bouton_parenthese_fermante.setObjectName("bouton_parenthese_fermante")
        self.bouton_puissance = QtWidgets.QPushButton(self.splitter_2)
        self.bouton_puissance.setStyleSheet("font: 57 12pt \"KacstPen\";")
        self.bouton_puissance.setObjectName("bouton_puissance")
        self.bouton_racin_carre = QtWidgets.QPushButton(self.splitter_2)
        self.bouton_racin_carre.setStyleSheet("font: 57 12pt \"KacstPen\";")
        self.bouton_racin_carre.setObjectName("bouton_racin_carre")
        self.verticalLayout_2.addWidget(self.splitter_3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.bouton7 = QtWidgets.QPushButton(self.centralwidget)
        self.bouton7.setStyleSheet("font: 57 12pt \"KacstPen\";")
        self.bouton7.setObjectName("bouton7")
        self.horizontalLayout_4.addWidget(self.bouton7)
        self.bouton8 = QtWidgets.QPushButton(self.centralwidget)
        self.bouton8.setStyleSheet("font: 57 12pt \"KacstPen\";")
        self.bouton8.setObjectName("bouton8")
        self.horizontalLayout_4.addWidget(self.bouton8)
        self.bouton9 = QtWidgets.QPushButton(self.centralwidget)
        self.bouton9.setStyleSheet("font: 57 12pt \"KacstPen\";")
        self.bouton9.setObjectName("bouton9")
        self.horizontalLayout_4.addWidget(self.bouton9)
        self.bouton_delete = QtWidgets.QPushButton(self.centralwidget)
        self.bouton_delete.setStyleSheet("font: 57 12pt \"KacstPen\";")
        self.bouton_delete.setObjectName("bouton_delete")
        self.horizontalLayout_4.addWidget(self.bouton_delete)
        self.bouton_clear_all = QtWidgets.QPushButton(self.centralwidget)
        self.bouton_clear_all.setStyleSheet("font: 57 12pt \"KacstPen\";")
        self.bouton_clear_all.setObjectName("bouton_clear_all")
        self.horizontalLayout_4.addWidget(self.bouton_clear_all)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.bouton4 = QtWidgets.QPushButton(self.centralwidget)
        self.bouton4.setStyleSheet("font: 57 12pt \"KacstPen\";")
        self.bouton4.setObjectName("bouton4")
        self.horizontalLayout_3.addWidget(self.bouton4)
        self.bouton5 = QtWidgets.QPushButton(self.centralwidget)
        self.bouton5.setStyleSheet("font: 57 12pt \"KacstPen\";")
        self.bouton5.setObjectName("bouton5")
        self.horizontalLayout_3.addWidget(self.bouton5)
        self.bouton6 = QtWidgets.QPushButton(self.centralwidget)
        self.bouton6.setStyleSheet("font: 57 12pt \"KacstPen\";")
        self.bouton6.setObjectName("bouton6")
        self.horizontalLayout_3.addWidget(self.bouton6)
        self.bouton_multiplication = QtWidgets.QPushButton(self.centralwidget)
        self.bouton_multiplication.setStyleSheet("font: 57 12pt \"KacstPen\";")
        self.bouton_multiplication.setObjectName("bouton_multiplication")
        self.horizontalLayout_3.addWidget(self.bouton_multiplication)
        self.bouton_division = QtWidgets.QPushButton(self.centralwidget)
        self.bouton_division.setStyleSheet("font: 57 12pt \"KacstPen\";")
        self.bouton_division.setObjectName("bouton_division")
        self.horizontalLayout_3.addWidget(self.bouton_division)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.bouton1 = QtWidgets.QPushButton(self.centralwidget)
        self.bouton1.setStyleSheet("font: 57 12pt \"KacstPen\";")
        self.bouton1.setObjectName("bouton1")
        self.horizontalLayout_2.addWidget(self.bouton1)
        self.bouton2 = QtWidgets.QPushButton(self.centralwidget)
        self.bouton2.setStyleSheet("font: 57 12pt \"KacstPen\";")
        self.bouton2.setObjectName("bouton2")
        self.horizontalLayout_2.addWidget(self.bouton2)
        self.bouton3 = QtWidgets.QPushButton(self.centralwidget)
        self.bouton3.setStyleSheet("font: 57 12pt \"KacstPen\";")
        self.bouton3.setObjectName("bouton3")
        self.horizontalLayout_2.addWidget(self.bouton3)
        self.bouton_addition = QtWidgets.QPushButton(self.centralwidget)
        self.bouton_addition.setStyleSheet("font: 57 12pt \"KacstPen\";")
        self.bouton_addition.setObjectName("bouton_addition")
        self.horizontalLayout_2.addWidget(self.bouton_addition)
        self.bouton_moins = QtWidgets.QPushButton(self.centralwidget)
        self.bouton_moins.setStyleSheet("font: 57 12pt \"KacstPen\";")
        self.bouton_moins.setObjectName("bouton_moins")
        self.horizontalLayout_2.addWidget(self.bouton_moins)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.bouton0 = QtWidgets.QPushButton(self.centralwidget)
        self.bouton0.setStyleSheet("font: 57 12pt \"KacstPen\";")
        self.bouton0.setObjectName("bouton0")
        self.horizontalLayout.addWidget(self.bouton0)
        self.bouton_virgule = QtWidgets.QPushButton(self.centralwidget)
        self.bouton_virgule.setStyleSheet("font: 57 12pt \"KacstPen\";")
        self.bouton_virgule.setObjectName("bouton_virgule")
        self.horizontalLayout.addWidget(self.bouton_virgule)
        self.bouton_puissance10 = QtWidgets.QPushButton(self.centralwidget)
        self.bouton_puissance10.setStyleSheet("font: 57 12pt \"KacstPen\";")
        self.bouton_puissance10.setObjectName("bouton_puissance10")
        self.horizontalLayout.addWidget(self.bouton_puissance10)
        self.bouton_ans = QtWidgets.QPushButton(self.centralwidget)
        self.bouton_ans.setStyleSheet("font: 57 12pt \"KacstPen\";")
        self.bouton_ans.setObjectName("bouton_ans")
        self.horizontalLayout.addWidget(self.bouton_ans)
        self.bouton_egal = QtWidgets.QPushButton(self.centralwidget)
        self.bouton_egal.setStyleSheet("font: 57 12pt \"KacstPen\";")
        self.bouton_egal.setObjectName("bouton_egal")
        self.horizontalLayout.addWidget(self.bouton_egal)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.horizontalLayout_5.addLayout(self.verticalLayout_3)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        spacerItem4 = QtWidgets.QSpacerItem(20, 42, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 688, 30))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.bouton_clear_all.clicked.connect(self.label_operation.clear)
        self.bouton_clear_all.clicked.connect(self.label_resultat.clear)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Dk Calculator"))
        self.comboBox_fonctions.setToolTip(_translate("MainWindow", "<html><head/><body><p>Fonction spéciales</p></body></html>"))
        self.comboBox_fonctions.setItemText(0, _translate("MainWindow", "Fonctions"))
        self.comboBox_fonctions.setItemText(1, _translate("MainWindow", "abs(x)"))
        self.comboBox_fonctions.setItemText(2, _translate("MainWindow", "cos(x)"))
        self.comboBox_fonctions.setItemText(3, _translate("MainWindow", "cos⁻¹(x)"))
        self.comboBox_fonctions.setItemText(4, _translate("MainWindow", "ln(x)"))
        self.comboBox_fonctions.setItemText(5, _translate("MainWindow", "pgcd(x,y)"))
        self.comboBox_fonctions.setItemText(6, _translate("MainWindow", "ppmc(x,y)"))
        self.comboBox_fonctions.setItemText(7, _translate("MainWindow", "sin(x)"))
        self.comboBox_fonctions.setItemText(8, _translate("MainWindow", "sin⁻¹(x)"))
        self.comboBox_fonctions.setItemText(9, _translate("MainWindow", "tan(x)"))
        self.comboBox_fonctions.setItemText(10, _translate("MainWindow", "tan⁻¹(x)"))
        self.bouton_parenthese_ouvrante.setToolTip(_translate("MainWindow", "<html><head/><body><p>Début d\'un groupement</p></body></html>"))
        self.bouton_parenthese_ouvrante.setText(_translate("MainWindow", "("))
        self.bouton_parenthese_fermante.setToolTip(_translate("MainWindow", "<html><head/><body><p>Fin d\'un groupement</p></body></html>"))
        self.bouton_parenthese_fermante.setText(_translate("MainWindow", ")"))
        self.bouton_puissance.setToolTip(_translate("MainWindow", "<html><head/><body><p>Puissance (^)</p></body></html>"))
        self.bouton_puissance.setText(_translate("MainWindow", "^"))
        self.bouton_racin_carre.setToolTip(_translate("MainWindow", "<html><head/><body><p>Racine carrée</p></body></html>"))
        self.bouton_racin_carre.setText(_translate("MainWindow", "√"))
        self.bouton7.setText(_translate("MainWindow", "7"))
        self.bouton8.setText(_translate("MainWindow", "8"))
        self.bouton9.setText(_translate("MainWindow", "9"))
        self.bouton_delete.setToolTip(_translate("MainWindow", "<html><head/><body><p>Delete last character</p></body></html>"))
        self.bouton_delete.setText(_translate("MainWindow", "Del"))
        self.bouton_clear_all.setToolTip(_translate("MainWindow", "<html><head/><body><p>Clear text</p></body></html>"))
        self.bouton_clear_all.setText(_translate("MainWindow", "AC"))
        self.bouton4.setText(_translate("MainWindow", "4"))
        self.bouton5.setText(_translate("MainWindow", "5"))
        self.bouton6.setText(_translate("MainWindow", "6"))
        self.bouton_multiplication.setToolTip(_translate("MainWindow", "<html><head/><body><p>Multiplication (*)</p></body></html>"))
        self.bouton_multiplication.setText(_translate("MainWindow", "x"))
        self.bouton_division.setToolTip(_translate("MainWindow", "<html><head/><body><p>Division (/)</p></body></html>"))
        self.bouton_division.setText(_translate("MainWindow", "/"))
        self.bouton1.setText(_translate("MainWindow", "1"))
        self.bouton2.setText(_translate("MainWindow", "2"))
        self.bouton3.setText(_translate("MainWindow", "3"))
        self.bouton_addition.setToolTip(_translate("MainWindow", "<html><head/><body><p>Addition (+)</p></body></html>"))
        self.bouton_addition.setText(_translate("MainWindow", "+"))
        self.bouton_moins.setToolTip(_translate("MainWindow", "<html><head/><body><p>Soustraction (+)</p></body></html>"))
        self.bouton_moins.setText(_translate("MainWindow", "-"))
        self.bouton0.setText(_translate("MainWindow", "0"))
        self.bouton_virgule.setText(_translate("MainWindow", ","))
        self.bouton_puissance10.setToolTip(_translate("MainWindow", "<html><head/><body><p>Exposant scientifique</p></body></html>"))
        self.bouton_puissance10.setText(_translate("MainWindow", "EXP"))
        self.bouton_ans.setText(_translate("MainWindow", "Ans"))
        self.bouton_egal.setText(_translate("MainWindow", "="))
