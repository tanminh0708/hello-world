F = lambda s, n: s[-n:] + s[:-n]
G = lambda s, n: s[n:] + s[:n]

def H(s: bytes, n: int) -> bytes:
    f = list(s)
    l = len(s)
    for i in range(l):
        f[i] = (f[i] + f[(i+n)%l]) & 0xff
    return bytes(f)

def pleb_hash(s: bytes) -> bytes:
    for _ in range(10):
        s = F(s, 5)
        s = H(s, 3)
        s = G(s, 10)
        s = H(s, -9)
    return s

flag = open("flag.txt", "rb").read()
flag_hash = pleb_hash(flag)
with open("output.txt", "w") as f:
    f.write(flag_hash.hex())