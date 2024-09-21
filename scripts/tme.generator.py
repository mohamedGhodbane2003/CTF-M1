import random
from sympy import isprime

def find_next_multiple_of_q(start, q):
    """Find the next multiple of q after start."""
    remainder = (start - 1) % q
    if remainder != 0:
        step = q - remainder
    else:
        step = 0
    return start + step

def generate_p(a, b, q):
    """Generate a prime number p such that a <= p < b and p - 1 is a multiple of q."""
    start = find_next_multiple_of_q(a, q)
    for p_candidate in range(start, b, q):
        if isprime(p_candidate):
            return p_candidate

def generate_g(p, q):
    """Generate a number g of order q modulo p."""
    while True:
        x = random.randint(2, p - 2)
        g = pow(x, (p - 1) // q, p)
        if g != 1:
            return g

if __name__ == "__main__":
    # Define parameters
    a = int("d9a8fa7feac45f3e6e7206ba134a97876861f60d1ce968bb9bb9c32c853ea532cb647e608b2d7cf413ae10062d6496f5d8c6ed99587a9a793534e73a7aa91549f0069dc382b1385363cd6d2eee1d970f85a93df8b1b99f2e6b8c38a6d258a740f6530971fb81ec3fde791636525b5621b5533aff51fc3ae935a55c00739a3de364954657a4861cda5c6a935b08bfb9b3618af678817444d5761ad3633941f7808f13e4d9753ce8de7e48b6239418fc853fb63ef922cd50946294fccc0101aeb558d75d6a7b11f55822a57d1164f757b7a09b277bcce1cbdecab7d1c11158a0b523da90a532f4edee87f9b4cca00d425f867a495b33efc61b4fa02fa6352c0237", 16)
    b = a + 2**1950
    q = int("9d4dd3c407653c27eff870c89fc1dce0532090c464ea112558969c6de2b56b2b", 16)

    try:
        # Generate p
        p = generate_p(a, b, q)
        assert a <= p < b, f"Error: p ({p}) is not in the interval [a, b)"
        assert (p - 1) % q == 0, f"Error: p ({p}) - 1 is not a multiple of q ({q})"

        # Generate g
        g = generate_g(p, q)
        assert pow(g, q, p) == 1, "Error: g**q != 1 mod p"

        print(f"Generated prime p such that (a <= p < b) and (p - 1) is a multiple of q:\n{p}")
        print(f"Generated g such that g**q == 1 mod p:\n{g}")
    except ValueError as e:
        print(f"Error: {e}")
