from Cliente.Funciones_cliente import iniciar_cliente

 # Configuración del cliente
 # HOST = '127.0.0.1'  # Dirección IP del servidor (localhost)
 # PORT = 12345        # Puerto del servidor

if __name__ == "__main__":
    
    HOST= input('Introduce Host: ')
    PORT = input('Introduce el PORT: ')
    PORT = int(PORT)

    iniciar_cliente(HOST,PORT)