from src.servidor.Funciones_servidor import iniciar_servidor 

# Configuración del servidor
HOST = '127.0.0.1'  # Dirección IP local (localhost)
PORT = 12345        # Puerto del servidor


if __name__ == "__main__":
    iniciar_servidor(HOST, PORT)