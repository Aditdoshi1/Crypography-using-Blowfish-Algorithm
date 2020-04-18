from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet
import os
from Crypto import Random
from Crypto.Cipher import Blowfish
from struct import pack
import sys

def BlowFish(key,iv):
    f=open("input.txt","r")
    content=f.read()
    f.close()
    for i in range(8):
    	content = ' ' + content
    content=content.encode()
    b=len(content)
    if(b%8!=0):
        while(b%8!=0):
            content+=" ".encode()
            b=len(content)
    backend = default_backend()
    cipher = Cipher(algorithms.Blowfish(key), modes.CBC(iv), backend=backend)
    encryptor = cipher.encryptor()
    cont = encryptor.update(content) + encryptor.finalize()
    open("output.txt","w").close()
    f=open("output.txt","wb")
    f.write(cont);
    f.close();

bs = Blowfish.block_size
iv = Random.new().read(bs)
key= b'Adit Doshi'
BlowFish(key, iv)