def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.
    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alpha = "abcdefghijklmnopqrstuvwxyz"

    for letter in plaintext:
        if letter in ALPHA or alpha:
            if letter in ALPHA:
                letter_index = (ALPHA.find(letter) + shift) % len(ALPHA)
                ciphertext = ciphertext + ALPHA[letter_index]
            elif letter in alpha:
                letter_index = (alpha.find(letter) + shift) % len(alpha)
                ciphertext = ciphertext + alpha[letter_index]
            else:
                ciphertext = ciphertext + str(letter)

    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.
    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alpha = "abcdefghijklmnopqrstuvwxyz"

    for letter in ciphertext:
        if letter in ALPHA or alpha:
            if letter in ALPHA:
                letter_index = (ALPHA.find(letter) - shift) % len(ALPHA)
                plaintext = plaintext + ALPHA[letter_index]
            elif letter in alpha:
                letter_index = (alpha.find(letter) - shift) % len(alpha)
                plaintext = plaintext + alpha[letter_index]
            else:
                plaintext = plaintext + str(letter)

    return plaintext
