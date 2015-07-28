from Dml import DML
from menu import menu


men=("Mostrar","Insertar","Actualizar","Eliminar","Cerrar Conexion")
opc = 0
objeto = DML()
while opc <5:
    opc = menu('DML MySQL',*men)
    if opc == 1:
        objeto.Mostrar()
    elif opc == 2:
        objeto.Insertar()
    elif opc == 3:
        objeto.Actualizar()
    elif opc == 4:
        objeto.Eliminar()
    elif opc == 5:
        objeto.Cerrar_Conexion()
    input("Presione una tecla para continuar...")
else:
    print("\nFin de DML\n".center(90, "#"))
