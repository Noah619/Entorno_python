import socket
import threading

# Configuración del cliente
HOST = '127.0.0.1'  # Dirección IP del servidor (localhost)
PORT = 12345        # Puerto del servidor

def __recibir_mensajes(client):
    while True:
        try:
            mensaje = client.recv(1024).decode('utf-8')
            if mensaje:
                print(mensaje)
        except:
            print("Error al recibir el mensaje.")
            client.close()
            break

def __enviar_mensajes(client):
    while True:
        mensaje = input("")
        client.sendall(mensaje.encode('utf-8'))


Iniciar_cliente(HOST,PORT)

def Iniciar_cliente:
    # Conectar al servidorç
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))

    # Crear hilos para enviar y recibir mensajes simultáneamente
    thread_recibir = threading.Thread(target=__recibir_mensajes, args=(client,))
    thread_enviar = threading.Thread(target=__enviar_mensajes, args=(client,))

    thread_recibir.start()
    thread_enviar.start()