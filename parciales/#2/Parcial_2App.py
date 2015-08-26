#!/usr/bin/python
# -*- coding: utf-8 -*-
from  kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen
import csv

reader = csv.reader(open('data.csv', 'r'), delimiter=',')
datos = {}
def espanol_ing(dato):
	inge =""
	for row in reader:
		to_db = [unicode(row[0], "utf8"), unicode(row[1], "utf8")]
		datos[row[0]]=row[1]
	inge=" No Disponible Aproxm"
	for x in datos:
		# print(x)
		if dato.upper() in x:
			inge= datos[x]
			
	return inge
def ing_espanol(dato):
	espa =""
	for row in reader:
		to_db = [unicode(row[0], "utf8"), unicode(row[1], "utf8")]
		datos[row[0]]=row[1]
	espa=" No Disponible Aproxm"
	for x in datos:
		if dato.upper() in datos[x]:
			espa= x
			
	return espa

# print(espanol_ing("rana"))
# print(ing_espanol('EAGLE'))
class Traductor(Screen):
	esp = ObjectProperty()
	ing = ObjectProperty()
	# print(busquedad)
	def mostrar(self):	
		espan= self.esp.text
		ingles=self.ing.text
		print(espan+" 	 "+ingles)
		if espan != '' and  ingles == '':
			tranduc= espanol_ing(espan)
			print(tranduc)
			print("Espanol a Ingles")
			self.impresion_ing= tranduc
		elif ingles != '' and  espan == '':
			tranduc= ing_espanol(ingles)
			print(tranduc)			
			print("Ingles a Espanol")
			self.impresion_esp = tranduc
		else:
			print("NO DISPONIBLE DATOS NULOS ERROR")
class Parcial_2App(App):
	def build(self):
		return Traductor()
	


# if__name__ == "__main__":
# 	Parcial_2App().run()

if __name__ == '__main__':
	Parcial_2App().run()
