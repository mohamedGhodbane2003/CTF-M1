import subprocess
import os

def generate_rsa_keys():
    # Create directory if it doesn't exist
    keys_dir = "keys"
    os.makedirs(keys_dir, exist_ok=True)

    # Generate private key
    private_key_path = os.path.join(keys_dir, "pprivate_key.pem")
    subprocess.run(["openssl", "genrsa", "-out", private_key_path, "2048"])

    # Generate public key
    public_key_path = os.path.join(keys_dir, "ppublic_key.pem")
    subprocess.run(["openssl", "rsa", "-in", private_key_path, "-pubout", "-out", public_key_path])

    return private_key_path, public_key_path

if __name__ == "__main__":
    private_key_path, public_key_path = generate_rsa_keys()
    print("Private key generated at:", private_key_path)
    print("Public key generated at:", public_key_path)

