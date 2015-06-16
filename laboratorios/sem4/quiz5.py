import os  # libreria para importa la funcion de limpiar pantalla

sup_mercado = ["pollo","pan","queso","soda","arroz"] # lista de super mercado por defecto
mer_default= sup_mercado[0:5] # super mercado por defecto
opc = "s"

while(opc  != "n"):	
	os.system("cls")# funcion para limpiar pantalla
	print("\n\t --MENU--\n\n\t 1- agregar\n\t 2- eliminar\n\t 3- mostrar \n")
	opc = int (input("\t--> "))	
	if(opc == 1):
		print("\n\t --INGRESO--\n")
		sup_mercado.append(input("\n Ingrese el Nuevo Elemento para Su Lista de Supermercado: "))		
	elif(opc ==2):
		print("\n\t --ELIMINAR--\n")
		print("\nSu Lista de Supermercado contiene : "+str( len(sup_mercado)),"Elementos")
		del sup_mercado[int (input("\n Ingrese el indice del Elemento que Desea Eliminar de Su Lista de Supermercado: "))]
	elif(opc ==3):
		print("\n\t --VISUALIZACION--\n")
		print("Elementos de Su Lista de Supermercado por Defecto: \n", str( mer_default))
		print("\nElementos  de Su Lista de Supermercado Agregados: ")
		mer_add = sup_mercado[5:len(sup_mercado)]
		print(mer_add)
		print("\nLista de Supermercado Actualizada: \n",sup_mercado)
		val = input("\n\nDesea continuar s\\n ? ")
		opc = val	
	





	
