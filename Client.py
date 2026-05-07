import socket

client = socket.socket()
client.connect(("localhost", 5000))

print("Connected to server")

while True:
    msg = input("Timi: ")
    client.send(msg.encode())

    reply = client.recv(1024).decode()
    print("Uha:", reply)