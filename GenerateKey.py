#for encrypting our files
from cryptography.fernet import Fernet

key = Fernet.generate_key()
file = open("encryption_key", "wb")
file.write(key)
file.close()