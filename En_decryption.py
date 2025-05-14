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
message = "Hello, world!"
key = 3
encrypted_message = encrypt_caesar(message, key)
print("Encrypted:", encrypted_message)

