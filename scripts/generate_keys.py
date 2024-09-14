import subprocess

def generate_keys(private_key_path='private.pem', public_key_path='public.pem', key_size=2048):
    # Generate the RSA private key
    subprocess.run(
    ['openssl', 'genpkey', '-algorithm', 'RSA', '-out', private_key_path, '-pkeyopt', f'rsa_keygen_bits:{key_size}'],
    check=True,
    text=True,
    capture_output=True
    )
    print(f"Private key saved to {private_key_path}")
    
    # Generate the RSA public key
    subprocess.run(
    ['openssl', 'rsa', '-pubout', '-in', private_key_path, '-out', public_key_path],
    check=True,
    text=True,
    capture_output=True
    )
    print(f"Public key saved to {public_key_path}")

generate_keys()
