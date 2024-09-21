import math
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend

def extract_rsa_components_from_pem(pem_file):
    with open(pem_file, 'rb') as f:
        pem_data = f.read()

    public_key = serialization.load_pem_public_key(pem_data, backend=default_backend())

    # Extrait N et e de la clé RSA
    n = public_key.public_numbers().n
    e = public_key.public_numbers().e

    return n, e




def find_factors(N, e, d):
    # Calculer l'exposant ed - 1
    exponent = e * d - 1

    # Trouver la plus grande puissance de 2 qui divise (ed - 1)
    s = 0
    while exponent % 2 == 0:
        exponent //= 2
        s += 1

    # Initialiser x
    x = 2

    # Répéter jusqu'à ce qu'un facteur soit trouvé ou que toutes les tentatives soient épuisées
    for _ in range(100):
        # Calculer y1
        y1 = pow(x, exponent, N)

        # Vérifier si y1 est valide (y1 != 1 mod N)
        if y1 != 1:
            # Trouver un facteur commun
            gcd = math.gcd(y1 - 1, N)

            # Si le facteur trouvé est différent de N, retourner les facteurs
            if gcd != 1 and gcd != N:
                return gcd, N // gcd

        # Incrémenter x pour la prochaine itération
        x += 1

    # Si aucun facteur n'est trouvé après un certain nombre d'itérations, retourner None
    return None, None

def calculate_private_key(N, e, p, q):
    phi_n = (p - 1) * (q - 1)
    d = pow(e, -1, phi_n)
    return d




def main():
    # Valeurs données
    # Utilisation de la fonction pour extraire les composantes de la clé publique
    fichier_pem = "public_key.pem"
    N, e = extract_rsa_components_from_pem(fichier_pem)

    print("N (modulus) de la clé RSA :", hex(N))
    print("e (exponent) de la clé RSA :", hex(e))    
    
    d = int("4cf4b7c7dd931e2649e95b04e18c3e9c6911824bcf4820698413c3665f0d5b6cfae3b079e812da141f5e138ff552106cab472959a2fd90d6c7a07d94caffde752b81d3ec5168a4d3b0962afa139b83affc840867d65234a1f9ee62d1ddeff26d132e9aecca10f7d1954cefada6902a5f81a9d476548008ac8d4013025d56ebf6e7cdb0fcc15e5e56421dcb64220194f1266a01c8a9e148a94fa6b202d2bd8504dc4d8c1c2caa58d3ac84813508de4ad2729ffb0eb6fe36cb1898bcc60d14152b192c1b66a36acf8999212746c358c238861acc7cc8e29a5cf8e329bbc018f06f11ee742c4563f04ae694d866b612b5601e9db08ca8234ae349c3049e637c94d1", 16)

    # Trouver les facteurs de N
    p, q = find_factors(N, e, d)
    # Calcul de la clé privée
    d1 = calculate_private_key(N, e, p, q)

    # Affichage de la clé privée
    print("Clé privée (d) :", hex(d1))

    if p and q:
        print("Facteurs trouvés :")
        print("p =", hex(p))
        print("q =", hex(q))
    else:
        print("Impossible de trouverles facteurs.")

if __name__ == "__main__":
    main()