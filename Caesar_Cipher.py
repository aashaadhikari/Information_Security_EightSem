def encrypt_caesar(plaintext, key):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            # seeing its uppercase/lowercase
            upcase = 65 if char.isupper() else 97
            encrypted_char = chr((ord(char)-upcase + key)%26 + upcase)
            ciphertext += encrypted_char


        else:
            ciphertext +=char # if char is not an alphabet(punctuation, space) don't change


    return ciphertext

def decrypt_caesar(ciphertext, key):
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            # seeing its uppercase/lowercase
            upcase = 65 if char.isupper() else 97
            decrypted_char = chr((ord(char)-upcase - key+26)%26 + upcase)
            plaintext += decrypted_char


        else:
            plaintext +=char # if char is not an alphabet(punctuation, space) don't change


    return plaintext


message = "Hello, world!"
key = 5

encrypted_message = encrypt_caesar(message, key)
decrypted_message = decrypt_caesar(encrypted_message, key)

print("plaintext:", message)
print("Encrypted:", encrypted_message)
print("decrypted:", decrypted_message)

