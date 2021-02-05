import string

class ExtendedVigenereCipher:
    def __init__(self):
        self.key = ""

    def _post_process(self, text):
        text = [text[i:i+5] for i in range(0, len(text), 5)]
        return " ".join(text)

    def encrypt(self, plaintext, key, spacing=False):
        self.key = key

        ciphertext = []
        i = 0
        for char in plaintext:
            encrypted_char = (ord(char) + ord(self.key[i])) % 256
            ciphertext.append(encrypted_char)
            i = (i+1) % len(key)

        ciphertext = bytes(ciphertext)
        if spacing:
            return self._post_process(ciphertext)

        return ciphertext

    def decrypt(self, ciphertext, key, spacing=False):
        self.key = key

        plaintext = []
        i = 0
        for char in ciphertext:
            decrypted_char = (ord(char) - ord(self.key[i]) + 256) % 256
            plaintext.append(decrypted_char)
            i = (i+1) % len(key)

        plaintext = bytes(plaintext)
        if spacing:
            return self._post_process(plaintext)

        return plaintext
