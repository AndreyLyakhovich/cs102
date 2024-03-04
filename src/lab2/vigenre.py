def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""

    keyword_repeated = (keyword * (len(plaintext) // len(keyword))) + keyword[:len(plaintext) % len(keyword)]

    for i in range(len(plaintext)): 
        if plaintext[i].isalpha():
            shift = ord(keyword_repeated[i].upper()) - ord('A')
            if plaintext[i].isupper():
                ciphertext = ciphertext + (chr((ord(plaintext[i]) + shift - ord('A')) % 26 + ord('A')))
            else:
                ciphertext = ciphertext + (chr((ord(plaintext[i]) + shift - ord('a')) % 26 + ord('a')))
        else:
            ciphertext = ciphertext + plaintext[i]

    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    keyword_repeated = (keyword * (len(ciphertext) // len(keyword))) + keyword[:len(ciphertext) % len(keyword)]

    for i in range (len(ciphertext)):
        if ciphertext[i].isalpha():
            shift = ord(keyword_repeated[i].upper()) - ord('A')
            if ciphertext[i].isupper():
                plaintext = plaintext + (chr((ord(ciphertext[i]) - shift - ord('A')) % 26 + ord('A')))
            else: 
                plaintext = plaintext + (chr((ord(ciphertext[i]) - shift - ord('a')) % 26 + ord('a')))
        else:
            plaintext = plaintext + ciphertext[i]

    return plaintext
