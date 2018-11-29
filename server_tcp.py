# coding=utf-8
import socket
import time

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip = '0.0.0.0'
port = int(raw_input('select a port: '))
file = open('shell.php', 'w')
try:
    server.bind((ip, port))
    server.listen(5)
    print 'ouvindo em:' + ip + ': ' + str(port)

    (client_socket, address) = server.accept()

    client_socket.send("server found\n")
    print "Client found"

    time.sleep(3)
    client_socket.send("connecting...\n\n")
    print "connecting...\n\n"

    time.sleep(10)
    print 'connection with:' + address[0]
    client_socket.send("#############\n# connected #\n#############\n\n\n")
    print "#############\n# connected #\n#############\n\n"

    client_socket.send("enter your nick. (n) to defaut nick)\n")
    client_socket.send("enter your nick: ")
    select = (client_socket.recv(800))
    nick = select + "→"

    if select == "n":
        while True:
            client_socket.send("\n##User 2##\n→")
            print "##User 2:##", client_socket.recv(8000)
            client_socket.send("##User 1##\n→")               #WRITE YOUR NICK
            client_socket.send(raw_input("##User 1##\n→") + "\n") #WRITE YOUR NICK


    else:
        while True:
            client_socket.send ('\n##' + nick + '##')
            print nick , client_socket.recv(8000)
            client_socket.send("##User 1##\n→")         #WRITE YOUR NICK
            client_socket.send(raw_input("User 1\n→") + "\n") #WRITE YOUR NICK


 

except Exception as Erro:

    print Erro
