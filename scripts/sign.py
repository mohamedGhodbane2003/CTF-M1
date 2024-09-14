import subprocess
import os

def sign_challenge(private_key_path, challenge):
    # Write the challenge to a temporary file
    temp_challenge_file = 'temp_challenge.txt'
    with open(temp_challenge_file, 'w') as f:
        f.write(challenge)

    # Define the signature file path
    signature_file = 'temp_signature.bin'

    # Run the OpenSSL command to sign the challenge
    subprocess.run(
        ['openssl', 'dgst', '-sha256', '-sign', private_key_path, '-out', signature_file, temp_challenge_file],check=True)

    # Read and print the signature
    with open(signature_file, 'rb') as f:
        signature = f.read()

    # Clean up temporary files
    os.remove(temp_challenge_file)
    os.remove(signature_file)

    return signature.hex()


private_key_path = input("Enter the path to the private key file: ").strip()
challenge = input("Enter the challenge to be signed: ").strip()
signature = sign_challenge(private_key_path, challenge)
print(f"Signature: {signature}")



