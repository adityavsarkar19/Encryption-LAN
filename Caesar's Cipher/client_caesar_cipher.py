import socket, sys


clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

IP = '127.0.0.1'
PORT = 5545

# connect to the server
clientsocket.connect( (IP, PORT) )


# ---------------------------------SEQUENCE BEGINS-------------------------------------------

# wait for intro message
print(clientsocket.recv(1024).decode())   # --> returns a string

# send back an OK response to proceed with the sequence
clientsocket.send('OK'.encode())

print('\n\nEnter your choice of 1 or 2: ',end='')
#asking user for choice beteen encryption or decryption
choice = input() #1/2
clientsocket.send(choice.encode()) 

if choice == '1':

    print('You have selected encryption')
    print('\n\nEnter your message: ',end='')
    # asking user for message
    message = input()

    clientsocket.send(message.encode())  # send message to server


    print('\n\nEnter your key: ',end='')
    # ask user for the key to be used in cipher
    key = input()
    clientsocket.send(key.encode()) #send key to server

    print()

    print("Your encrypted message is : ")
    print(clientsocket.recv(1024).decode()) #recieve encrypted message
    print("Thank you for using Caesar cipher")

elif choice == '2':

    print('You have selected decryption')
    print('\n\nEnter your message: ',end='')
    # asking user for message
    message = input()

    clientsocket.send(message.encode())   # send message to server


    print('\n\nEnter your key: ',end='')
    # ask user for the key to be used in cipher
    key = input()
    clientsocket.send(key.encode()) #send key to server

    print()


    print("Your decrypted message is : ")
    print(clientsocket.recv(1024).decode()) #recieve decrypted message
    print("Thank you for using Caesar cipher")

else:
    # wait for error message
    print()
    print(clientsocket.recv(1024).decode())    
