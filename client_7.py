# Fabio Fabrizio Zampiello Lutzu

from socket import *
import random
import send_flag


# Create socket and connect to 162.243.73.199:9996 using TCP
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.connect(("162.243.73.199", 9996))


# Creates some random value for Seq and Ack then creates first string to send to the server
seq = random.randint(0, 50)
ack = random.randint(51, 100)

ans = "FIN,ACK Seq=" + str(seq) + " Ack=" + str(ack)
print(ans) 

# Recive first and second response from the server 
serverSocket.send(ans)
res = serverSocket.recv(1024).splitlines()
print(res[0])
print(res[1])


if res[0] != None and res[1] != None:
    r1_seq = None
    r1_ack = None
    r2_seq = None
    r2_ack = None

    F = res[0]
    S = res[1]

    # Parse the <ACK>string from the first response from the server 
    i = 0
    while i < len(F):
        if F[i].isdigit():
            if r1_seq == None:
                r1_seq = F[i]
                i += 1
                while i < len(F) and F[i].isdigit():
                    r1_seq += F[i]
                    i += 1
            else:
                if r1_ack == None:
                    r1_ack = F[i]
                    i += 1
                while i < len(F) and F[i].isdigit():
                    r1_ack += F[i]
                    i += 1
        else:
            i += 1

    # Parse the <FIN,ACK>string from the second response from the server 
    i = 0
    while i < len(S):
        if S[i].isdigit():
            if r2_seq == None:
                r2_seq = S[i]
                i += 1
                while i < len(S) and S[i].isdigit():
                    r2_seq += S[i]
                    i += 1
            else:
                if r2_ack == None:
                    r2_ack = S[i]
                    i += 1
                while i < len(S) and S[i].isdigit():
                    r2_ack += S[i]
                    i += 1
        else:
            i += 1

    # Confirms response from server is correct then create the <ACK>string to send
    if r1_seq == r2_seq and r1_ack == r2_ack:
        ans = ("ACK Seq=" + r1_ack + " Ack=" + str(int(r1_seq) + 1))

    # Send answer and receive flag, then close connection
    serverSocket.send(ans)
    print(ans)
    flag = serverSocket.recv(1024)
    print(flag)
    serverSocket.close()
    
    # Send the flag
    send_flag.send(flag, "7")
