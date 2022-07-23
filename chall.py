from Crypto.Util.number import getPrime, bytes_to_long, GCD

e = 3
while True:
    p = getPrime(1024)
    q = getPrime(1024)
    phi = (p-1) * (q-1)
    if GCD(phi, e) == 1:
        break
n = p*q

flag = open("flag.txt", "rb").read()
assert len(flag) == 86

pt = bytes_to_long(flag)
ct = pow(pt, e, n)
with open("output.txt", "w") as f:
    f.write(f"n = {n}\n")
    f.write(f"ct = {ct}\n")
    


