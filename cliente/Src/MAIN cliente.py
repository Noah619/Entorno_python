from Cliente.Funciones_cliente import iniciar_cliente

 # Configuración del cliente
 # HOST = '127.0.0.1'  # Dirección IP del servidor (localhost)
 # PORT = 12345        # Puerto del servidor

if __name__ == "__main__":
    
    host= input('Introduce Host: ')
    port = input('Introduce el PORT: ')
    port = int(port)

    iniciar_cliente(host,port)