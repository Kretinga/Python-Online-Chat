import socket 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('192.168.193.180', 4444))

while True:
    chat = input(">> ")
    s.send(chat.encode())
    print("[+] Waiting answer...")
    response = s.recv(1024).decode()
    print(f"Server: {response}")