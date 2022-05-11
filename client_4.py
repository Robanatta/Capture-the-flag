# Fabio Fabrizio Zampiello Lutzu

from socket import *
import send_flag

# Create socket and connect to 162.243.73.199:9993 using TCP
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.connect(("162.243.73.199", 9993))

# Recive first response from the server
res = serverSocket.recv(1024)
print(res.decode("utf-8").strip())

# Split the response and saves it in 3 float numbers
rtt, alpha_value, last_rtt = res.split()
rtt = float(rtt.split('ms')[0])
alpha_value = float(alpha_value)
last_rtt = float(last_rtt.split('ms')[0])

# Calculate the estimated RTT, rounds it to a int then convert it back to a string
ertt = alpha_value * last_rtt + (1 - alpha_value) * rtt
ertt = str(int(round(ertt)))
print(ertt)

# Send the estimated RTT to server and receive the flag, then close the connection
serverSocket.send(ertt.encode("utf-8"))
flag = serverSocket.recv(1024)
print(flag.decode("utf-8"))
serverSocket.close()

# Send the flag
send_flag.send(flag, "4")

