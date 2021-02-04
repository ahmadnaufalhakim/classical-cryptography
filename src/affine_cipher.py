import re

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

class AffineCipher :
    def __init__(self):
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

    def is_coprime(self, p, q) :
        """
        Check if two given numbers are coprime or not
        """
        while q != 0 :
            p, q = q, p%q

        return p == 1

    def extended_euclid_gcd(self, a, b) :
        """
        Returns 3 results, where:
        Referring to the equation ax + by = gcd(a, b)
            1st result is gcd(a, b)
            2nd result is x
            3rd result is y
        """
        r = b; old_r = a
        s = 0; old_s = 1
        t = 1; old_t = 0

        while r != 0 :
            quotient = old_r//r
            old_r, r = r, old_r-quotient*r
            old_s, s = s, old_s-quotient*s
            old_t, t = t, old_t-quotient*t
        return old_r, old_s, old_t

    def modulo_multiplicative_inverse(self, A, M) :
        """
        Returns multiplicative inverse of A under modulo of M, assuming that A and M are coprime
        """
        if not self.is_coprime(A, M) :
            raise Exception(f"{A} and {M} are not coprime")

        gcd, x, y = self.extended_euclid_gcd(A, M)

        while x < 0 :
            x += M

        return x

    def encrypt(self, plaintext, key_m, key_b, spacing=False) :
        """
        Encrypt plaintext by given key using Affine Cipher algorithm
        """
        if len(plaintext) == 0 :
            raise Exception("Plaintext cannot be empty")
        if not self.is_coprime(key_m, len(alphabet)) :
            raise Exception(f"Key M: {key_m} is not coprime with {len(alphabet)}")

        plaintext = self.preprocess_text(plaintext)
        
        encrypted = ''

        for i in range(len(plaintext)) :
            encrypted += self.letters[(key_m*self.indexes[plaintext[i]] + key_b) % len(alphabet)]

        if spacing :
            encrypted = self.postprocess_text(encrypted)

        return encrypted

    def decrypt(self, ciphertext, key_m, key_b, spacing=False) :
        """
        Decrypt ciphertext by given key using Affine Cipher algorithm
        """
        if not self.is_coprime(key_m, len(alphabet)) :
            raise Exception(f"Key M: {key_m} is not coprime with {len(alphabet)}")

        ciphertext = self.preprocess_text(ciphertext)

        decrypted = ''
        key_m_inverse = self.modulo_multiplicative_inverse(key_m, len(alphabet))

        for i in range(len(ciphertext)) :
            decrypted += self.letters[(key_m_inverse*(self.indexes[ciphertext[i]] - key_b)) % len(alphabet)]

        if spacing :
            decrypted = self.postprocess_text(decrypted)

        return decrypted

# ac = AffineCipher()
# print(ac.modulo_multiplicative_inverse(3,8))
# print(ac.encrypt("kripto", 7, 10))
# print(ac.decrypt("czolne", 7, 10))