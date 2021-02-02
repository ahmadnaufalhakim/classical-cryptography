import numpy as np
import re

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

class PlayfairCipher :
    def __init__(self):
        self.playfair_square = [['' for y in range(5)] for x in range(5)]

    def preprocess_text(self, text) :
        """
        Preprocess text by removing non-alphabetic characters, and uppercasing the text
        """
        preprocessed_text = re.sub(r"[^a-zA-Z]", '', text)
        preprocessed_text = preprocessed_text.upper()
        return preprocessed_text

    def postprocess_text(self, text) :
        """
        Postprocess text by adding whitespace in every 5 consecutive characters in the text
        """
        postprocessed_text = [text[i:i+5] for i in range(0, len(text), 5)]
        postprocessed_text = ' '.join(postprocessed_text)
        return postprocessed_text

    def generate_playfair_square(self, key) :
        """
        Generate Playfair Square based on given preprocessed key
        """
        key = self.preprocess_text(key)
        key = re.sub(r"[J]", '', key)
        key = ''.join([j for i, j, in enumerate(key) if j not in key[:i]])
        key = key + re.sub(rf"[{key + 'J'}]", '', alphabet)
        for i in range(5) :
            for j in range(5) :
                self.playfair_square[i][j] = key[i*5 + j]
                self.playfair_square = np.array(self.playfair_square)

    def encrypt(self, plaintext, key, spacing=False) :
        """
        Encrypt plaintext by given key using Playfair Cipher algorithm
        """
        if len(plaintext) == 0 :
            raise Exception("Plaintext cannot be empty")

        plaintext = self.preprocess_text(plaintext)
        self.generate_playfair_square(key)

        encrypted = ''
        new_plaintext = ''

        if len(plaintext) < 2 :
            new_plaintext = plaintext
        else :
            for i in range(len(plaintext)-1) :
                new_plaintext += plaintext[i]
                if plaintext[i] == plaintext[i+1] :
                    new_plaintext += 'X'
            new_plaintext += plaintext[-1]

        if len(new_plaintext) & 1 :
            new_plaintext += 'X'

        for i in range(0, len(new_plaintext), 2) :
            row_1, col_1 = np.where(self.playfair_square == new_plaintext[i])
            row_2, col_2 = np.where(self.playfair_square == new_plaintext[i+1])
            if row_1 == row_2 :
                encrypted += self.playfair_square[row_1][0][(col_1+1) % 5][0]
                encrypted += self.playfair_square[row_2][0][(col_2+1) % 5][0]
            elif col_1 == col_2 :
                encrypted += self.playfair_square[(row_1+1) % 5][0][col_1][0]
                encrypted += self.playfair_square[(row_2+1) % 5][0][col_2][0]
            else :
                encrypted += self.playfair_square[row_1][0][col_2][0]
                encrypted += self.playfair_square[row_2][0][col_1][0]

        if spacing :
            encrypted = self.postprocess_text(encrypted)

        return encrypted

    def decrypt(self, ciphertext, key, spacing=False) :
        """
        Decrypt ciphertext by given key using Playfair Cipher algorithm
        """
        ciphertext = self.preprocess_text(ciphertext)
        self.generate_playfair_square(key)

        decrypted = ''

        for i in range(0, len(ciphertext), 2) :
            row_1, col_1 = np.where(self.playfair_square == ciphertext[i])
            row_2, col_2 = np.where(self.playfair_square == ciphertext[i+1])
            if row_1 == row_2 :
                decrypted += self.playfair_square[row_1][0][(col_1-1) % 5][0]
                decrypted += self.playfair_square[row_2][0][(col_2-1) % 5][0]
            elif col_1 == col_2 :
                decrypted += self.playfair_square[(row_1-1) % 5][0][col_1][0]
                decrypted += self.playfair_square[(row_2-1) % 5][0][col_2][0]
            else :
                decrypted += self.playfair_square[row_1][0][col_2][0]
                decrypted += self.playfair_square[row_2][0][col_1][0]

        decrypted = re.sub(r"[X]", '', decrypted)

        if spacing :
            decrypted = self.postprocess_text(decrypted)

        return decrypted

# pc = PlayfairCipher()
# plaintext = "temui ibu nanti malam"
# key = "jalan ganesha sepuluh"
# encrypted = pc.encrypt(plaintext, key, True)
# print(encrypted)
# decrypted = pc.decrypt(encrypted, key, True)
# print(decrypted)