def prepare_text(text):
    text = text.upper().replace('J', 'I').replace(' ', '')
    result = ''
    i = 0
    while i < len(text):
        a = text[i]
        if i + 1 < len(text):
            b = text[i + 1]
            if a == b:
                result += a + 'X'
                i += 1
            else:
                result += a + b
                i += 2
        else:
            result += a + 'X'
            i += 1
    return result

def generate_matrix(key):
    key = key.upper().replace('J', 'I')
    matrix = ''
    for c in key:
        if c not in matrix and c.isalpha():
            matrix += c
    for c in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if c not in matrix:
            matrix += c
    return [list(matrix[i:i+5]) for i in range(0, 25, 5)]

def find_position(matrix, letter):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == letter:
                return row, col

def encrypt_pair(a, b, matrix):
    row1, col1 = find_position(matrix, a)
    row2, col2 = find_position(matrix, b)

    if row1 == row2:
        return matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
    elif col1 == col2:
        return matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
    else:
        return matrix[row1][col2] + matrix[row2][col1]

def decrypt_pair(a, b, matrix):
    row1, col1 = find_position(matrix, a)
    row2, col2 = find_position(matrix, b)

    if row1 == row2:
        return matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
    elif col1 == col2:
        return matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
    else:
        return matrix[row1][col2] + matrix[row2][col1]

def encrypt_playfair(plain_text, key):
    text = prepare_text(plain_text)
    matrix = generate_matrix(key)
    cipher = ''
    for i in range(0, len(text), 2):
        cipher += encrypt_pair(text[i], text[i + 1], matrix)
    return cipher

def decrypt_playfair(cipher_text, key):
    matrix = generate_matrix(key)
    plain = ''
    for i in range(0, len(cipher_text), 2):
        plain += decrypt_pair(cipher_text[i], cipher_text[i + 1], matrix)
    return plain

# Example
key = "MONARCHY"
plain_text = "HELLO WORLD"

cipher = encrypt_playfair(plain_text, key)
decrypted = decrypt_playfair(cipher, key)

print("Original Text :", plain_text)
print("Encrypted     :", cipher)
print("Decrypted     :", decrypted)
