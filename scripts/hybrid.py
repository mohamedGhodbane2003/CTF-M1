import subprocess
import json
import os
import sys

class OpensslError(Exception): 
    pass 


def encrypt_message_with_aes(plaintext, cipher='aes-128-cbc'):  
    passphrase = os.urandom(16).hex() 
    pass_arg = 'pass:{}'.format(passphrase) 
    args = ['openssl', 'enc', '-' + cipher, '-base64', '-pass', pass_arg, '-pbkdf2'] 
    if isinstance(plaintext, str): 
        plaintext = plaintext.encode('utf-8') 
    result = subprocess.run(args, input=plaintext, stdout=subprocess.PIPE, stderr=subprocess.PIPE) 
    error_message = result.stderr.decode() 
    if error_message != '': 
        raise OpensslError(error_message) 
    return result.stdout.decode(), passphrase


def encrypt_passphrase_with_rsa(passphrase):
    p = subprocess.Popen(['openssl', 'pkeyutl', '-encrypt', '-inkey', 'keys/ordinateur.pem', '-pubin'],
                         stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    encrypted_passphrase, _ = p.communicate(passphrase.encode())
    encrypted_passphrase_hex = encrypted_passphrase.hex()
    return encrypted_passphrase_hex

def encrypt_message_from_file(file_path):
    with open(file_path, 'r') as file:
        message = file.read()
    ciphertext_base64, passphrase = encrypt_message_with_aes(message)
    encrypted_passphrase_hex = encrypt_passphrase_with_rsa(passphrase)
    data = {
        "session-key": encrypted_passphrase_hex,
        "ciphertext": ciphertext_base64
    }
    return json.dumps(data, indent=4)


if len(sys.argv) != 2:
    print("Usage: python script.py <file_path>")
    sys.exit(1)
file_path = sys.argv[1]
encrypted_data = encrypt_message_from_file(file_path)
print(encrypted_data)


