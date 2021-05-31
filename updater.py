import subprocess
import os
from threading import Thread

#Your app name goes here
file_name = 'app.js'

f = open(file_name, 'r', encoding='utf-8')
current_len = len(f.read())
f.close()

def run():
    p = subprocess.Popen(['node', file_name], shell=True)
    p.communicate()

def check():
    while 1:
        with open(file_name, 'r', encoding='utf-8') as file:
            global current_len
            if (x := len(file.read())) != current_len:
                current_len = x
                os.system('cmd /c taskkill /im node.exe /F')
                Thread(target=run).start()


a = Thread(target=run)
b = Thread(target=check)
b.start()
a.start()
a.join()
b.join()