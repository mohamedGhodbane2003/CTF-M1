import subprocess


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


def dictionary_attack(challenge, ciphertext, dictionary_file, cipher='aes-128-cbc'):
    with open(dictionary_file, 'r') as f:
        for line in f:
            passphrase = line.strip()
            try:
                plaintext = decrypt(ciphertext, passphrase, cipher)
                if plaintext == challenge:
                    return passphrase
            except OpensslError:
                pass
    return None


dictionary_file = 'text_files/dict.txt'
challenge = b'warty aitch image torte knock'
ciphertext = "U2FsdGVkX1+gyhE6eix6l5YyeSEM7RRfqRDUHphwk0rbchCBtKz4S3mmY1RPwEF7\n"

found_passphrase = dictionary_attack(challenge, ciphertext, dictionary_file)

if found_passphrase:
    print("Passphrase found:", found_passphrase)
else:
    print("Passphrase not found in the dictionary.")
