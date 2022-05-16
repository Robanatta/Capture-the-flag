# Roberto Ibanez Omar

from socket import *
import send_flag
conversions = {
    "1" : 0,
    "2" : 1,
    "3" : 2,
    "4" : 3,
    "5" : 4,
    "6" : 5,
    "7" : 6,
    "8" : 7,
    "9" : 0,
    "10" : 1,
    "11" : 2,
    "12" : 3,
    "13" : 4,
    "14" : 5,
    "15" : 6,
    "16" : 7,
    "17" : 0,
    "18" : 1,
    "19" : 2,
    "20" : 3,
    "21" : 4,
    "22" : 5,
    "23" : 6,
    "24" : 7,
    "25" : 0,
    "26" : 1,
    "27" : 2,
    "28" : 3,
    "29" : 4,
    "30" : 5,
    "31" : 6,
    "32" : 7

    
}

# Create socket and connect to 162.243.73.199:9997 using TCP
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.connect(("162.243.73.199", 9997))

# Recive the response from the server
res = serverSocket.recv(1024)
print(res.decode("utf-8").strip())

#Splite the response into IP and mask
add, mask = res.split()
ad = add.decode("utf-8")
masks = mask.decode("utf-8")
maski = int(masks)
add1, add2, add3, add4 = ad.split(".")
iadd1 = int(add1)
iadd2 = int(add2)
iadd3 = int(add3)
iadd4 = int(add4)

#Send the correct network address to the server
if maski <9:
    bin1 = format(iadd1, '08b')
    abin1 = list(bin1)
    for i in range(conversions[masks]+1, 8):
        abin1[i] = "0"
    sbin1 = ''.join(map(str, abin1))
    ibin1 = int(sbin1, 2)
    nAddress = str(ibin1) + ".0.0.0" 
    print(nAddress)
    serverSocket.send(nAddress.encode("utf-8"))
elif maski < 17:
    bin2 = format(iadd2, '08b')
    abin2 = list(bin2)
    for i in range(conversions[masks]+1, 8):
        abin2[i] = "0"
    sbin2 = ''.join(map(str, abin2))
    ibin2 = int(sbin2, 2)
    nAddress = str(add1) +"."+ str(ibin2) + ".0.0"
    print(nAddress)
    serverSocket.send(nAddress.encode("utf-8"))
elif maski < 25:
    bin3 = format(iadd3, '08b')
    abin3 = list(bin3)
    for i in range(conversions[masks]+1, 8):
        abin3[i] = "0"
    sbin3 = ''.join(map(str, abin3))
    ibin3 = int(sbin3, 2)
    nAddress = str(add1) +"."+ str(add2) + "." + str(ibin3) + ".0"
    print(nAddress)
    serverSocket.send(nAddress.encode("utf-8"))
elif maski < 33:
    bin4 = format(iadd4, '08b')
    abin4 = list(bin4)
    for i in range(conversions[masks]+1, 8):
        abin4[i] = "0"
    sbin4 = ''.join(map(str, abin4))
    ibin4 = int(sbin4, 2)
    nAddress = str(add1) + "." + str(add2) + "." + str(add3) + "." + str(ibin4) 
    print(nAddress)
    serverSocket.send(nAddress.encode("utf-8"))
    
#Receave the flag
flag = serverSocket.recv(1024)
print(flag.decode("utf-8"))
serverSocket.close()


# Send the flag
send_flag.send(flag, "8")