You're working with a **Caesar Cipher implementation in Python**, and your code includes both **encryption** and **decryption** functions. Here's a clear explanation of what each part is doing:

---

### 🔹 **1. `encrypt_caesar(plaintext, key)`**

This function **shifts each letter forward** in the alphabet by the given key.

#### ✅ Step-by-step:

* `ciphertext = ''`: Starts with an empty string to build the encrypted message.
* `for char in plaintext`: Goes through each character in the message.
* `char.isalpha()`: Checks if the character is a letter (ignores numbers, punctuation).
* `offset = 65 if char.isupper() else 97`: Finds the ASCII code base — 65 for uppercase, 97 for lowercase.
* `ord(char) - offset`: Converts the character to its position in the alphabet (0–25).
* `+ key % 26`: Adds the key and wraps around using modulo 26.
* `chr(... + offset)`: Converts the new position back to a character.
* `else`: If it's not a letter (like space or punctuation), keep it as is.

---

### 🔹 **2. `decrypt_caesar(ciphertext, key)`**

This function **shifts each letter backward** by the same key to get the original message.

#### ✅ Step-by-step:

* `plaintext = ''`: Starts empty to build the result.
* Uses the same logic as encryption, but instead of adding the key, it subtracts it:

  ```python
  decrypted_char = chr((ord(char) - offset - key + 26) % 26 + offset)
  ```

  * `+ 26` is added to prevent negative numbers during subtraction.

---

### 🔹 **3. The Example**

```python
message = "HELLO"
key = 3
```

You are:

* Encrypting `HELLO` with a shift of `3` → `KHOOR`
* Then decrypting `KHOOR` back to `HELLO`

---

### 🔚 **Output**

```plaintext
Plaintext: HELLO
Encrypted: KHOOR
Decrypted: HELLO
```

---

### ✅ Summary

You’ve built a Caesar Cipher that:

* Works for both uppercase and lowercase letters
* Leaves non-letter characters untouched
* Can both encrypt and decrypt messages using a shift key

Would you like me to simplify this further or turn it into a GUI (like with Tkinter)?
