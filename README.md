# Reverse Shell

Connect to a host machine on your network with it's IPv4 address and execute commands remotely. 

## Features

- Send alert messages with `Pyautogui`
- Get user input through `easygui` text box
- Open URLs in the web browser
- Enter keys on the host remotely
- Send multiple commands simultaneously 

## Commands

```
browse <url> 
alert <message>
text <message>
press <key> 
type <key>
kill 
terminate
```
All other inputs other than the ones mentioned above will be executed on the terminal by default.

**Note: `kill` command breaks the loop on the server while the host would still be listening for new connections. To close the socket completely, use the `terminate` command.**

**To send multiple commands simultaneously, seperate the commands with `&` without space.**

**EG: browse youtube.com&alert SURPRISE!**

## Entering Keys

**Some basic keys and their names:**

- Windows key: `win`
- Tab: `tab`
- Alt key: `alt`
- Control key: `ctrl`
- Shift: `shift`
- Enter: `enter`

### Examples
- `press ctrl,tab` --> Switches tabs
- `type Step away from my device!` --> Types the message on the keyboard
- `press win,r` --> Opens windows run 

## Functioning

**This script was written considering the fact that both the host machine and the server runs python.**

To begin with, run the `host.py` file on the host and connect to it through `server.py` .

*Quick tip: Use the command `pythonw host.py` on the host machine to run python in the background.*

## Dependencies

**Install the dependencies on the host with the following commands**

```
pip3 install webbrowser
pip3 install easygui
pip3 install pyautogui
```


