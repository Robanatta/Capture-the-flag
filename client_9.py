# Castro Dos Santos Jhefferson and Fabio Fabrizio Zampiello Lutzu

import socket
import send_flag

# Create socket
host = '162.243.73.199'
port = 9998
socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
socket.connect((host,port))

# Recive from server the data and parse it
D = socket.recv(1024).decode('utf-8')
print(D.strip())
D = D.strip().replace("otherwise ","").split(",")

# Converts IP to binary
Send_ip = list(''.join([bin(int(k)+256)[3:] for k in D[-1].split('.')]))

T = []
F = []
for i in range(len(D) - 2):
    T.append(D[i].split()[0].split('/')[0])
    F.append(D[i].split()[0].split('/')[1])
    T[i] = list(''.join([bin(int(k)+256)[3:] for k in T[i].split('.')]))

# Search for valid interface
max = 0
pos = -1
for i in range(len(T)):
    temp = 0
    c = True
    for h in range(int(F[i])):
        if T[i][h] == Send_ip[h]:
            temp += 1
        else:
            c = False
            break
    if temp > max and c:
                max = temp
                pos = i

# Send interface
if pos >= 0:
    socket.send(str(pos).encode('utf-8'))
    print(str(pos))
else:
    print(D[-2])
    socket.send(D[-2].encode('utf-8'))
flag = socket.recv(1024)
print(flag.decode('utf-8'))

socket.close()

# Send flag
send_flag.send(flag, '9')






