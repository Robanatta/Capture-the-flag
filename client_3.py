
# Jhefferson Castro dos santos
#requirements: the TCP responde must have RTT max 2 seconds
import socket
#using TCP
socket1 = socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
socket2 = socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)

socket1.connect(('162.243.73.199',9996))
data = socket1.recv(128)
socket1.close()
#extract port number from data variable 
#same as extracting the information received from the server and 'copied' into the variabole data.
random_port = int(data.decode('ascii').replace('random port: ', ''))
print("random port: " + str(random_port))

#connecting to the new random port received from the server
socket2.connect(('162.243.73.199', random_port))
data = socket2.recv(128)

print(data.decode('utf-8'))
socket2.close()
