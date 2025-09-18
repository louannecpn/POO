# Partie 1
m = "0110001101000110"
k = "1110111011110000"

def binaire_vers_texte(binaire: str) -> str:
    texte = ""
    for i in range(0, len(binaire), 8):
        octet = binaire[i:i+8]
        texte += chr(int(octet, 2))
    return texte

def xor_binaire(bin1: str, bin2: str) -> str:
    resultat = ""
    longueur = min(len(bin1), len(bin2))
    for i in range(longueur):
        if bin1[i] != bin2[i]:
            resultat += "1"
        else:
            resultat += "0"
    return resultat

def table_verite():
    print("Question 3 :")
    print("x y | (x XOR y) XOR y")
    for x in [0,1]:
        for y in [0,1]:
            res = (x ^ y) ^ y
            print(f"{x} {y} | {res}")

message_clair = binaire_vers_texte(m)
print("Partie 1:")
print("===========================================================")
print("Question 1 :")
print("Message clair :", message_clair)

message_chiffre_binaire = xor_binaire(m, k)
print("\nQuestion 2 :")
print("Message chiffré :", message_chiffre_binaire)

print("")
table_verite()

message_dechiffre = xor_binaire(message_chiffre_binaire, k)
print("\nQuestion 4 :")
print("Message déchiffré :", binaire_vers_texte(message_dechiffre))
print("Il applique un XOR avec la clé")
print("===========================================================")

# Partie 2
def xor_caractere(c1: str, c2: str) -> str:
    return chr(ord(c1) ^ ord(c2))

def masque_jetable(message: str, cle: str) -> str:
    resultat = ""
    for i in range(len(message)):
        caractere_message = message[i]
        caractere_cle = cle[i % len(cle)]
        resultat += xor_caractere(caractere_message, caractere_cle)
    return resultat

message = "nsi"
cle = "BAC"

message_chiffre = masque_jetable(message, cle)
message_dechiffre = masque_jetable(message_chiffre, cle)
print()
print("Partie 2 :")
print("===========================================================")
print("Message original :", message)
print("Clé              :", cle)
print("Message chiffré  :", message_chiffre)
print("Message déchiffré:", message_dechiffre)
print("===========================================================")