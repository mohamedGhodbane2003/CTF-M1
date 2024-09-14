import subprocess
import os

def rsa_encrypt(message, public_key):
    # Write the plaintext to a temporary file
    with open('temp_plain.txt', 'w') as f:
        f.write(message)
    
    # Encrypt the plaintext using OpenSSL
    result = subprocess.run(
        ['openssl', 'rsautl', '-encrypt',
        '-inkey', public_key, 
        '-pubin', '-in', 'temp_plain.txt', 
        '-out', 'temp_encrypted.bin'],
        check=True,
        text=True,
        capture_output=True
    )
        
    # Read the encrypted data from the file
    with open('temp_encrypted.bin', 'rb') as f:
        encrypted_data = f.read()
        
        # Clean up temporary files
    os.remove('temp_plain.txt')
    os.remove('temp_encrypted.bin')
        
    return encrypted_data.hex()
    
public_key = input("Enter the public key file name: ")
message = input("Enter the message: ")
encrypted_message = rsa_encrypt(message, public_key)
print(f"encrypted_message: {encrypted_message}")