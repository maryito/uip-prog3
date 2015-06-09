nombre =input("Ingrese Su Nombre: ")
vent1 = float (input("Ingrese La Venta #1: "))
vent2 =float (input("Ingrese La Venta #2: "))
vent3 =float (input("Ingrese La Venta #3: "))

venta = vent1+vent2+vent3
comisiones= (venta*12.5)/100

print("\nINFORME DE COMISIONES\n\nVendedor\tVenta\t\tComision\n")
print(nombre,"\t\t",str(venta),"\t\t",str(comisiones))
