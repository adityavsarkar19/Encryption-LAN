
import socket 
import threading 
import re
import getmac
import datetime
import random

PORT = 5545
SERVER = socket.gethostbyname(socket.gethostname())
FORMAT = 'utf-8'

#print (SERVER)
#Server in my pc 192.168.137.1

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((SERVER, PORT))


def encrypt_decrypt(TEXT, KEY):
    ENCTEXT=""
    N=len(TEXT)
    for i in range(N):
        T=TEXT[i]
        P=KEY[i%len(KEY)]
        E=chr(ord(T) ^ ord(P))
                
        ENCTEXT+=E

    return ENCTEXT

#def proc()









server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((SERVER,PORT))
server_socket.listen()



def startServer():
    server_socket.listen()
   

while True:
    (csocket, address) = server_socket.accept()
    IP = address[0]
    #Port = address[1]
    #Thread(target=proc, args=(csocket, IP)).start()
    thread = threading.Thread(target = proc, args = (csocket, IP))
    thread.start()


print('Starting server....')
startServer()