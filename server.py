import socket

server = socket.socket()
server.bind(("localhost", 5000))
server.listen(1)

print("Server started... waiting for client")

client, addr = server.accept()
print("Client connected:", addr)

while True:
    msg = client.recv(1024).decode()
    if not msg:
        break

    print("Uni:", msg)

    reply = input("Ma: ")
    client.send(reply.encode())