import subprocess

# Exception raised in case of a problem
class OpensslError(Exception):
    pass

def decrypt(ciphertext, passphrase, cipher='aes-128-cbc'):
    # Prepare arguments to send to openssl
    pass_arg = 'pass:{}'.format(passphrase)
    args = ['openssl', 'enc', '-' + cipher, '-d', '-base64', '-pass', pass_arg, '-pbkdf2']

    # If ciphertext is of type str, we need to encode it to bytes to
    # be able to send it in the pipeline to openssl
    if isinstance(ciphertext, str):
        ciphertext = ciphertext.encode('utf-8')

    # Open the pipeline to openssl. Send ciphertext to openssl's stdin, retrieve stdout and stderr
    #    display the invoked command
    #    print('debug : {0}'.format(' '.join(args)))
    result = subprocess.run(args, input=ciphertext, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # If an error message is present on stderr, we stop everything
    # Note: stderr returns bytes(), so we decode it
    error_message = result.stderr.decode()
    if error_message != '':
        raise OpensslError(error_message)

    # OK, openssl sent the decrypted content to stdout.
    return result.stdout

ciphertext = "U2FsdGVkX1/j+TZTZmYGDQi2+JYmaofk+pNFVQrOSmHby8N0MSVIOlZ1l4vsPwHN\n"
passphrase = "mohamed600G"

try:
    decrypted_message = decrypt(ciphertext, passphrase)
    print("Decrypted message:", decrypted_message.decode('utf-8'))
except OpensslError as e:
    print("Error during decryption:", e)
