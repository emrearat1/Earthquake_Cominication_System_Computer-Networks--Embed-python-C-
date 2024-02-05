import threading
import socket
import time



ip = socket.gethostbyname(socket.gethostname())
print(ip)
port = 9495
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
            broadcast(f'{nickname} left the chat'.encode('utf-8'))
            nicknames.remove(nickname)

            break

def receive():
    while True:

        client, adress = server.accept()
        clients.append(client)
        thread = threading.Thread(target=handle,args=(client,))
        thread.start()
print("server is listening")

receive()

# def receive_from_stm():
#     while(True):
#         response = ser.readline()
#         # print("response----{}".format(response))
#         if response== b'ALERT':
#             print(response)
#
# ser = serial.Serial('COM6',baudrate= 113000,timeout= 1)  # open serial port
# print(ser.name)         # check which port was really used
# # ser.write(b'hello')     # write a string
#
# stm_thread = threading.Thread(target=receive_from_stm())
# stm_thread.start()
#
# # close port
# ser.close()



