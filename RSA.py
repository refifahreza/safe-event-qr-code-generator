import random
from math import gcd
from Crypto.Util.number import isPrime, inverse
# program ini hanya menerima dan mengeluarkan bilangan bulat

#generate bilangan prima (penggunaan pada program digenerate dua kali untuk p dan q)
def generate_prime_number():
    while True:
        p = random.randint(10**50, 10**100)
        if isPrime(p):
            return p
        
#generate totient RSA =  (p – 1)(q – 1)
def totient(p, q):
    return (p-1)*(q-1)


#generate pasangan kunci
def generate_key_pair(p, q):
    n = p * q
    m = totient(p, q)

    while True:
        e = random.randint(1, m-1)
        if gcd(e, m) == 1:
            break
    d = inverse(e, m)
    return (e, n), (d, n)

#enkripsi plaintext dengan kunci private RSA
def encrypt(private_key, plaintext):
    key, n = private_key
    cipher = pow(plaintext, key, n)
    return cipher

#dekripsi ciphertext dengan kunci publik RSA
def decrypt(public_key, ciphertext):
    key, n = public_key
    plain = pow(ciphertext, key, n)
    return plain
