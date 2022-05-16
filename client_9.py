from itertools import count
import socket
import send_flag

host = '162.243.73.199'
port = 9998
socket1 = socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
socket1.connect((host,port))
data = str(socket1.recv(1024).decode('utf-8'))
print()

data = data.rstrip().split(",")
tmp = data
print("data" + str(data))
size = len(data)-3
print("size ===== " + str(size))

counter = 0
flag = 0

for info in data:
    #print(info)
    element = info.split(" ")
    value = element[1]
    print(element)
    socket1.send(value.encode())
    data = socket1.recv(1024)
    print(data)
    if counter == size:
        break
    if len(data) > 15:
        flag = 1
    if flag == 1:
        break
    counter += 1
print("tempppp ==== "+str(tmp))
if flag == 0:
    element = tmp[-2]
    element = element.split(" ")
    value = element[1]
    print("#### element: " +str(element))
    print("### value "+ str(value))
    host = tmp[-1]
    print("host  :" + str(host))
    socket1.close()
    socket1 = socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
    socket1.connect((host,port))
    data = str(socket1.recv(1024).decode('utf-8'))


    socket1.send(value.encode())
    data = socket1.recv(1024)
    print(data)


        

    


socket1.close()
#socket2 = socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
#socket1.connect((response,port))
#data = str(socket2.recv(1024).decode('utf-8'))

#socket1.send(message.encode())


#socket1.close()