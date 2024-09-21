import argparse
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization

def extract_rsa_components(public_key_path, private_key_path):
    with open(public_key_path, "rb") as public_key_file:
        public_key_pem = public_key_file.read()
    with open(private_key_path, "rb") as private_key_file:
        private_key_pem = private_key_file.read()

    # Deserialize keys
    private_key = serialization.load_pem_private_key(private_key_pem, password=None, backend=default_backend())
    public_key = serialization.load_pem_public_key(public_key_pem, backend=default_backend())

    # Extract components
    N = private_key.public_key().public_numbers().n
    e = private_key.public_key().public_numbers().e
    d = private_key.private_numbers().d

    return N, e, d

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract RSA components from public and private keys.")
    parser.add_argument("public_key", help="Path to the PEM-encoded public key file.")
    parser.add_argument("private_key", help="Path to the PEM-encoded private key file.")
    args = parser.parse_args()

    N, e, d = extract_rsa_components(args.public_key, args.private_key)

    print("N:", N)
    print("e:", e)
    print("d:", d)
    i = int("295fb63eb09f12a5ad9e7d2c96c7aab4b631c19bafed6214b8b30dccf6d4dcbc53d39e0b6598ab3d271fb0cdc5034fef20baee48a7ab6d4a5523856ee265ae9cd480d3ddd57136a56939d14defe06628a39be935b7a8a91ccc03043a9d33a9b847474a542ddb2a298bca8b3082974ad02ff5450ed283cd1cd79b6f1ed39156a4904a6d3b7aa6fc9bf1812afc58e2a2f11cdc6caf4b6f73d15e27da0cca01496a61ec8d6c8de14805430ef4dfb4bbe8495d3a538e2e0936a0adf9ce12678196dbb427b53d97358a01610f899d18e766830b09cd761ab6b5a1d923a3879ec2e0104c9a981bc4052c383bb927729988b6951c5db9a962416bd1e2295a6449f8ac81", 16)
    print("i", i)