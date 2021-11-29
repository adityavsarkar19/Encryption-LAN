
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