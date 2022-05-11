# Roberto Ibanez Omar

from http import server
from socket import *
import send_flag


serverAddressPort = ("162.243.73.199", 9991)
bytesToSend = str.encode("helo")

# Create socket to 162.243.73.199:9991 using UDP
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.connect(("162.243.73.199", 9991))

# Send the string "helo" to the server
serverSocket.sendto(bytesToSend, serverAddressPort)

# Recive the flag
flag = serverSocket.recv(1024)
print(flag.decode("utf-8"))


# Send the flag and close connection
send_flag.send(flag, "1")
serverSocket.close()
