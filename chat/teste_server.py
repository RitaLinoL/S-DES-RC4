#socket_echo_server.py
import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 5355)
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)

# Listen for incoming connections
sock.listen(2)
msg = ""
while msg != ('\x18'):
    # Receive the data in small chunks and retransmit it

    connection, client_address = sock.accept()

    data = connection.recv(16)
    print('received {!r}'.format(data))
    print('sending data back to the client')
    msg = input()
    message = msg.encode("UTF-8")
    connection.sendall(message)
            
    connection.close()


import socket
from threading import Thread
import time

def recebe_mensagens(socket_):
    while True:
        msg = socket_.recv(1024)
        if not(len(msg)):
            break
        print(msg.decode("utf-8"))
    print("Conexão com o servidor encerrada")


def envia_mensagens(socket_):
    while True:
        msg = input("Msg> ")
        try:
            socket_.sendall(msg.encode("utf-8"))
        except socket.error:
            break
        if msg.lower() == "fim":
            socket_.close()
            break
    print("Envio de mensagens encerrado!")