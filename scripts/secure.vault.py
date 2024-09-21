from hashlib import sha256

def key_expansion(seed: bytes) -> bytes:
    """Returns 256 bits pseudo-randomly generated from the seed."""
    state = seed
    output = b''
    for i in range(8):
        state = sha256(state).digest()
        output += state[:4]
    return output

def get_seed(expected_iv):
    for seed in range(2**16):
        seed_bytes = seed.to_bytes(2, 'big')
        key_material = key_expansion(seed_bytes)
        IV = key_material[16:32]
        if IV == expected_iv:
            return seed_bytes
    return None

expected_iv = bytes.fromhex('5a784d1c950d26297bf3361d3d36c383')

seed = get_seed(expected_iv)
key_material = key_expansion(seed)
K = key_material[0:16]
IV = key_material[16:32]

print(f"seed: {seed.hex()}")
print(f"Key: {K.hex()}")
print(f"IV: {IV.hex()}")

''''
echo "mnUEn+ViTC19KCzcXhdoa2n2mzk9QtWuhD5+XN0vaCfqCWCug2yQzoLdMZOd/tSC                            
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" | openssl enc -d -aes-128-cbc -K 46b7d7bc979599c2c326b9bf543f3a70 -base64 -iv 5a784d1c950d26297bf3361d3d36c383
'''