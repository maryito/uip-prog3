datos={}
cifrado=""# almacenara codigo cifrado
descifrado=""# almacenara codigo Descifrado
opc =0
while(opc  != 4):	# control del menu y opciones 
	print("\n\t --MENU--\n\n\t 1- Intoducir texto \n\t 2- Cifrarlo\n\t 3- Descifrarlo \n\t 4- Imprimirlo") # menu de las opciones 
	opc = int (input("\t--> "))		
	temp=""
	if(opc == 1):  # opcion para introducir texto 
		print("\n\t --INTRODUCIR TEXTO--\n")	
		texto = input("Ingrese el texto a cifrar: ")	# asigancion por teclado del texto 
		#datos[texto]="" # asignacion del la clave al diccionario
	elif(opc ==2):# opcion de cifrar 
		print("\n\t --CIFRARDO--\n")
		for x in texto: # recorrido del texto caracter por caracter
			dig =ord(x)+1  # convercion del caracter  a numero 
			temp += chr(dig) # convercio del numero a una cadena 
			cifrado = temp  # asignacion  del texto cifrado 
		print("\n CIFRADO CON EXITO :)")

	elif(opc ==3):
		print("\n\t --DESCIFRADO--\n")# opcion de descifrar 
		for c in cifrado:# recorrido del texto cifrado  caracter por caracter
			dig =ord(c)-1
			temp += chr(dig)	# convercio del numero cifrado a una cadena y asi obteniendo el texto cifrado 
			descifrado = temp# asignacion  del texto descifrado 
		print("\n DESCIFRADO CON EXITO :)")

	elif(opc ==4):
		print("\n\t --IMPRIMIR--\n") # opcion impresion 		
		print("Texto--> ",texto,"\nCifrado--> ", cifrado,"\nDescifrado--> ", descifrado)# impresion del texto, cifrado y descifrado 
		#print(datos) # impresion del  diccionario
	#datos[texto]="Texto Cifrado: "+cifrado+"Texto Descifrado: "+descifrado  # manejado con diccionario
else:
		print("\n\n\tFIN DEL PARCIAL #1 \n\t:) :) :)") # Fin del programa