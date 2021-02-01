import re

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

class AutokeyVigenereCipher :
    def __init__(self) :
        self.indexes = dict(zip(alphabet, range(len(alphabet))))
        self.letters = dict(zip(range(len(alphabet)), alphabet))

    def preprocess_text(self, text) :
        """
        Preprocess text by removing non-alphabetic characters, and uppercasing the text
        """
        preprocessed_text = re.sub(r"[^a-zA-Z]", "", text)
        preprocessed_text = preprocessed_text.upper()
        return preprocessed_text

    def postprocess_text(self, text) :
        """
        Postprocess text by adding whitespace in every 5 consecutive characters in the text
        """
        postprocessed_text = [text[i:i+5] for i in range(0, len(text), 5)]
        postprocessed_text = ' '.join(postprocessed_text)
        return postprocessed_text

    def encrypt(self, plaintext, key, spacing=False) :
        """
        Encrypt plaintext by given key using Auto-Key Vigenere Cipher algorithm
        """
        if len(key) < 2 :
            raise Exception("Key must be at least 2 characters long")

        plaintext = self.preprocess_text(plaintext)
        key = self.preprocess_text(key)

        encrypted = ''
        if len(key) > len(plaintext) :
            key = key[:len(plaintext)]
        elif len(key) < len(plaintext) :
            key += plaintext[:len(plaintext)-len(key)]

        i = 0
        for letter in plaintext :
            encrypted += self.letters[(self.indexes[letter] + self.indexes[key[i]]) % len(alphabet)]
            i += 1

        if spacing :
            encrypted = self.postprocess_text(encrypted)

        return encrypted

    def decrypt(self, ciphertext, key, spacing=False) :
        """
        Decrypt ciphertext by given key using Auto-Key Vigenere Cipher algorithm
        """
        if len(key) < 2 :
            raise Exception("Key must be at least 2 characters long")

        ciphertext = self.preprocess_text(ciphertext)
        key = self.preprocess_text(key)

        decrypted = ''

        i = 0
        for letter in ciphertext :
            decrypted_char = self.letters[(self.indexes[letter] - self.indexes[key[i]]) % len(alphabet)]
            decrypted += decrypted_char
            if len(key) < len(ciphertext) :
                key += decrypted_char
            i += 1

        if spacing :
            decrypted = self.postprocess_text(decrypted)

        return decrypted

# avc = AutokeyVigenereCipher()
# plaintext = "ini adalah contoh plainteks yang sangat panjang"
# key = "cryptokey"
# encrypted = avc.encrypt(plaintext, key, True)
# print(encrypted)
# decrypted = avc.decrypt(encrypted, key, True)
# print(decrypted)