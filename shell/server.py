import socket

s = socket.socket()
port = 8080
host = "192.168.29.179"
s.connect((host, port))
print("[+] Connected to host machine")
print("")

while True:
    command = input(str("root@daemon:~$ "))
    s.send(command.encode())
    if command == "kill":
        s.send(command.encode())
        print("[+] Shell disconnected")
        break
    elif command == "terminate":
        s.send(command.encode())
        print("\n[+] Terminated socket connection at host machine")
        break
    else:
        data = s.recv(1024)
        print(data)
        continue





