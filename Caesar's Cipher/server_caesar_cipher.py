import socket, sys, threading, string

# instantiate server's socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# define address params
IP = '127.0.0.1'
PORT = 5545
ThreadCount = 0

# bind server
try:
    serversocket.bind( (IP, PORT) )
except socket.error as e:
    print(str(e))


# start listening
serversocket.listen()

print('The server is up! Listening at:',IP,PORT)
print()

# ---------------------------------ENCRYPTION BEGINS-------------------------------------------

def new_encryption(clientsocket, address):

    print('-------------------------------------------')
    print('New connection made! Client address:',address)


    # interact with client
    # --------------------------------------------------------------

    # send intro message
    intro = '\nWelcome! If you want to encrypt a message enter 1, If you want to decrypt a message enter 2\n'

    clientsocket.send(intro.encode())

    # wait for OK response
    if clientsocket.recv(1024).decode() != 'OK':
        print('Something went wrong! Disconnecting')
        clientsocket.close()

    choice = clientsocket.recv(1024).decode()  
    print(choice) # either 1/2


    if choice == '1':

        input_message = clientsocket.recv(1024).decode()  
        key = int(clientsocket.recv(1024).decode())
    
        encrypted = cipher_encrypt(input_message, key)
        print(encrypted)
        clientsocket.send(encrypted.encode())

    elif choice == '2':

        input_message = clientsocket.recv(1024).decode()  
        key = int(clientsocket.recv(1024).decode())
    
        decrypted = cipher_decrypt(input_message, key)
        print(decrypted)
        clientsocket.send(decrypted.encode())    

    else:
        # send error message to client
        clientsocket.send('Invalid choice! Try again...'.encode())    


#function for encryption
def cipher_encrypt(message, key):

    encrypted = ""
    

    for c in message:

        if c.isupper(): #check if it's an uppercase character

            c_index = ord(c) - ord('A')
            print (c_index)

            # shift the current character by key positions
            c_shifted = (c_index + key) % 26 + ord('A')
            c_new = chr(c_shifted)
            encrypted += c_new

        elif c.islower(): #check if its a lowecase character

            # subtract the unicode of 'a' to get index in [0-25) range
            c_index = ord(c) - ord('a') 
            print(c_index)
            c_shifted = (c_index + key) % 26 + ord('a')
            c_new = chr(c_shifted)
            encrypted += c_new

        elif c.isdigit():

            # if it's a number,shift its actual value 
            c_new = (int(c) + key) % 10
            encrypted += str(c_new)

        else:

            # if its neither alphabetical nor a number, just leave it like that
            encrypted = 'Not a valid message'

    return encrypted

#function for decryption
def cipher_decrypt(message, key):

    decrypted = ""

    for c in message:

        if c.isupper(): 

            c_index = ord(c) - ord('A')
            # shift the current character to left by key positions to get its original position
            c_og_position = (c_index - key) % 26 + ord('A')
            c_og = chr(c_og_position)
            decrypted += c_og

        elif c.islower(): 

            c_index = ord(c) - ord('a') 
            c_og_position = (c_index - key) % 26 + ord('a')
            c_og = chr(c_og_position)
            decrypted += c_og

        elif c.isdigit():

            # if it's a number,shift its actual value 
            c_og = (int(c) - key) % 10
            decrypted += str(c_og)

        else:

            # if its neither alphabetical nor a number, just leave it like that
            decrypted = 'Not a valid message'

    return decrypted

   

while True:

    # wait until a client connects
    (clientsocket, address) = serversocket.accept() #--> returns (clientsocket, address)

    # we won't reach this point until a client connects
    
    # call the "handle_new_client" function to interact with the client
    new_encryption(clientsocket,address)

    clientsocket.close()    # close the connection and start the next iteration of the loop to wait for the next client





print('The server is going down!')
serversocket.close()    # close down the server




