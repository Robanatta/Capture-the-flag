# Roberto Ibanez Omar

from socket import *
import send_flag


serverAddressPort = ("162.243.73.199", 9991)
bytesToSend = str.encode("helo")

# Create socket to 162.243.73.199:9991 using UDP
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.connect(("162.243.73.199", 9991))

# Send the string "helo" to the server
serverSocket.sendto(bytesToSend, serverAddressPort)

# Recive the flag and close connection
flag = serverSocket.recv(1024)
print(flag.decode("utf-8"))
serverSocket.close()

# Send the flag
send_flag.send(flag, "2")

