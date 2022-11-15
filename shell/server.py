import socket

s = socket.socket()
port = 8080
host = "" #IPv4 Address of host machine
s.connect((host, port))
print("[+] Connected to host machine\n")

while True:
    command = input(str("shell:~$ "))
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





