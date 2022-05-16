import socket
import send_flag

host = '162.243.73.199'
port = 9998
socket1 = socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
socket1.connect((host,port))
data = str(socket1.recv(1024).decode('utf-8'))
print(data)



socket1.close()