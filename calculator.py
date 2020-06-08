# *-Coding:utf-8
from collections import deque

from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog,QLineEdit
from PyQt5 import QtGui 
from PyQt5 import QtCore
import math
import sys

from calco_ui import *


liste_chiffres = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
liste_chiffres_float = [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]
liste_operateurs = { \
					"+" : (1, "gauche"), "-" : (1, "gauche"), \
					"x" : (2, "gauche"), "/" : (2, "gauche"), \
					"^" : (3, "droite"), "√" : (3, "droite")
					}


class Calculatrice(QMainWindow):


	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.liste_chiffres = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
		self.liste_chiffres_float = [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]
		self.liste_operateurs = { 
									"+" : (1, "gauche", lambda a,b: a + b ),
									"-" : (1, "gauche", lambda a,b: a - b),
									"x" : (2, "gauche", lambda a,b: a * b), 
									"/" : (2, "gauche", lambda a,b: a / b), 
									"^" : (3, "droite", lambda a,b: a ** b),
									"√" : (3, "droite", lambda a : math.sqrt(a) ),
								}
		self.fonctions = {
							"abs" : (3, "droite", lambda a: math.fabs(a)), 
							"cos" : (3, "droite", lambda a: math.cos(a)), 
							"cos⁻¹" : (3, "droite", lambda a : math.acos(a)),
							"ln" : (3, "droite" , lambda a : math.log(a)),
							"log" : (3, "droite" , lambda a : math.log10(a)),
							"pgcd" : (3, "droite" , lambda a, b : math.gcd(a,b)), 
							"ppcm" : (3, "droite", lambda a, b : int(a * b / math.gcd(a,b))),
							"sin" : (3, "droite", lambda a: math.sin(a)), 
							"sin⁻¹" : (3, "droite", lambda a : math.asin(a)),
							"tan" : (3, "droite", lambda a : math.tan(a)), 
							"tan⁻¹" : (3, "droite", lambda a: math.atan(a)),
						}
		self.ans = 0
		self.ui.bouton0.clicked.connect(lambda : self.test("0"))
		self.ui.bouton1.clicked.connect(lambda : self.test("1"))
		self.ui.bouton2.clicked.connect(lambda : self.test("2"))
		self.ui.bouton3.clicked.connect(lambda : self.test("3"))
		self.ui.bouton4.clicked.connect(lambda : self.test("4"))
		self.ui.bouton5.clicked.connect(lambda : self.test("5"))
		self.ui.bouton6.clicked.connect(lambda : self.test("6"))
		self.ui.bouton7.clicked.connect(lambda : self.test("7"))
		self.ui.bouton8.clicked.connect(lambda : self.test("8"))
		self.ui.bouton9.clicked.connect(lambda : self.test("9"))
		self.ui.bouton_addition.clicked.connect(lambda : self.verif_operator("+"))
		self.ui.bouton_moins.clicked.connect(lambda : self.verif_operator("-"))
		self.ui.bouton_multiplication.clicked.connect(lambda : self.verif_operator("x"))
		self.ui.bouton_division.clicked.connect(lambda : self.verif_operator("/"))
		self.ui.bouton_delete.clicked.connect(lambda : self.del_button())
		self.ui.bouton_virgule.clicked.connect(lambda : self.insert_virgule())
		self.ui.bouton_egal.clicked.connect(lambda: self.gestion_egal() )
		self.ui.bouton_ans.clicked.connect(lambda : self.gestion_ans() )
		self.ui.bouton_parenthese_ouvrante.clicked.connect(lambda : self.parenthese_bouton("("))
		self.ui.bouton_parenthese_fermante.clicked.connect(lambda : self.parenthese_bouton(")"))
		#Bouton function 
		self.ui.bouton_racin_carre.clicked.connect(lambda : self.racine_carre())
		self.ui.bouton_puissance.clicked.connect(lambda : self.verif_operator("^"))
		self.ui.bouton_puissance10.clicked.connect(lambda : self.petite_verif_pour_puissance10())
		self.ui.comboBox_fonctions.activated.connect(lambda : self.gestion_fonction(self.ui.comboBox_fonctions.currentIndex()))


	def gestion_fonction(self, index):
		if index != 0:
			self.ui.label_operation.setText(self.ui.label_operation.text() + self.ui.comboBox_fonctions.currentText()[:-2])


	def gestion_fonction_1(self, event):
		if self.ui.comboBox_fonctions.currentIndex() != 0:
			self.ui.label_operation.setText(self.ui.label_operation.text() + self.ui.comboBox_fonctions.currentText()[:-2])


	def gestion_egal(self):
		self.ans = self.set_label_calcul(self.ui.label_operation.text())


	def gestion_ans (self):
		self.ui.label_operation.setText(self.ui.label_operation.text() + "ans")

	
	def racine_carre(self):
		'''Ajoute un symbole racine carré'''
		op ="√" 
		taille = len(self.ui.label_operation.text())
		if taille == 1:
			if self.ui.label_operation.text() == "x" and self.ui.label_operation.text() == "/":
				self.ui.label_operation.setText("")
			else:
				self.ui.label_operation.setText(self.ui.label_operation.text() + op)
		else :
			self.ui.label_operation.setText(self.ui.label_operation.text() + op)



	def petite_verif_pour_puissance10(self):
		if len(self.ui.label_operation.text()) > 0:
			if self.ui.label_operation.text()[-1] in self.liste_chiffres :
				self.verif_operator("x10^")


	def parenthese_bouton(self, parenthese):
		self.ui.label_operation.setText(self.ui.label_operation.text() + parenthese)


	def del_button(self):
		''' bouton supprime un caractère '''
		if len(self.ui.label_operation.text()) > 0:
			if self.ui.label_operation.text()[-1]  in self.liste_chiffres + [k for k in self.liste_operateurs] + ["(", ")"]:
				self.ui.label_operation.setText(self.ui.label_operation.text()[:-1])
			else :
				val_label_operation = self.ui.label_operation.text()

				while len(val_label_operation) > 0:
					if val_label_operation[-1] not in self.liste_chiffres + [k for k in self.liste_operateurs] + ["(", ")"] :
						val_label_operation = val_label_operation[:-1]
					else :
						break
				self.ui.label_operation.setText(val_label_operation)
			if len(self.ui.label_operation.text()) > 0:
				if self.ui.label_operation.text()[-1]  in self.liste_chiffres + [k for k in self.liste_operateurs] + ["(", ")"]:
					self.set_label_calcul(self.ui.label_operation.text())
			else :
				self.ui.label_resultat.setText("")
		else:
			self.ui.label_resultat.setText("")
		

	def test(self, num):
		'''Ajoute un chiffre à l'écran'''
		if len(self.ui.label_operation.text()) == 1 and self.ui.label_operation.text() == "0":
			self.ui.label_operation.setText(num)
		else:
			self.ui.label_operation.setText(self.ui.label_operation.text() + num)
		self.set_label_calcul(self.ui.label_operation.text())


	def verif_operator(self,op):
		'''Ajoute un symbole d'opération''' 
		taille = len(self.ui.label_operation.text())
		if taille  > 0: 
			if self.ui.label_operation.text()[-1] in [k for k in self.liste_operateurs] :
				self.ui.label_operation.setText(self.ui.label_operation.text()[:-1] + op)
			else:
				self.ui.label_operation.setText(self.ui.label_operation.text() + op)
		elif taille == 0:
			if op == "-":
				self.ui.label_operation.setText(self.ui.label_operation.text() + op)
		elif taille == 1:
			if self.ui.label_operation.text()[-1] == "-" and op == "+":
				self.ui.label_operation.setText("")


	def insert_virgule(self):

		nombre_avant_virgule = False
		position = 0
		ecran = self.ui.label_operation.text()

		if len(ecran ) == 0 :
			self.ui.label_operation.setText("0.")
		else :
			virgule_present = False
			op_present = False
			for i in range(len(ecran)):
				if ecran[-i] == '.':
					virgule_present = True
				if ecran[-i] in [k for k in self.liste_operateurs] + ["(", ")"]:
					op_present = True
					break

			if (not virgule_present and not op_present) :
				self.ui.label_operation.setText(self.ui.label_operation.text() + ".")
			elif (not virgule_present and op_present):
				if self.ui.label_operation.text()[-1] in self.liste_chiffres :
					self.ui.label_operation.setText(self.ui.label_operation.text() + ".")


	#Shunting Yard Algorithm
	def transform_post_fixe(self,items):
		operateurs = []
		liste_final = deque()
		liste_total_operateurs = dict(self.liste_operateurs ,** self.fonctions)
		for element in items:
			if element in liste_total_operateurs:
				if not operateurs :
					operateurs.append(element)
				elif operateurs[-1] == "(" :
					operateurs.append(element)
				else:
					while operateurs :
						a = (operateurs[-1] in liste_total_operateurs)
						if a : 
							if (liste_total_operateurs[element][0] < liste_total_operateurs[operateurs[-1]][0] and liste_total_operateurs[element][1] == liste_total_operateurs[operateurs[-1]][1]) or \
								  (liste_total_operateurs[element][0] <= liste_total_operateurs[operateurs[-1]][0] and liste_total_operateurs[element][1] != liste_total_operateurs[operateurs[-1]][1]) :
								  liste_final.append(operateurs.pop())
							else :
								break
						else:
							break
					operateurs.append(element)
			#Si c'est une parenthèse ouvrante on l'ajoute si c'est une parenthèse fermante on dépile les opérateurs jusqu'à la prochaine parenthèse ouvrante
			elif element in ["(", ")"] :
				if element == "(":
					operateurs.append(element)
				elif element == ")":
					while operateurs:
						if operateurs[-1] != "(":
							liste_final.append(operateurs.pop())
						else:
							operateurs.pop()
							break
			elif element == "ans":
				liste_final.append(self.ans)
			#Si c'est un nombre on l'ajoute sans faire d'histoire à la file
			else :
				liste_final.append(element)
		while operateurs :
			if operateurs[-1] not in ["(", ")"]:
				liste_final.append(operateurs.pop())
			else :
				operateurs.pop()
		return list(liste_final)


	def extraction_pour_calcul_post_fixe(self, chaine_caractere):
		
		if len(chaine_caractere) == 0:	
				return ""	
		else :
			uniquement_fait_op = True
			for i in chaine_caractere :

				if i not in  [k for k in self.liste_operateurs] + ["(" , ")"]: 	
					uniquement_fait_op = False;
					break
			if uniquement_fait_op:
				return ""

		if chaine_caractere[-1] in self.liste_operateurs:
			chaine_caractere = chaine_caractere[:-1]
		es_negatif = False
		#final est une liste qui contiendra l'opération post fixée
		final = []
		i = 0
		num = True
		#On parcourt l'expression que l'on veut transformer 
		while i  < len(chaine_caractere):
			# s'il s'agit d'une simple opération (+, -, /, *) on ajoute le caractère dans operateurs 
			if chaine_caractere[i] in self.liste_operateurs:
				if chaine_caractere[i] not in ["-" , "√"]:
					final.append(chaine_caractere[i])

				elif chaine_caractere[i] == "√":
					if i > 0 :
						if chaine_caractere[i - 1] in self.liste_chiffres :
							final.append("x")
					final.append(chaine_caractere[i])

				else :
					if i == 0  or (i > 0 and chaine_caractere[i - 1] == "(" ):
						final.append(0.0)
						es_negatif = True
					final.append(chaine_caractere[i])
				num = False
				i = i + 1
			#les s'il s'agit d'une parenthèse  
			elif chaine_caractere[i] in ["(", ")"]:
				if chaine_caractere[i] == "(":
					if chaine_caractere[i-1] in self.liste_chiffres and i > 0:
						final.append("x")
					final.append("(")
				else:
					final.append(chaine_caractere[i])
				num = False
				i = i + 1
			#Si c'est un nombre 
			elif chaine_caractere[i] in self.liste_chiffres:
				#le nombre peut avoir plusieurs chiffres d'où la présence de cette variable var qui nous aidera à rassembler ceux-ci
				val = ""
				while  i < len(chaine_caractere) and  (chaine_caractere[i] in self.liste_chiffres + ["."]) : 
					val = val + chaine_caractere[i]
					i = i + 1

				final.append(float(val))
				if es_negatif :
					es_negatif = False
				num = True
			elif chaine_caractere[i] == ",":
				i = i + 1
			#S'il s'agit d'un caractère implicitement une fonction
			else :
				if i > 0 :
					if chaine_caractere[i - 1] in self.liste_chiffres :
						final.append("x")
				op = ""
				while i < len(chaine_caractere):
					if chaine_caractere[i] in ["(", ")", ","] + [k for k in self.liste_operateurs] + self.liste_chiffres:
						break
					else :
						op = op + chaine_caractere[i]
					i = i + 1
				final.append(op) 
		return final


	def calcul_post_fixe(self, final):
			i = 0
			while i < len(final):
				if  final[i] in liste_operateurs:
					if final[i] == "√":
						if final[i - 1 ] >= 0 :
							final[i-1] = math.sqrt(final[i - 1])
							final.pop(i)
							i = 0
						else :
							return "Math error"
					else:	
						a = final[i-2]
						b = final[i-1]
						a = self.liste_operateurs[final[i]][2](a,b)
						b = i-2
						for j in range(3):
							final.pop(b)

						final.insert(b, a)
					i = 0
				elif final[i] in self.fonctions :
					if final[i] in ["ppcm", "pgcd"]:
						a = math.floor( final[i-1] )
						b = math.floor( final[i-2] )
						if a == int( final[i-1] ) and b == int( final[i-2] ) :
							a = self.liste_fonctions[final[i]][2](a,b)
							for j in range(3):
								final.pop(i-2)
							final.insert(i-2, a)
							i = 0
						else :
							return "Math error"
					else :
						final[i-1] = self.fonctions[ final[i] ][2](final[i-1])
						final.pop(i)
						i = 0
				else:
					i = i + 1

			if len(final) > 0:
				if len(final) > 1:
					return "Syntax error"
				else:
					return  final[0] 				

	def set_label_calcul(self, chaine):
		try:

			liste_charac = self.extraction_pour_calcul_post_fixe(self.ui.label_operation.text())
			liste_charac = self.transform_post_fixe(liste_charac)
			result = self.calcul_post_fixe(liste_charac)
			self.ui.label_resultat.setText( str(result))
			return result
		except ValueError :
			self.ui.label_resultat.setText("Math Error")
		except OverflowError :
			self.ui.label_resultat.setText("∞")
		except TypeError:
			self.ui.label_resultat.setText("Synthax erreur")
		except ZeroDivisionError :
			self.ui.label_resultat.setText("∞")




def main():
	app = QApplication(sys.argv)
	f = Calculatrice()
	f.show()
	sys.exit(app.exec())

	
if __name__ == "__main__":
	main()