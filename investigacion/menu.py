'''menu que recibira por parametro:
un titulo y un apuntador a una tupla que contendra las opciones
retornando la opcion elegida
version 1.3
'''
def menu(principal,*opc):
    opciones = {}
    validacion = False
    while validacion!=True:
        print(" MENU".center(45, "-"))
        print("\n\t\t -%s- \n"%(principal.upper().title())) # titulo centrado

        for i in range (len(opc)):
            print("\t",i+1,"- ",str(opc[i]).capitalize()) # tabulado con primera letra en mayuscula
            opciones[i+1]=opc[i]
        print("".center(45, "-"))
        eleccion = int(input("Esciba la opcion a Realizar --> "))
        if  eleccion in opciones:
            validacion= True
        else:
            print("Opcion incorrecta ")
            validacion=False
    return eleccion

#Ejemplo
men=("uno","dos","tres","cuarto","cinco")
print("su eleccion fue: "+str(menu("principal",*men)))
