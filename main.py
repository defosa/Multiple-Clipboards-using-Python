import win32clipboard
import time

ol = ""


while True:
    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    if ol != data:
        with open ("clip.history.txt", 'a+') as f:
            f.write(data + "/n")
        ol = data
    time.sleep(0.5)
