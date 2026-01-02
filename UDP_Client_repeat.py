from socket import *

serverName = 'localhost'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_DGRAM)

print("Client is ready. Type 'quit' to exit.")

while True:
    message = input('Please input lowercase sentence: ')
    
    
    clientSocket.sendto(message.encode(), (serverName, serverPort))
    
    if message.lower() == 'quit':
        break

    modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
    print(f"Received from server: {modifiedMessage.decode()}")

clientSocket.close()