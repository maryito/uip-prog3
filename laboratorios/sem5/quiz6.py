directorio ={}
nombre =""
numero=0
opc =0
while(opc  != 5):	
	print("\n\t --MENU--\n\n\t 1- Imprimir \n\t 2- Agregar\n\t 3- Quitar \n\t 4- Buscar \n\t 5- Salir")
	opc = int (input("\t--> "))	
	
	if(opc == 1):
		print("\n\t --IMPRIMIR--\n")			
		
		if(len(directorio)>0):
		
			for clave,valor in directorio.items():
				print("\n\t Nombre: ", clave," Numero de Telefono: ", valor)
		else:
			print("\tDirectorio Vacio...\a")
	elif(opc ==2):
		print("\n\t --AGREGAR--\n")
		
		nombre= input(" Ingrese el Nombre: ")
		numero= int (input(" Ingrese el Numero de Telefono: "))		
		directorio[nombre]=numero
		
	elif(opc ==3):
		print("\n\t --QUITAR--\n")
		numero= int (input(" Ingrese el Numero de Telefono a eliminar: "))
		
		for clave,valor in directorio.items():#con la funcion items encuentro los valores del diccionario
			if(valor == numero):
				nombre = clave
		del directorio[nombre]		
		
	elif(opc ==4):
		print("\n\t --BUSCAR--\n")	
		nombre= input(" Ingrese el Nombre a Buscar: ")
		
		if(nombre in directorio):
			print("\n RESULTADO DE LA BUSQUEDA:\n\t Nombre: ", nombre," Numero de Telefono: \a", directorio[nombre])
		else:
			print("\n\tNombre no Existe En el Directorio...\a")
	elif(opc ==5):
		#print("\n\t --SALIR --\n")		
		opc = 5
	else:
		print("opcion no encontrada... \a")
else:
		print("se termino\a\a\a")