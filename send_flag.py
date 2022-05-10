from socket import *

def send(flag, challenge_number):

    # Team usernames
    fabio_usarname = "fabio.zampiellolutzu"
    roberto_username = ""
    castro_username = ""

    # Create and connect socket to 162.243.73.199:11111 using TCP to send the flag
    flagSocket = socket(AF_INET, SOCK_STREAM)
    flagSocket.connect(("162.243.73.199", 11111))

    # Fabio flag response 

    # Creates the response to send
    send = fabio_usarname + " " + challenge_number + " " + flag.decode('utf-8')
    print("Sending " + fabio_usarname + " flag")
    print(send)

    # Send our flag and recive the response
    flagSocket.send(send)
    fres = flagSocket.recv(1024)
    print(fres)
    
    # Roberto flag response

    # Castro flag response

    # Close socket
    flagSocket.close()