import subprocess
import os
import sys

def sign_file_with_private_key(private_key_path, file_to_sign):
    # Generate signature
    signature = subprocess.check_output(["openssl", "dgst", "-sha256", "-sign", private_key_path, file_to_sign])

    # Convert signature to hexadecimal
    signature_hex = signature.hex()

    return signature_hex

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <private_key> <message>")
        sys.exit(1)

    private_key_path = sys.argv[1]
    file_to_sign = sys.argv[2]

    if not os.path.exists(private_key_path):
        print("Private key not found.")
    elif not os.path.exists(file_to_sign):
        print("File to sign not found.")
    else:
        signature_hex = sign_file_with_private_key(private_key_path, file_to_sign)
        print("Signature :", signature_hex)
