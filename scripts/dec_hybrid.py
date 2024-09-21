import subprocess
import json
import base64
import sys

def decrypt_passphrase_with_rsa(encrypted_passphrase_hex):
    p = subprocess.Popen(['openssl', 'pkeyutl', '-decrypt', '-inkey', 'keys/my_private_key.pem'],
                         stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    encrypted_passphrase = bytes.fromhex(encrypted_passphrase_hex)
    passphrase, _ = p.communicate(encrypted_passphrase)
    return passphrase.decode()

def decrypt_message_with_aes(ciphertext_base64, passphrase):
    p = subprocess.Popen(['openssl', 'enc', '-d', '-aes-128-cbc', '-base64', '-pass', 'pass:' + passphrase, '-pbkdf2'],
                         stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    ciphertext = base64.b64decode(ciphertext_base64)
    message, _ = p.communicate(ciphertext)
    return message.decode()

def decrypt_message_from_json(json_data):
    data = json.loads(json_data)
    encrypted_passphrase_hex = data["session-key"]
    ciphertext_base64 = data["ciphertext"]
    passphrase = decrypt_passphrase_with_rsa(encrypted_passphrase_hex)
    message = decrypt_message_with_aes(ciphertext_base64, passphrase)
    return message

if len(sys.argv) != 2:
    print("Usage: python script.py <file_path>")
    sys.exit(1)
file_path = sys.argv[1]
with open(file_path, 'r') as file:
    encrypted_data = file.read()

decrypted_data = decrypt_message_from_json(encrypted_data)
print(decrypted_data)