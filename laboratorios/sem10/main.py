# Azalia  y Maryon Torres

import menu
import libro
import copia
import lector
import autor
"""Hacer un menú:
1. Ingresar un lector (Permite crear un nuevo lector)
2. Ingresar un autor (Crear un nuevo autor)
3. Ingresar un libro (Permite ingresar un libro)
4. Hacer una peticion (Permite que un autor use una copia de un libro)
5. Hacer una devolucion

- Existen 10 copias de un libro
- Un lector usa una copia
- Un autor escribe un libro"""

peticion = {}
devolucion = {}
copia = {}

opc = 0

while opc < 5:
    menu.menu("Biblioteca Publica",
     "Ingresar un lector",
     "Ingresar un autor",
     "Ingresar un libro",
     "Hacer una peticion",
     "Hacer una devolucion")

    opc = int(input("\nIndique la acción que desea realizar: "))

    if (opc == 1):
        print ("\n***Ingresar un lector***\n")
        ID = lector.id = input("ID: ")
        nom_lec = lector.nombre = input ("Nombre: ")
        lector = lambda identificacion,nombre: print("\t Lector\n ID: "+str(identificacion),"Nombre: "+nombre); # lector actual 
        

    elif (opc == 2):

        print ("\n***Ingresar un autor***\n")
        nom_aut = autor.nombre = input("Nombre: ")
        nac = autor.nacionalidad = input("Nacionalidad: ")

    elif (opc == 3):
        print ("\n***Ingresar un libro***\n")
        titulo = libro.titulo = input ("Titulo: ")
        tipo = libro.tipo = input ("Tipo de Libro: ")
        edit = libro.editorial = input ("Editorial: ")

        peticion [libro.titulo] = 10

    elif (opc == 4):
        print ("\n***Hacer petición de copias***\n")
        pet = input("Ingrese el libro que desea utilizar: ")

        if pet in peticion:
            for libro,cant in peticion.items():

                if libro == pet and cant > 0:
                    cant-=1                    
                    peticion[pet]= cant
                    
                    lector(ID,nom_lec)
                    print("Pidio el libro %s  y Quedan  Disponible %s "%(libro,str(cant)))
                else:
                    print ("Ya no tienes copias disponibles de este libro")
        else:
            print("No esta disponible")

    elif (opc == 5):
        print ("\n***Hacer devolucion de copias***\n")
        dev = input("Ingrese el libro que desea Devolver: ")

        if dev in peticion:
            for libro,cant in peticion.items():
                if libro == dev and cant > 0:                    
                    cant+=1
                    peticion[dev]= cant
                    lector(ID,nom_lec)
                    print("Entrego el libro %s  y Ahora hay  Disponible %s "%(libro,str(cant)))
                else:
                    print ("Ya no tienes copias disponibles de este libro")
        else:
            print("No esta disponible")
        opc == 6
