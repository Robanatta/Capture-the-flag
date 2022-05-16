# Jhefferson Castro dos santos
import socket
import send_flag

host = '162.243.73.199'
port = '9992'

#requirements: the TCP responde must have RTT max 2 seconds

#using TCP
socket1 = socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
socket2 = socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
socket1.connect((host,int(port)))
#extract new random port from data received from the socket1
random_port = socket1.recv(1024).decode().rstrip().split(" ")[2]
print("random port: ", random_port)
socket1.close()
socket2.connect((host,int(random_port)))
received_data = socket2.recv(1024)
print(received_data)
send_flag.send(received_data, '3')
socket2.close()

    






