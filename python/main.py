import threading
import socket
import time


ip = socket.gethostbyname(socket.gethostname())
print(ip)
port = 9493
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((ip,port))

server.listen()
clients = []
nicknames = []

def broadcast(message):
    for client in clients:
        client.send(message)
def handle(client):
    while True:
        try:
            message = client.recv(512)
            broadcast(message)
            print(message.decode('utf-8'))
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f'{nickname} left the chat'.encode('ascii'))
            nicknames.remove(nickname)

            break

def receive():
    while True:

        client, adress = server.accept()
        # print(f'connected with {str(adress)}')

        # client.send('NİCK'.encode('ascii'))
        nickname = client.recv(512).decode('utf-8')
        nicknames.append(nickname)
        clients.append(client)

        print(f'nickname of client: {nickname}')
        # print(f'{nickname} joined the chat'.encode('utf-8'))
        # print("connected to server!!!!".encode('utf-8'))

        thread = threading.Thread(target=handle,args=(client,))
        thread.start()
print("server is listening")

receive()
