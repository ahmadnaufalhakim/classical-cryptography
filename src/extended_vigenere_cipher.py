import string

class ExtendedVigenereCipher:
    def __init__(self):
        self.key = ""

    def _generate_key(self, text):
        if len(self.key) >= len(text):
            return
        key = self.key
        for i in range(len(text) - len(key)):
            self.key += key[i % len(key)]

    def _post_process(self, text):
        text = [text[i:i+5] for i in range(0, len(text), 5)]
        return " ".join(text)

    def encrypt(self, plaintext, key, spacing=False):
        self.key = key
        self._generate_key(plaintext)

        ciphertext = []
        for i in range(len(plaintext)):
            ch = (ord(plaintext[i]) + ord(self.key[i])) % 256
            ciphertext.append(ch)
        ciphertext = bytes(ciphertext)
        if spacing:
            return self._post_process(ciphertext)

        return ciphertext

    def decrypt(self, ciphertext, key, spacing=False):
        self.key = key
        self._generate_key(ciphertext)

        plaintext = []
        for i in range(len(ciphertext)):
            ch = (ord(ciphertext[i]) - ord(self.key[i]) + 256) % 256
            plaintext.append(ch)
        plaintext = bytes(plaintext)
        if spacing:
            return self._post_process(plaintext)

        return plaintext
