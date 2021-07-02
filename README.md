# Reverse Shell

Connect to a host machine on your network with it's IPv4 address and execute commands remotely. 

## Features

- Send alert messages with Pyautogui
- Get user input through text box
- Open URLs in web browser
- Enter keys remotely
- Send multiple commands simultaneously 

## Commands

```
browse <url> 
alert <message>
text <message>
press <key> 
```
All other inputs other than the ones mentioned above will be executed on the terminal by default.
**To send multiple commands simultaneously, seperate the commands with `&` without space.**

**EG: browse youtube.com&alert SURPRISE!**
