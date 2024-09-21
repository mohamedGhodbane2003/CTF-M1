from sympy import isprime, nextprime
from concurrent.futures import ThreadPoolExecutor

def find_p_and_factorization_worker(args):
    a, b, q, lower_r, upper_r = args
    r = nextprime(lower_r)
    i = 0
    while r < upper_r:
        i += 1
        print(f"Tentative {i}")
        p = 2 * q * r + 1
        if isprime(p):
            return p, r
        r = nextprime(r)
    return None, None

def find_p_and_factorization(a, b, q, num_threads=4):
    lower_r = (a - 1) // (2 * q)
    upper_r = (b - 1) // (2 * q)

    # Diviser l'intervalle en sections pour le traitement parallèle
    ranges = [(a, b, q, lower_r + i * (upper_r - lower_r) // num_threads, lower_r + (i + 1) * (upper_r - lower_r) // num_threads) for i in range(num_threads)]

    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        results = list(executor.map(find_p_and_factorization_worker, ranges))

    for p, r in results:
        if p is not None:
            return p, r
    return None, None

def find_generator(p, q, r):
    phi = p - 1
    factors = [2, q, r]

    for g in range(2, p):
        if all(pow(g, phi // factor, p) != 1 for factor in factors):
            return g
    return None

if __name__ == "__main__":
    a_hex = "cbfb27cf12a2bd9f01afcc24446823360dcac506aaf2df25174eec3c90a93ef5eea61b0c6094543aac6664f9131593d4abc04ad534153e9284f1178ec0c41caa6ddc20ed769e6974d97875c4c041865626fc82d4e5e072d9dcf14939d5d01001606fffcda4c8b7656743e04485648644f4fab9b0474d49adb0c72a57b17b1d6e2fd5a97dd62408d9f53888964b5ac489da720c24d5862d93c393fdb47dca71b5854143552e8866430c5b21d420136d57a19a7b2a667291287bfda29a58ab053334191c5787724eb7c9afa73ef3f56a0c6a38f3e7c0e478972557a759211cfa08a19d713930bbad2750fa0c4870f8f4a4a8e613a9e39c75d1977f3f4c762f7271"
    q_hex = "caf3551df1a9f3e8d57bb0dcf7dd07dc2d2103a214c6b5470cbac104f2f7867a846c44c022d36cd69dba71993e7bcd09"
    a = int(a_hex, 16)
    b = a + 2**1950
    q = int(q_hex, 16)

    p, r = find_p_and_factorization(a, b, q)
    if p is not None:
        print(f"\nFactorisation de (p-1)/q:\n2, {r}")
    else:
        print("Aucun p valide trouvé dans l'intervalle.")

    g = find_generator(p, q, r)
    if g is not None:
        print(f"\nTrouvé g: \n{g}")
    else:
        print("Aucun générateur valide trouvé.")