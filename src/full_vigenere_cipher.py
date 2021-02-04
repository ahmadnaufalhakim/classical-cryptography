import string
import random
import re

class FullVigenereCipher:
	def __init__(self):
		self.alphabet_uppercase = list(string.ascii_uppercase)
		self.full_vigenere_matrix = self._generate_full_vigenere_matrix()
		self.regex = re.compile('[^a-zA-Z]')

	def _post_process(self, text):
		text = [text[i:i+5] for i in range(0, len(text), 5)]
		text = " ".join(text)
		return text

	def _generate_full_vigenere_matrix(self):
		matrix = []
		for x in range(26):
			is_duplicate = True
			while is_duplicate:
				temp_alphabet = self.alphabet_uppercase
				random.shuffle(temp_alphabet)
				temp_string = ''.join(temp_alphabet)
				if temp_string not in matrix :
					is_duplicate = False
			matrix.append(temp_string)
		
		return matrix

	def encrypt(self, plaintext, key, spacing=False):
		plaintext = self.regex.sub('', plaintext.lower())
		key = self.regex.sub('', key.lower())
		ciphertext = ''

		for i in range(len(plaintext)):
			idx_key = i % len(key)
			col = string.ascii_lowercase.index(plaintext[i])
			row = string.ascii_lowercase.index(key[idx_key])
			
			ciphertext += self.full_vigenere_matrix[row][col]
		
		if spacing:
			return self._post_process(ciphertext)

		return ciphertext

	def decrypt(self, ciphertext, key, spacing=False):
		ciphertext = self.regex.sub('', ciphertext.upper())
		key = self.regex.sub('', key.lower())
		plaintext = ''

		for i in range(len(ciphertext)):
			idx_key = i % len(key)
			row = string.ascii_lowercase.index(key[idx_key])
			vigenere_row = self.full_vigenere_matrix[row]
			letter_idx = vigenere_row.index(ciphertext[i])
			
			plaintext += string.ascii_lowercase[letter_idx]
		
		if spacing :
			return self._post_process(plaintext)

		return plaintext
