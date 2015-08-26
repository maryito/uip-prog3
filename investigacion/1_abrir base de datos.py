import mysql.connector
from mysql.connector import errorcode

configuracion={'user':'root',
'password':'best1995',
'host':'localhost',
'database':'usuario_bd'}
try:
    
  bd = mysql.connector.connect(**configuracion)
  print("Conexion exitosa")
except mysql.connector.Error as err:
  print("Error en la conexion \n", err)
else:
  bd.close()
