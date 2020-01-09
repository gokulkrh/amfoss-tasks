q = input("plaintext to be encrypted: ")
key = int(input("key: "))
plaintext = list(q)
ciphertext = ""

for i in q:
    if i.isupper():
        ciphertext += chr((ord(i) + key - 65) % 26 + 65)
    else:
        ciphertext += chr((ord(i) + key - 97) % 26 + 97)

print(ciphertext)