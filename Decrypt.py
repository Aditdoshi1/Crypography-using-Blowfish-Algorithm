from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet
import os
from Crypto import Random
from Crypto.Cipher import Blowfish
from struct import pack
import sys


def DBlowFish(key):
    f=open("output.txt","rb")
    content=f.read()
    f.close()
    iv = content[:bs]
    backend = default_backend()
    cipher = Cipher(algorithms.Blowfish(key), modes.CBC(iv), backend=backend)
    decryptor = cipher.decryptor()
    content=decryptor.update(content[bs:]) + decryptor.finalize()
    f=open("decrypted_data.txt","wb")
    f.write(content)
    f.close()


bs = Blowfish.block_size
key= b'Adit Doshi'
DBlowFish(key)