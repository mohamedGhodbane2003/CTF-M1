GF2 = GF(2)
x = polygen(GF2, 'x')
poly_base = x^64 + x^4 + x^3 + x + 1
A.<x> = GF2.extension(poly_base)
f = x^4 + x^3 + x + 1
I = f.inverse_mod(poly_base)
hex_number = Integer('7e58b2311e3323f1', 16)
binary_string = bin(hex_number)[2:]
coeffs = [int(bit) for bit in binary_string]
coeffs.reverse()
S = A(coeffs)
P = S * I
print(P)

#P is the poly representation of PSWD
