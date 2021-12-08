import socket 


PORT = 5545
SERVER = socket.gethostbyname(socket.gethostname())
FORMAT = 'utf-8'

#print (SERVER)
#Server in my pc is 192.168.137.1

while True:

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # IP of Local host
    client_socket.connect((SERVER, PORT))

    """ THE CLIENT PART """
    server_reply = client_socket.recv(1024).decode()
    print(server_reply)




    Choice = input("Enter your choice (1/2/3/4/5): ")
    #client_socket.send(Choice.encode())

    if Choice[0]=='1':
        OriginalText=input("Enter the Original string/text: ")
        Key=input("Enter the Key/password: ")
        if len(Key.strip())==0:
                Key= socket.gethostbyname(socket.gethostname())
        # mac id
        client_socket.send(OriginalText.encode())
        client_socket.send(Key.encode())

        EncryptedText = client_socket.recv(1024).decode(FORMAT)
        print("Encrypted Text: ", EncryptedText)
        
        print("\n\n\n")
        client_socket.close()
        
    elif Choice[0]=='2':
        EncryptedText=input("Enter the Encrypted string/text: ")
        Key=input("Enter the Key/password: ")
        if len(Key.strip())==0:
                Key= socket.gethostbyname(socket.gethostname())
        
        client_socket.send(EncryptedText.encode())
        client_socket.send(Key.encode())
        # mac id
        DecryptedText = client_socket.recv(1024).decode()
        print("Decrypted Text: ", DecryptedText)
        
        print("\n\n\n")
        client_socket.close()
        
    elif Choice[0]=='3':
        OriginalTextFile=input("Enter the Original Text Filename: ")
        Key=input("Enter the Key/password: ")
        if len(Key.strip())==0:
                Key= socket.gethostbyname(socket.gethostname())
        
        try:
            inFile=open(OriginalTextFile,'r')
            OriginalText=inFile.read()
            inFile.close()
            client_socket.send(OriginalText.encode())
            client_socket.send(Key.encode())

            EncryptedTextFile=input("Enter the Encrypted Text Filename (press enter for default name): ") 
            if len(EncryptedTextFile.strip())==0:
                EncryptedTextFile="ENC"+OriginalTextFile
            #print(EncriptedTextFile)

            EncryptedText = client_socket.recv(1024).decode()
            outFile=open(EncryptedTextFile,'w')
            outFile.write(EncryptedText)
            outFile.close()
        except:
            print("File Error!")
            
        print("Encrypted Text File made. Check in the directory")
        client_socket.close()
        
    elif Choice[0]=='4':
        EncryptedTextFile=input("Enter the Encrypted Text Filename: ")
        Key=input("Enter the Key/password: ")
        if len(Key.strip())==0:
                Key= socket.gethostbyname(socket.gethostname())
        
        try:
            inFile=open(EncryptedTextFile,'r')
            EncryptedText=inFile.read()
            inFile.close()
            client_socket.send(EncryptedText.encode())
            client_socket.send(Key.encode())
            OriginalTextFile=input("Enter the Original Text Filename (press enter for default name): ")
            if len(OriginalTextFile.strip())==0:
                OriginalTextFile="DEC"+EncryptedTextFile
            #print(OriginalTextFile)

            OriginalText = client_socket.recv(1024).decode()
            outFile=open(OriginalTextFile,'w')
            outFile.write(OriginalText)
            outFile.close()
        except:
            print("File Error!")
            
        print("Encrypted Text File made. Check in the directory")
        client_socket.close()

        
    elif Choice[0]=='5':
        print("Disconnecting from Server......")
        client_socket.close()
        break
    else:
        print("Invalid Choice! Try again.")
    




