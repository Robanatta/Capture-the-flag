# Roberto Ibanez Omar

from socket import *
import send_flag
conversions = {
    "1" : 0,
    "9" : 0,
    "17" : 0,
    "25" : 0,
    "2" : 1,
    "10" : 1,
    "18" : 1,
    "26" : 1,
    "11": 2,
    "19": 2,
    "27": 2,
    "3": 2,
    "4" : 3,
    "12" : 3,
    "20" : 3,
    "28" : 3,
    "5" : 4,
    "13" : 4,
    "21" : 4,
    "29" : 4,
    "6" : 5,
    "12" : 5,
    "20" : 5,
    "30" : 5,
    "7" : 6,
    "15" : 6,
    "23" : 6,
    "31" : 6,
    "8" : 7,
    "16" : 7,
    "24" : 7,
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
add1 = int(add1)
add2 = int(add2)
add3 = int(add3)
add4 = int(add4)

if maski <9:
    bin1 = format(add1, '08b')
    abin1 = list(bin1)
    for i in range(conversions[masks], 8):
        abin1[i] = 0
    sbin1 = ''
    for i in abin1:
        sbin1 += '' + i 
    print(sbin1)
elif maski < 17:
    bin2 = format(add2, '08b')
    abin2 = list(bin2)
    for i in range(conversions[masks], 8):
        abin2[i] = 0
    sbin2 = ''
    for i in abin2:
        sbin2 += ''+i
    print(sbin2)

elif maski < 25:
    bin3 = format(add3, '08b')
    abin3 = list(bin3)
    for i in range(conversions[masks], 8):
        abin3[i] = 0
    sbin3 = ''
    for i in abin3:
        sbin3 += ''+i
    print(sbin3)
elif maski < 33:
    bin4 = format(add4, '08b')
    abin4 = list(bin4)
    for i in range(conversions[masks], 8):
        abin4[i] = 0
    sbin4 = ''
    for i in abin4:
        sbin4 += ''+i
    print(sbin4)
    







serverSocket.close()


def decimalTo8BitBinary(n):
    return format(n, '08b')

def binaryToDecimal(n):
    return int(n, 2)

print(decimalTo8BitBinary(3))
print(binaryToDecimal("00001100"))