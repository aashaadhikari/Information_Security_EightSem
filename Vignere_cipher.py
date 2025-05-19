# Vigenère Cipher in Python

def generate_key(text, key):
    key = list(key)
    if len(text) == len(key):
        return "".join(key)
    else:
        for i in range(len(text) - len(key)):
            key.append(key[i % len(key)])
    return "".join(key)

def encrypt(text, key):
    encrypted_text = []
    key = generate_key(text, key)
    for i in range(len(text)):
        if text[i].isalpha():
            shift = (ord(text[i].upper()) + ord(key[i].upper())) % 26
            encrypted_char = chr(shift + ord('A'))
            encrypted_text.append(encrypted_char if text[i].isupper() else encrypted_char.lower())
        else:
            encrypted_text.append(text[i])
    return "".join(encrypted_text)

def decrypt(cipher_text, key):
    original_text = []
    key = generate_key(cipher_text, key)
    for i in range(len(cipher_text)):
        if cipher_text[i].isalpha():
            shift = (ord(cipher_text[i].upper()) - ord(key[i].upper()) + 26) % 26
            original_char = chr(shift + ord('A'))
            original_text.append(original_char if cipher_text[i].isupper() else original_char.lower())
        else:
            original_text.append(cipher_text[i])
    return "".join(original_text)

# Example usage
plain_text = "Hello World"
key = "KEY"

encrypted = encrypt(plain_text, key)
decrypted = decrypt(encrypted, key)

print("Plain Text:", plain_text)
print("Key:", key)
print("Encrypted:", encrypted)
print("Decrypted:", decrypted)
