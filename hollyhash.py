#!/usr/bin/env python3
from Crypto.Cipher import AES
from Crypto.Util.strxor import strxor
from Crypto.Util.Padding import pad
import os

BLOCK_SIZE = 16
FLAG = open("flag.txt", "r").read()

def holy_hash(s: bytes, key: bytes) -> str:
    s = pad(s, BLOCK_SIZE)
    blocks = [s[i:i+BLOCK_SIZE] for i in range(0, len(s), BLOCK_SIZE)]
    h = bytes(BLOCK_SIZE)
    cipher = AES.new(key, AES.MODE_ECB)
    for block in blocks:
        h = strxor(h, cipher.encrypt(block))
    return h.hex()

key = os.urandom(16)

for _ in range(200):
    try:
        option = int(input("Your option: "))
        if option == 0:
            print("Give me some data to hash (in hex):")
            s = bytes.fromhex(input()[:4096])
            h = holy_hash(s, key)
            print(h)
        elif option == 1:
            print("Show me what you've got:")
            s = bytes.fromhex(input()[:4096])
            if holy_hash(s, key) == "a"*32:
                print(f"Here's your reward: {FLAG}")
                break
            else:
                print("Nope :^)")
        elif option == 2:
            print("Good bye :)")
            break
        else:
            print("Invalid option")
    except:
        print("An unexpected error occurred!")
        break

