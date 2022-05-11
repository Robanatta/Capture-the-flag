from socket import *

def send(flag, challenge_number):

    # Team usernames
    Usernames = ["fabio.zampiellolutzu","roberto.ibanez.omar","castro.dos.santos.jhefferson"]
    
    for user in Usernames:

        # Create and connect socket to 162.243.73.199:11111 using TCP to send the flag
        flagSocket = socket(AF_INET, SOCK_STREAM)
        flagSocket.connect(("162.243.73.199", 11111))

        # Fabio flag response 

        # Creates the response to send
        send = user + " " + challenge_number + " " + flag.decode('utf-8')
        print("Sending " + user + " flag")
        print(send)

        # Send our flag and recive the response
        flagSocket.send(send.encode('utf-8'))
        fres = flagSocket.recv(1024)
        print(fres.decode())

        # Close socket
        flagSocket.close()
    
