print("""
To play multiplayer and become server enter 1
To play multiplayer and connect enter 2
To play with a bot enter 3
""")
DEBUG = 1 #For release set this to 0

def dbgPrint(x):
    if DEBUG:
        print(x)



import socket, threading

firstInput = int(input("->"))
dbgPrint("First input is {0}".format(firstInput))

if firstInput == 1:
    multiServer()
elif firstInput == 2:
    multiClient()
elif firstInput == 3:
    bot()




def multiServer():
    pass

def multiClient():
    pass

def bot():
    pass

#NOTES: use threading for network interface and ui consider pygame for gui
class networkManager:
    def __init__(self, clientOrServer):
        dbgPrint("New network manager")

    def clientGetterLoop(clientsocket):
        pass

    def client(self):
        clientsocket = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM
        )
        host =
        port = 15560
        try:
            clientsocket.connect((host,port)) # Connect to h
        except Exception as e:
            dbgPrint(e)
            print("Connection Error")
        t = threading.Thread(run= clientGetterLoop)
        message = clientsocket.recv(1024).decode('ascii') # Receive 1024 bytes
        clientsocket.send(message.encode('ascii')) # Send message
        clientsocket.close()

class uiManager:
    pass
