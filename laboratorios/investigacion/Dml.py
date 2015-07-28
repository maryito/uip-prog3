# -*- coding: utf-8 *-*
'''DML en mysql
	Desarrollado por Maryon Torres
'''
import mysql.connector
from mysql.connector import errorcode

class DML():
	"""DML"""
	def __init__(self,usuario='root',password='best1995', host='localhost',nom_bd='usuario_bd'):
		'''inicializacion con parametros de configuracion BD'''
		self.usuario = usuario
		self.password= password 
		self.host= host
		self.nom_bd= nom_bd
		self.CrearConexion()

	def CrearConexion(self):
		''' Creacion de una conexion '''
		print("\n\t --CONECTANDONOS A LA BD MySQL-\n")
		configuracion={"user":self.usuario,
						"password": self.password,
						"host":self.host,
						"database":self.nom_bd}
		try:
			self.bd=mysql.connector.connect(**configuracion)
			self.cursor = self.bd.cursor()

			estado=("\n!!!Conexion Exitosa!!!")
		except mysql.connector.Error as err:
			estado=("\n!!!Error En la Conexion!!!",err)
		return print(estado)
	def Mostrar(self ):
		'''consulta Bd SELECT'''
		print("\n\t --CONSULTANDO EN LA BD--\n")
		consulta = " SELECT * FROM test"
		self.cursor.execute(consulta)
		#fetchall Obtengo todos los valores Bd
		try:
			self.resultados = self.cursor.fetchall()
			if self.resultados  == None:
		   		estado= ("\n!!!Base De Datos vacia !!!")
			else:
				for registro in self.resultados:
					cedula=registro[0]
					nombre=registro[1]
					edad=registro[2]
					#convercion de formato byte array  a string 
					print("Nombre: %s Cedula: %s  Edad: %s "%(str(cedula,encoding='UTF-8'),str(nombre,encoding='UTF-8'),edad))
					
					estado=("\n!!!Consulta Exitosa!!!")
		except mysql.connector.Error as err:
			estado=("\n!!!Erro: No se pudo obtener los datos!!!",err)
			return print(estado)
	def Insertar(self):
		'''Insertar datos en la BD INSERT'''
		print("\n\t --AGREGANDO DATOS A LA BD--\n")
		try:
			cedula =input("Ingrese su Cedula:")
			nombre =input("Ingrese su nombre:")
			edad =int(input("Ingrese su edad:"))
			Insertar = ("INSERT INTO test (nombre, cedula, edad) VALUES ('%s','%s','%i')"%(nombre,cedula,edad))
			self.cursor.execute(Insertar)
			self.bd.commit()

			estado=("\n!!!Datos Insertar Exitosamente!!!")
		except mysql.connector.Error as err:
			estado=("\n!!!Erro al Insertar Datos!!!",err)
		return print(estado)
	def Actualizar(self):
		'''Actualizar datos en la BD UPDATE'''
		print("\n\t --ACTUALIZANDO LA BD--\n")
		try:
			cedula =input("Ingrese su Cedula Actual:")
			nueva_cedula=input("Ingrese su La Nueva Cedula:")
			consulta_actualizar = ("SELECT * FROM test WHERE cedula LIKE '%s'"%(cedula))
			status=self.verificacion(consulta_actualizar)
			if status == None:
				estado= ("\n!!!Dato No Encontrado en la BD!!!")
			else:
				actualizar=("UPDATE test SET cedula='%s' WHERE cedula='%s' "%(nueva_cedula,cedula))
				self.cursor.execute(actualizar)
				self.bd.commit()

				estado=("\n!!!Datos Actulizados Exitosamente!!!")
		except mysql.connector.Error as err:
			estado=("\n!!!Erro al Actualizar Datos!!!",err)
		return print(estado)
	def Eliminar(self):
		'''Eliminar registros en la BD DELETE'''
		print("\n\t --ELIMINANDO DATOS EN LA BD--\n")
		try:
			criterio = input("Ingrese nombre que desea eliminar: ")
			# hacemos una consulta para saber si el dato ingresado esta en la tabla
			consulta_eliminar = ("SELECT * FROM test WHERE nombre LIKE '%s'"%(criterio))
			status=self.verificacion(consulta_eliminar)
			if status == None:
			   	estado= ("\n!!!Dato No Encontrado en la BD!!!")
			else:			
				self.cursor = self.bd.cursor()
				criterio_consulta = ("DELETE FROM test WHERE nombre = '%s'" % (criterio ))
				self.cursor.execute(criterio_consulta)
				self.bd.commit()

				estado=("\n!!!Datos Eliminado Exitosamente!!!")
		except mysql.connector.Error as err:
			estado=("\n!!!Error al Eliminar Datos !!!",err)
		return print(estado)
	
	def verificacion(self,consulta):
		self.cursor = self.bd.cursor()
		self.cursor.execute(consulta)
		status = self.cursor.fetchone()
		return(status)
	def Cerrar_Conexion(self):
		self.cursor.close()
		self.bd.close()
		print("\n!!!Conexion Cerradas!!!\n".center(90, "*"))