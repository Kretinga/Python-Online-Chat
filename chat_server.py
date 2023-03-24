import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('192.168.193.180', 4444))
server.listen(0)

connection, address = server.accept()
print(f"Se ha unido al chat la direccion {address}")

while True:
    chat = connection.recv(1024).decode()
    print(f"Cliente: {chat}")
    response = input(">> ")
    connection.send(response.encode())