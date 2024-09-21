from sage.all import *
from sage.all import *

def interpolate(points, F):
    x = F['x'].gen()
    lagrange_polynomials = []
    for i in range(len(points)):
        numerator = 1
        denominator = 1
        xi, _ = points[i]
        for j in range(len(points)):
            if i != j:
                xj, _ = points[j]
                numerator *= (x - xj)
                denominator *= (xi - xj)
        lagrange_polynomials.append(numerator/denominator)
    result = sum([y * l for (x, y), l in zip(points, lagrange_polynomials)])
    return result

# Define the field
p = 2**64 - 59
F = GF(p)

# Define the values of X and A
X_values = ['78946865d4fe94c4', '2b38908441886cb3', '9e600d658374a87f', 'a03c965f575c0226', '50c2c05cc1b13a06', '91cdd06f0e77b5bc', 'cd9882882aef3ddf', '6ab833cfdb6848ac', '42f00c060465d82c', '2e0d8135a585a35e', '5d740003fb4d50cb', '15e20b1f7f6f5c66', '6517a47cd0b44daa', '3254911b42183bd5', '876e3072350df2cf', 'f88b71aaa033fb48', 'a16e572b4fc5cfc3']
A_values = ['7f93303642d70e6e', '1a724220251689d0', 'c0ddc997c8c4c782', '1790a10022ed2af4', '408ba7cedaa12966', '80ae43c5e073293e', '1d628ecc6f04a13b', '52da353456f336af', '784b39bc530bd37c', '9323272edb14ab7f', '1e88b6aeddd621c4', '93c1981f3506f717', '087fd56e2a75c01a', '2b22099ebb79a958', 'e2df05dfd7a694cd', '66646802094b42f2', 'fed8db495bf6038a']
B_values = ['b7cfcb6d382404d0', '9854256391a63193', '28ca9216e1b3987c', 'ca36e50311efb678', '58754f82ec41f698', 'd530aa2ffaae1e76', 'b2067c305ecd8d4d', '60d60705aee1f0b2', '109f5412fe4e96a9', '84125f5f1ac04ff6', '34ff890867dc0634', '9a61be6fe7966a81', '470ab763f0ffb56f', '09c105f9a2f52324', '3526f6c23da86d84', '002435520e0d1ad1', '50e8508d54287fbe']

# Convert hexadecimal strings to integers
X_values_int = [int(X, 16) for X in X_values]
A_values_int = [int(A, 16) for A in A_values]

# Generate points using X and A
points = [(F(x), F(y)) for x, y in zip(X_values_int, A_values_int)]

# Perform Lagrange interpolation
result = interpolate(points, F)

# Get the constant coefficient
constant_coefficient = result.coefficients()[0]

# Print the constant coefficient in hexadecimal
print(hex(constant_coefficient))