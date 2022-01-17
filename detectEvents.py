import win32api
import pyautogui
import win32clipboard
import configparser

def retrieveCode(buttonName):
    buttonCode = 0
    if buttonName == 'F1':
        buttonCode = 0x70
    if buttonName == 'F2':
        buttonCode = 0x71
    if buttonName == 'F3':
        buttonCode = 0x72
    if buttonName == 'F4':
        buttonCode = 0x73
    if buttonName == 'F5':
        buttonCode = 0x74
    if buttonName == 'F6':
        buttonCode = 0x75
    if buttonName == 'F7':
        buttonCode = 0x76
    if buttonName == 'F8':
        buttonCode = 0x77
    if buttonName == 'F9':
        buttonCode = 0x78
    if buttonName == 'F10':
        buttonCode = 0x79
    if buttonName == 'F11':
        buttonCode = 0x7A
    if buttonName == 'F12':
        buttonCode = 0x7B
    return buttonCode

#file configuration retrieve
parser = configparser.ConfigParser()
parser.read('config.txt')

pause = parser.get('config', 'pause')
print("Pause with: " +pause)
pause = retrieveCode(pause)


goOn = parser.get('config', 'goOn')
print("GoOn with: " +goOn)
goOn = retrieveCode(goOn)

paste = parser.get('config', 'paste')
print("Paste with: " +paste)
paste = retrieveCode(paste)

stopRec = parser.get('config', 'stopRec')
print("Stop Recording with: " +stopRec)
stopRec = retrieveCode(stopRec)

def detectPressOrClick():
#This function detect a key pressed. It use win32api library and uses codes that can be found at
#https://docs.microsoft.com/en-us/windows/win32/inputdev/virtual-key-codes
    pressedNormalized = 0
    pressed = 0
    x = 0
    y = 0
    text = ''
    #0x75 is F6 Press and will continue after pause
    if pressed >= 0:
        pressed = win32api.GetKeyState(int(goOn))
        if pressed < 0:
            pressedNormalized = 'goOn'

    #0x76 is F7 Press and will pause
    if pressed >= 0:
        pressed = win32api.GetKeyState(int(pause))
        if pressed < 0:
            pressedNormalized = 'pause'

    #0x77 is F8 Press and will paste
    if pressed >= 0:
        pressed = win32api.GetKeyState(int(paste))
        if pressed < 0:
            pressedNormalized = 'paste'
            win32clipboard.OpenClipboard()
            text = win32clipboard.GetClipboardData()
            win32clipboard.CloseClipboard()
            pyautogui.typewrite(text)

    #0x02 is right click
    if pressed >= 0:
        pressed = win32api.GetKeyState(0x02)
        if pressed < 0:
            pressedNormalized = 'Right Click'
            x,y = pyautogui.position()

    #0x01 is left click
    if pressed >= 0:
        pressed = win32api.GetKeyState(0x01)
        if pressed < 0:
            pressedNormalized = 'Left Click'
            x,y = pyautogui.position()
    
    #0x78 is F9 Press and will stop recording mode
    if pressed >= 0:
        pressed = win32api.GetKeyState(int(stopRec))
        if pressed < 0:
            pressedNormalized = 'stopRec'

    #At the end check that a key was pressed        
    if pressed >= 0:
        pressedNormalized = 0
    return pressedNormalized, x, y, text


