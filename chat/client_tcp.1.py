import socket

HOST = input("Host: ")
PORT = 5354           # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)

tcp.connect(dest)

print ('Para sair use CTRL+X\n')
msg = input()
while msg != ('\x18'):
    tcp.send (msg.encode("UTF-8"))
    msg = input()
tcp.close()



