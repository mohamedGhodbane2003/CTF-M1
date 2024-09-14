# CTF-M1 

## 1. AES-128-CBC Decryption

### Challenge Steps:

1. **Navigate the Environment:**
   - Go out **two times** from the local "poubelle" (trash).
   - Afterward, you will find a **plan**. Pick it up.
   - Use the plan to head **nord-est** (northeast).

2. **Finding the Encrypted Password:**
   - Upon reaching your destination, you will find:
     - **Inscriptions sur le mur** (wall inscriptions),
     - A **terminal d'administration** (administration terminal),
     - A **clavier** (keyboard).
   - Check underneath the keyboard, where you will discover an encrypted password.
   - The encryption used is **AES-128-CBC**, and the encrypted password is as follows:

     ```
     U2FsdGVkX18qP9Qv8gDPfn6+M1ce0tuMHT7XeinCqc8YTjYuw032n81YVYJw7zTg
     Om9a/G9vX1AmG2bfNZHCxA==
     ```

3. **Finding the Passphrase:**
   - The passphrase to decrypt the password is hidden in the **inscriptions sur le mur**.
   - The passphrase is: **ISECR0XX**.

4. **Decrypting the Password:**
   - Use the following details to decrypt the AES-128-CBC encrypted message:
     - **Encrypted message (Base64 encoded):**
       ```
       U2FsdGVkX18qP9Qv8gDPfn6+M1ce0tuMHT7XeinCqc8YTjYuw032n81YVYJw7zTg
       Om9a/G9vX1AmG2bfNZHCxA==
       ```
     - **Passphrase:**
       ```
       ISECR0XX
       ```
   - Using the script `decrypt_aes.py`, you can decrypt the message and obtain the following cleartext:

     ```
     4a631e72-b33d-43f8-90b0-fd96ca32974e
     ```

## 2. RSA Encryption

### Challenge Steps:

1. **Access the Service Terminal:**
   - Go to the **service terminal** and choose the **tutorial** option.

2. **Obtain the Public Key:**
   - Retrieve the public key for **pki_tutorial**.

3. **Encrypt the Message:**
   - Use the retrieved public key to encrypt the message: **"I got it!"**.
   - The script to use is **encrypt_rsa.py**.
   - You will get something like this : 

     ```
      Enter the public key file name: keys/pki_tutorial.pem
      Enter the message: I got it!
      encrypted_message: 0ba0ab876fc0cef1b2ba32d99cf016fb9a83bdac10b811c50b9952e460bd23014fef66ce770e38dc8ac7772ce93a1627a405c1604429df3aa1e071d66c3751f6f70e43eb7f9e96e8de577df19ca6f87c8da8ff60003da2c77c204df75bb366448c862a034d2bc63d336c39cb143efa873f5df3865f7bbc4e732548c6c782b77c2d37d517514d4143674256492f2a5e06fc33f5ea4820e1cfc33e16a0f4d86e04df54bfa53339afc79e84d295d537f35e51918f5e77a9f2b27d47004ed01279d27a549b911dde05ffdb04fe896ce0eea40da667cb7f65e99d817047e8a96ee44ea7c9468f22aa996edc811f678d3f35f51d90c338b4addae38d10a36ea4d04cbb
     ```

## 3. RSA Key Generation

### Challenge Steps:

1. **Generate RSA Keys:**
   - Use the script `generate_keys.py` to generate your RSA public and private keys. 
   - The keys will be saved to `private.pem` and `public.pem` respectively.

2. **Upload Your Public Key:**
   - After generating the keys, upload your public key (`public.pem`) using the **service terminal**.

## 4. Challenge Signature

### Challenge Steps:

1. **Sign the Challenge:**
   - After uploading your public key, go to the **electrique local** to turn the power on. 
   - They will ask you to sign a challenge. 
   - Use the script `sign.py` to sign it. 
   - For example:
     ```
     Enter the path to the private key file: private.pem
     Enter the challenge to be signed: adman harts huzza rinse foray
     Signature: 8f284498fe55b1747969cf72e0333a5d035c4b46397840bf6272f10eada9ceaffa2f9dc645cca9cdb2b93cc8c92a01fb09f93094ade45b1775636c371341c753f091375120fd187ce0156aa65334142e83a283a956e4ef62a118f75c15494fb30f24156205c2226a3071a9ee4c6c0d32a0cab5d1988d7fc7c90366c295a50dfcef581c2b0868f4c1ff93c674fba62cd9eb105e0a2c2816e59706f67c105dd1fd019a32aed064cb8ed823e8663ad2b77f54d4596a4811f7c4bb733f3755226f4123404f085aaf8eb30cdaa5d64eac7b53e541e9b2802619f7272df2bddd2b78cca340c33b82b37091ada9887f695fbbed97698b9e91d220b1d71584e0378f90ed
     ```
