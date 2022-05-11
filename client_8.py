# Roberto Ibanez Omar

from socket import *
import send_flag

# Create socket and connect to 162.243.73.199:9994 using TCP
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.connect(("162.243.73.199", 9997))

# Recive the response from the server
res = serverSocket.recv(1024)
print(res.decode("utf-8").strip())

serverSocket.close()