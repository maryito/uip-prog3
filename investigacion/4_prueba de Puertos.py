from socket import * 


ip = input("Ingrese el ip a Escanear: ")
ip_escaner = gethostbyname(ip)

print ("Escaniando Puerto Abiertos de la siguiente direccion: ", ip_escaner)

for i in range(20, 1025):
    s = socket(AF_INET, SOCK_STREAM)

    resultado = s.connect_ex((ip_escaner, i))

    if(resultado == 0) :
        print ("Puerto %d: Esta Abierto "% (i,))
    s.close()