#!/usr/bin/env python3
import random
import time
import os
from secret import a, S

p = 0xae9d5f33de0013821fb88bd87da4c872e1277f48f0888b9a9208a598aa14013d0f909a11f3a6202a1eba9d47324abd46d603afa8ba25be99c1dbb0196dd57233
q = 0x574eaf99ef0009c10fdc45ec3ed264397093bfa4784445cd490452cc550a009e87c84d08f9d310150f5d4ea399255ea36b01d7d45d12df4ce0edd80cb6eab919
g = 3
PK = pow(g, a, p)
assert 1 <= a <= q-1

FLAG = open("flag.txt", "r").read()

def getrandbits(nbits):
    rng = random.Random(int(time.time()) * S)
    return rng.getrandbits(nbits)

def randbelow(p):
    l = p.bit_length() // 2
    return ((random.getrandbits(l) << l) | getrandbits(l)) % p

def challenge():
    try:
        print("Welcome stranger :)")
        print("Only those who possess the wisdom of the memes shall take the flag")
        print("You have one chance. Good luck!\n")
        
        print(f"{hex(PK) = }")
        k = randbelow(q)
        h = pow(g, k, p)
        print(f"{hex(h) = }")
        x = int(input("x = "), 16) % q
        assert 1 <= x <= q-1
        s = (a*x + k) % q
        print(f"{hex(s) = }\n")

        print("I've shown you what I've got. Now it's your turn.")
        x = randbelow(q)
        print(f"{hex(x) = }")
        s = int(input("s = "), 16) % q

        if pow(g, s, p) == (pow(PK, x, p) * h) % p:
            print("Welcome fellow memer!!!")
            print(f"Here's your flag: {FLAG}")
        else:
            print("Normie detected!!!!")
    except:
        print("An error occurred!")

if __name__ == "__main__":
    challenge()