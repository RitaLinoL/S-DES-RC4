import socket
HOST = '' # Endereco IP local
PORT = 5354            # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(1)
while True:
    con, cliente = tcp.accept()
    print ('Conectado por', cliente)
    while True:
        msg = con.recv(1024)
        if not msg: break
        print (msg.decode('UTF-8'))
    print ('Finalizando conexao do cliente', cliente)
    con.close() 