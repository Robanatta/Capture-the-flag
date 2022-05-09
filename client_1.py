# Fabio Fabrizio Zampiello Lutzu

from socket import *
import send_flag

# Create socket and connect to 162.243.73.199:9990 using TCP
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.connect(("162.243.73.199", 9990))

# Recive response and close socket connection
res = serverSocket.recv(1024)
print("response flag = " + res.decode("utf-8"))
serverSocket.close()

# Send flag
send_flag.send(res, "1")

