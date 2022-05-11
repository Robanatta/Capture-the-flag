# Fabio Fabrizio Zampiello Lutzu

from socket import *
import send_flag

# Create socket and connect to 162.243.73.199:9999 using TCP
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.connect(("162.243.73.199", 9999))

# Receive the string representation of the first and second byte
byte = serverSocket.recv(1024).strip()
print(byte)
byte = byte.split(" ")

# Divide the two byte in an array of bits
A = list(byte[0])
B = list(byte[1])
C = [None]*len(A)

# Check if the two bytes have the same length
if len(A) == len(B):

    #Sum the two bytes
    i = len(A)
    while i > 0:
        i -= 1
        x = int(A[i]) + int(B[i])
        if x >= 2:
            if x == 2:
                C[i] = 0
            else:
                C[i] = 1
            if i > 0:
                A[i - 1] = int(A[i - 1]) + 1
            elif i == 0:
                A = C
                B = [0]*len(C)
                B[-1] = 1
                i = len(A)  
        else:
            C[i] = x
    
    # Invert each bits and convert it to string
    ans = ""
    for u in range(len(C)):
        if C[u] == 0:
            ans += "1"
        else:
            ans += "0"

    # Send the checksum to server and receive the flag
    serverSocket.send(ans)
    print(ans)
    flag = serverSocket.recv(1024)
    print(flag)

    # Send the flag
    send_flag.send(flag, "10")
else:
    print("Invalid bytes")

# Close connection
serverSocket.close()

