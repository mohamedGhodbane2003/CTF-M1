import subprocess

# Exception raised in case of a problem
class OpensslError(Exception):
    pass

def rsa_encrypt(plaintext, rsa_public_key_path):
    # Prepare the arguments to send to openssl
    args = ['openssl', 'pkeyutl', '-encrypt', '-pubin', '-inkey', rsa_public_key_path]

    # If plaintext is of type str, encode it to bytes
    if isinstance(plaintext, str):
        plaintext = plaintext.encode('utf-8')

    # Open the pipeline to openssl. Send plaintext to openssl's stdin, retrieve stdout and stderr
    result = subprocess.run(args, input=plaintext, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # If an error message is present on stderr, raise an exception
    error_message = result.stderr.decode()
    if error_message != '':
        raise OpensslError(error_message)

    # Return the encrypted content from stdout
    return result.stdout


plaintext = "I got it!"
rsa_public_key_path = "keys/pk_tutorial_key.pem"

try:
    encrypted_message = rsa_encrypt(plaintext, rsa_public_key_path)
    print("Encrypted message:", encrypted_message.hex())
except OpensslError as e:
    print("Error during encryption:", e)

