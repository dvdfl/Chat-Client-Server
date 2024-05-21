# Chat - Cient application
import socket
from datetime import datetime
from threading import Thread


# server's IP address
# if the server is not on this machine, 
# put the private (network) IP address (e.g 192.168.1.2)
SERVER_HOST = "127.0.0.1"
SERVER_PORT = 5002 # server's port
separator_token = "<SEP>" # we will use this to separate the client name & message
BUFFER_SIZE = 1024

# initialize TCP socket
s = socket.socket()
print(f"[*] Connecting to {SERVER_HOST}:{SERVER_PORT}...")
# connect to the server
s.connect((SERVER_HOST, SERVER_PORT))
print("[+] Connected.")


# prompt the client for a name
name = input("Enter your name: ")

# function to continually listen for messages
def listen_for_messages():
    while True:
        message = s.recv(BUFFER_SIZE).decode()
        print("\r" + message)

# make a thread that listens for messages to this client & print them
t = Thread(target=listen_for_messages)
# make the thread daemon so it ends whenever the main thread ends
t.daemon = True
# start the thread
t.start()

while True:
    # input message we want to send to the server
    to_send =  input("")
    # a way to exit the program
    if to_send.lower() == '-q':
        s.send(to_send.encode())
        break

    if to_send.lower().startswith('-f'):
        cmd_args = to_send.split(" ") 
        file_name = cmd_args[1]
        file_header = f"-f{separator_token}{name}{separator_token}{file_name}"
        s.send(file_header.encode())

        f = open(file_name,'rb') # Open in binary
        l = f.read(BUFFER_SIZE)

        while (l):
            print("\r Sending file.....")
            s.send(l)
            l = f.read(BUFFER_SIZE)
        
        if not l:
            f.close()
        print(" sent!")
        continue
    
    # add the datetime, name & the color of the sender
    date_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S') 
    # to_send = f"{client_color}[{date_now}] {name}{separator_token}{to_send}{Fore.RESET}"
    to_send = f"[{date_now}] {name}{separator_token}{to_send}"
    # finally, send the message
    s.send(to_send.encode())

# close the socket
s.close()