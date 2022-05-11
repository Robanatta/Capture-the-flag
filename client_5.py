# Roberto Ibanez Omar

from socket import *
import send_flag

conversions = {
    "bits" : 1,
    "Kb" : 10**3,
    "Mb" : 10**6,
    "Gb" : 10**9,
    "Kbps" : 10**3,
    "Mbps" : 10**6,
    "Gbps" : 10**9
}

# Create socket and connect to 162.243.73.199:9994 using TCP
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.connect(("162.243.73.199", 9994))

# Recive the response from the server
res = serverSocket.recv(1024)
print(res.decode("utf-8").strip())

#Splite the response to until we have L, R1 and R2 values and units
LTotal, LMeasure, R1Total, R1Measure, R2Total, R2Measure = res.split()
LName, Lvalue = LTotal.split("=")
R1Name, R1value = R1Total.split("=")
R1Name, R2value = R2Total.split("=")

Lvalue = float(Lvalue)
R1value = float(R1value)
R2value = float(R2value)
 
#Calculate and send the total transmission delay
delay = (Lvalue * conversions[LMeasure]) / (R1value * conversions[R1Measure])
delay+=(Lvalue * conversions[LMeasure]) / (R2value * conversions[R2Measure])
delay = str(delay)
print(delay)

serverSocket.send(delay.encode("utf-8"))

#Receave the flag
flag = serverSocket.recv(1024)
print(flag.decode("utf-8"))
serverSocket.close()


# Send the flag
send_flag.send(flag, "5")