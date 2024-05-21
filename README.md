# Overview

This is a Chat application that exemplifies a Client-Server Model program. The application illustrates the use of TCP sockets to send and receive messages between two systems, with one system acting as a server and the rest as clients interacting through the server.

This application consists of two main components:
    - The server program, named server.py, must be executed first and stay active for clients to connect.
    - The client program, named client.py, is executed by client computers that will connect to the server for interaction.

These are configured to run on the same computer using different command instances. Still, when running on different computers, the SERVER_HOST constant value on the client.py program must be set to the actual IP of the computer running the server program.

In this application, we can see the Client-Server network model in action. Here, a system acting as a server waits for clients to connect and make requests for information that will be provided to the client or clients accordingly. Meanwhile, the client systems make requests to connect to the server system and requests.


[Software Demo Video](https://zoom.us/clips/share/Z4pkDIita_9ql6K2ek0NrImEbaEscrtfSVk2pH77IzsvFf59WI_OdqGc-37h55GDQtkcoIaWkQcHAUk6_zi_CMTv.XJVVlIZqzgQ0PNdV)

# Network Communication

This application uses the BSD (Berkely) sockets API to send and receive messages and files between server and client, with an active session listening for messages and, in the case of the server, also listening for new connections.

This application establishes a TCP session through a virtual socket-to-socket connection for reliability and in-order delivery. The port numbers are configurable, but by default, we use port number 5002.

Message exchange between the server and the clients occurs through stream sockets that transmit a byte stream (binary sequence). 

# Development Environment

This application was developed using Visual Studio Code.

The application is written in Python and, because of its simplistic nature, only requires some native Python libraries, such as the socket library for connectivity and the thread library for isolation of socket listening.

# Useful Websites

* [Real Python - Socket Programming in Python (Guide)](https://realpython.com/python-sockets/#background)
* [Geeks for Geeks - Client Server Model](https://www.geeksforgeeks.org/client-server-model/)
* [Python - Socket — Low-level networking interface](https://docs.python.org/3/library/socket.html)
# Future Work

* Improve threading handling
* Provide a graphical UI
* Implement sharing files (only uploading currently).