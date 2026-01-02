from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print('The server is ready receive')
while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    print(f"Receive from {clientAddress}: {message.decode()}")

    modifiedMessage = message.decode().upper()
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)
    if modifiedMessage == 'QUIT':
        serverSocket.close()
        break
    