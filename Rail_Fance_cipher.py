def encrypt_rail_fence(text, rails):
    # Create empty rows
    fence = ['' for _ in range(rails)]
    row = 0
    direction = 1  # 1 means down, -1 means up

    for char in text:
        fence[row] += char
        row += direction
        if row == 0 or row == rails - 1:
            direction *= -1  # Change direction

    return ''.join(fence)


def decrypt_rail_fence(cipher, rails):
    # Create the pattern
    pattern = [['' for _ in range(len(cipher))] for _ in range(rails)]
    row, direction = 0, 1

    for i in range(len(cipher)):
        pattern[row][i] = '*'
        row += direction
        if row == 0 or row == rails - 1:
            direction *= -1

    # Fill the pattern with cipher text
    index = 0
    for r in range(rails):
        for c in range(len(cipher)):
            if pattern[r][c] == '*':
                pattern[r][c] = cipher[index]
                index += 1

    # Read the pattern to get plain text
    result = ''
    row, direction = 0, 1
    for i in range(len(cipher)):
        result += pattern[row][i]
        row += direction
        if row == 0 or row == rails - 1:
            direction *= -1

    return result


# Example
plain_text = "HELLO WORLD"
key = 3

encrypted = encrypt_rail_fence(plain_text.replace(" ", ""), key)
decrypted = decrypt_rail_fence(encrypted, key)

print("Encrypted:", encrypted)
print("Decrypted:", decrypted)
