
import socket
import threading
import json
from urllib.request import urlopen
import time
import serial
nickname = input("nick:")
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('192.168.56.1',9495))
zaman = time.strftime("%d:%m:%Y %H:%M:%S")
ip = socket.gethostbyname(socket.gethostname())
url ='http://ipinfo.io/json'
response = urlopen(url)
location_data = json.load(response)
client.send(f'{nickname} JOINED SERVER ---- IP ADRESS:{ip}---- time:{zaman}----{location_data}'.encode('utf-8'))
def receive():
    while True:
        try:

            message = client.recv(1024).decode('utf-8')
            print(message)
        except:
            pass
def write():
    while True:
        message = f'{nickname}: {input("")}'
        client.send(message.encode('utf-8'))
        # print(message)

def receive_from_stm():
    while(True):
        response = ser.readline()
        # print("response----{}".format(response))
        print(response)
        zaman2 = time.strftime("%d:%m:%Y %H:%M:%S")
        message = f'{nickname}: {response}----IP ADRESS:{ip}---- time:{zaman2}----{location_data}'
        client.send(message.encode('utf-8'))
        # önemli
        # if response== b'ALERT':
        #     zaman2 = time.strftime("%d:%m:%Y %H:%M:%S")
        #     message = f'{nickname}: {"ALERT"}----IP ADRESS:{ip}---- time:{zaman2}----{location_data}'
        #     client.send(message.encode('utf-8'))
        #     print(response)

ser = serial.Serial('COM6',baudrate= 113000,timeout= 1)  # open serial port
print(ser.name)         # check which port was really used


# stm_thread = threading.Thread(target=receive_from_stm())
# stm_thread.start()


receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()

stm_thread = threading.Thread(target=receive_from_stm())
stm_thread.start()

# close port
# ser.close()