import random
import sympy

def find_factors(a, b, q):
    factors=[]
    Q_prime_size_bits = 6
    Q_prime = 1

    while Q_prime.bit_length() < Q_prime_size_bits:
        prime = sympy.randprime(2, 2**100)
        factors.append(prime)
        Q_prime *= prime 
    print(factors)

    min_range = (a + Q_prime - 1) // Q_prime
    max_range = (b + Q_prime - 1) // Q_prime
    last_prime = sympy.randprime(min_range, max_range)
    p = (Q_prime * last_prime * q )+ 1
    while True:
        if sympy.isprime(p):
            factors.append(last_prime)
            return p, factors
        last_prime = sympy.randprime(min_range, max_range)
        print(last_prime)
        p = (Q_prime * last_prime * q ) + 1

def find_generator(p, q, factors):
    phi = p - 1
    for g in range(2, p):
        if all(pow(g, phi // factor, p) != 1 for factor in factors):
            return g
        
if __name__ == "__main__":

    a = int("cbfb27cf12a2bd9f01afcc24446823360dcac506aaf2df25174eec3c90a93ef5eea61b0c6094543aac6664f9131593d4abc04ad534153e9284f1178ec0c41caa6ddc20ed769e6974d97875c4c041865626fc82d4e5e072d9dcf14939d5d01001606fffcda4c8b7656743e04485648644f4fab9b0474d49adb0c72a57b17b1d6e2fd5a97dd62408d9f53888964b5ac489da720c24d5862d93c393fdb47dca71b5854143552e8866430c5b21d420136d57a19a7b2a667291287bfda29a58ab053334191c5787724eb7c9afa73ef3f56a0c6a38f3e7c0e478972557a759211cfa08a19d713930bbad2750fa0c4870f8f4a4a8e613a9e39c75d1977f3f4c762f7271", 16)
    b = a + 2**1950
    q = int("caf3551df1a9f3e8d57bb0dcf7dd07dc2d2103a214c6b5470cbac104f2f7867a846c44c022d36cd69dba71993e7bcd09",16)

    p, factors = find_factors(a, b, q)
    g = find_generator(p,q,factors)
    print(f"g: \n{g}")
    print(f"(p-1)//q: \n{factors}")
    print(factors)
