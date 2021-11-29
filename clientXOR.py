import socket 


PORT = 5545
SERVER = socket.gethostbyname(socket.gethostname())
#FORMAT = 'utf-8'

#print (SERVER)
#Server in my pc is 192.168.137.1


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# IP of Local host
client_socket.connect((SERVER, PORT))

""" THE CLIENT PART """





client_socket.close()
