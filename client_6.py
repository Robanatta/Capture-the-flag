import socket
import send_flag

host = '162.243.73.199'
port = '9995'
socket1 = socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
socket1.connect((host,port))
#sending SYN seq 0
socket1.sendall("SYN Seq=0".encode())
#receiving data from server
data = str(socket1.recv(1024).decode('utf-8'))
print(data)
data = data.rstrip().split(" ")
seq = data[1].split("=")[1]
ack = data[2].split("=")[1]
message = "ACK Seq="+ ack + "Ack=" + str(int(seq)+1)
print(message)
#send data back to the server
socket1.sendall(message.encode())
data = str(socket1.recv(1024).decode('utf-8'))

#test__output
print(data)
#end__output

#send data to 'send_flag'
send_flag.send(data,'6')
socket1.close()