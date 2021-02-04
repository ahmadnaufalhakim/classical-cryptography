from tkinter import *
from tkinter import scrolledtext
from tkinter import ttk
from tkinter import filedialog
from vigenere_cipher import VigenereCipher
from full_vigenere_cipher import FullVigenereCipher
from autokey_vigenere_cipher import AutokeyVigenereCipher
from extended_vigenere_cipher import ExtendedVigenereCipher
from playfair_cipher import PlayfairCipher
from affine_cipher import AffineCipher
import string

class Gui:
	def __init__(self):
		self.window = Tk()
		self.window.title("Tugas Kecil 1 IF4020 - 13517055 13517139")
		self.window.geometry('640x590')
		self.window.resizable(False, False)

		self.label_plaintext = Label(self.window, text="Plaintext")
		self.label_plaintext.grid(column=0, row=0, sticky=W, padx=10)

		self.plaintext = scrolledtext.ScrolledText(self.window, width=65, height=10)
		self.plaintext.grid(column=0, row=1, columnspan=3, padx=5)

		self.btn_openfile_plaintext = Button(self.window, text="Open File Plaintext", command=self.choose_plaintext_file)
		self.btn_openfile_plaintext.grid(column=2, row=0, sticky=E, pady=5, padx=20)

		self.algorithms = [
            'Vigenere Cipher', 
            'Full Vigenere Cipher', 
            'Auto-key Vigenere Cipher',
			'Extended Vigenere Cipher', 
            'Playfair Cipher', 
            'Affine Cipher']

		self.ciphers = {
			0: VigenereCipher(),
			1: FullVigenereCipher(),
			2: AutokeyVigenereCipher(),
			3: ExtendedVigenereCipher(),
			4: PlayfairCipher(),
			5: AffineCipher(),
		}

		self.label_choose_algorithm = Label(self.window, text='Algorithm :')
		self.label_choose_algorithm.grid(column=0, row=3, pady=10, padx=10, sticky=SW)

		self.combobox_algorithms = ttk.Combobox(self.window, values=self.algorithms, width=30, state="readonly")
		self.combobox_algorithms.grid(column=1, row=3, pady=10, sticky=SW)
		self.combobox_algorithms.current(0)
		self.combobox_algorithms.bind('<<ComboboxSelected>>', self.handler)

		self.label_key = Label(self.window, text='Key :')
		self.label_key.grid(column=0, row=4, sticky=W, padx=10)

		self.key = Entry(self.window, width=40)
		self.key.grid(column=1, row=4, sticky=W)

		# self.label_n_transpotition = Label(self.window, text='n_transpotition :')
		# self.n_transpotition = Entry(self.window, width=40)

		self.label_m = Label(self.window, text='m :')
		self.m = Entry(self.window, width=40)

		self.label_b = Label(self.window, text='b :')
		self.b = Entry(self.window, width=40)
		
		self.label_spaces = Label(self.window, text='Spaces :')
		self.label_spaces.grid(column=0, row=5, sticky=W, padx=10)

		self.spaces = Entry(self.window, width=40)
		self.spaces.grid(column=1, row=5, sticky=W)

		self.btn_encrypt = Button(self.window, text="Encrypt", width=15, command=self.encrypt_clicked)
		self.btn_encrypt.grid(column=2, row=3, sticky='E', padx=20)

		self.btn_decrypt = Button(self.window, text="Decrypt", width=15, command=self.decrypt_clicked)
		self.btn_decrypt.grid(column=2, row=4, sticky='E', padx=20)

		self.label_ciphertext = Label(self.window, text="Ciphertext")
		self.label_ciphertext.grid(column=0, row=7, sticky=W, padx=10, pady=(20, 5))

		self.ciphertext = scrolledtext.ScrolledText(self.window, width=65, height=10)
		self.ciphertext.grid(column=0, row=8, columnspan=3, padx=5)

		self.btn_openfile_ciphertext = Button(self.window, text="Open File Ciphertext", command=self.choose_ciphertext_file)
		self.btn_openfile_ciphertext.grid(column=2, row=7, sticky=E, pady=(20, 5), padx=20)
	
		self.btn_savefile_ciphertext = Button(self.window, text="Save File Ciphertext", width=70, command=self.save_ciphertext_file)
		self.btn_savefile_ciphertext.grid(column=0, row=9, sticky='', pady=(20, 5), padx=20, columnspan=3)

	def handler(self, event):
		current = self.combobox_algorithms.current()

		if current == 5: # Affine
			self.label_m.grid(column=0, row=4, sticky=W, padx=10)
			self.m.grid(column=1, row=4, sticky=W)

			self.label_b.grid(column=0, row=5, sticky=W, padx=10)
			self.b.grid(column=1, row=5, sticky=W)

			self.label_key.grid_remove()
			self.key.grid_remove()
		else:
			self.label_m.grid_remove()
			self.m.grid_remove()

			self.label_b.grid_remove()
			self.b.grid_remove()

			self.label_key.grid(column=0, row=4, sticky=W, padx=10)
			self.key.grid(column=1, row=4, sticky=W)
		
		self.label_spaces.grid(column=0, row=5, sticky=W, padx=10)
		self.spaces.grid(column=1, row=5, sticky=W)

		# if current == 0 : # Vigenere
			# self.label_key.grid(column=0, row=4, sticky=W, padx=10)
			# self.key.grid(column=1, row=4, sticky=W)
			
			# self.label_spaces.grid(column=0, row=5, sticky=W, padx=10)
			# self.spaces.grid(column=1, row=5, sticky=W)

			# self.label_n_transpotition.grid_remove()
			# self.n_transpotition.grid_remove()

			# self.label_m.grid_remove()
			# self.m.grid_remove()

			# self.label_b.grid_remove()
			# self.b.grid_remove()
		# elif current == 1 : # Full Vigenere
		# 	self.label_key.grid(column=0, row=4, sticky=W, padx=10)
		# 	self.key.grid(column=1, row=4, sticky=W)

		# 	self.label_spaces.grid(column=0, row=5, sticky=W, padx=10)
		# 	self.spaces.grid(column=1, row=5, sticky=W)

		# 	self.label_n_transpotition.grid_remove()
		# 	self.n_transpotition.grid_remove()

		# 	self.label_m.grid_remove()
		# 	self.m.grid_remove()

		# 	self.label_b.grid_remove()
		# 	self.b.grid_remove()
		# elif current == 2 : # Auto-key Vigenere
		# 	self.label_key.grid(column=0, row=4, sticky=W, padx=10)
		# 	self.key.grid(column=1, row=4, sticky=W)

		# 	self.label_spaces.grid(column=0, row=5, sticky=W, padx=10)
		# 	self.spaces.grid(column=1, row=5, sticky=W)

		# 	self.label_n_transpotition.grid_remove()
		# 	self.n_transpotition.grid_remove()

		# 	self.label_m.grid_remove()
		# 	self.m.grid_remove()

		# 	self.label_b.grid_remove()
		# 	self.b.grid_remove()
		# elif current == 3 : # Extended Vigenere
		# 	self.label_key.grid(column=0, row=4, sticky=W, padx=10)
		# 	self.key.grid(column=1, row=4, sticky=W)

		# 	self.label_spaces.grid(column=0, row=5, sticky=W, padx=10)
		# 	self.spaces.grid(column=1, row=5, sticky=W)
		# 	self.spaces.insert("1", "0")
		# 	self.spaces.config(state=DISABLED)

		# 	self.label_n_transpotition.grid_remove()
		# 	self.n_transpotition.grid_remove()

		# 	self.label_m.grid_remove()
		# 	self.m.grid_remove()

		# 	self.label_b.grid_remove()
		# 	self.b.grid_remove()
		# elif current == 4 : # Playfair
		# 	self.label_key.grid(column=0, row=4, sticky=W, padx=10)
		# 	self.key.grid(column=1, row=4, sticky=W)

		# 	self.label_spaces.grid(column=0, row=5, sticky=W, padx=10)
		# 	self.spaces.grid(column=1, row=5, sticky=W)

		# 	self.label_n_transpotition.grid_remove()
		# 	self.n_transpotition.grid_remove()

		# 	self.label_m.grid_remove()
		# 	self.m.grid_remove()

		# 	self.label_b.grid_remove()
		# 	self.b.grid_remove()
		# elif current == 5 : # Affine
		# 	self.label_m.grid(column=0, row=4, sticky=W, padx=10)
		# 	self.m.grid(column=1, row=4, sticky=W)

		# 	self.label_b.grid(column=0, row=5, sticky=W, padx=10)
		# 	self.b.grid(column=1, row=5, sticky=W)

		# 	self.label_spaces.grid(column=0, row=6, sticky=W, padx=10)
		# 	self.spaces.grid(column=1, row=6, sticky=W)

		# 	self.label_key.grid_remove()
		# 	self.key.grid_remove()

		# 	self.label_n_transpotition.grid_remove()
		# 	self.n_transpotition.grid_remove()

	def encrypt_clicked(self) :
		current = self.combobox_algorithms.current()
		plaintext = self.plaintext.get("1.0", "end-1c")
		key = self.key.get()
		spaces = int(self.spaces.get())

		ciphertext = self.ciphers[current].encrypt(plaintext, key, spaces)
		print(ciphertext)
		self.ciphertext.delete("1.0", END)
		self.ciphertext.insert("1.0", ciphertext)
		# if current == 0 : # Vigenere
		# 	plaintext = self.plaintext.get("1.0", "end-1c")
		# 	key = self.key.get()
		# 	spaces = int(self.spaces.get())

		# 	ciphertext = self.VigenereStandard.encrypt(key, plaintext, spaces)
		# 	self.ciphertext.delete("1.0", END)
		# 	self.ciphertext.insert("1.0", ciphertext)

		# elif current == 1 : # Full Vigenere
		# 	plaintext = self.plaintext.get("1.0", "end-1c")
		# 	key = self.key.get()
		# 	spaces = int(self.spaces.get())
			
		# 	ciphertext = self.FullVigenere.encrypt_full_vigenere(plaintext, key, spaces)
		# 	self.ciphertext.delete("1.0", END)
		# 	self.ciphertext.insert("1.0", ciphertext)
		# elif current == 2 : # Auto-key Vigenere
		# 	plaintext = self.plaintext.get("1.0", "end-1c")
		# 	key = self.key.get()
		# 	spaces = int(self.spaces.get())

		# 	ciphertext, key_fix = self.AutoKeyVigenere.encrypt_auto_key_vigenere(plaintext, key, spaces)
		# 	self.ciphertext.delete("1.0", END)
		# 	self.ciphertext.insert("1.0", ciphertext)
			
		# 	print("key for decrypt : ", key_fix)
		# elif current == 3 : # Extended Vigenere
		# 	plaintext = self.plaintext.get("1.0", "end-1c")
		# 	key = self.key.get()

		# 	ciphertext = self.VigenereExtended.encrypt(key, plaintext, 0)
		# 	self.ciphertext.delete("1.0", END)
		# 	self.ciphertext.insert("1.0", ciphertext)

		# elif current == 4 : # Playfair
		# 	plaintext = self.plaintext.get("1.0", "end-1c")
		# 	key = self.key.get()
		# 	spaces = int(self.spaces.get())
			
		# 	ciphertext = self.PlayFair.encrypt_playfair(plaintext, key, spaces)
		# 	self.ciphertext.delete("1.0", END)
		# 	self.ciphertext.insert("1.0", ciphertext)

		# elif current == 5 : # Affine
		# 	plaintext = self.plaintext.get("1.0", "end-1c")
		# 	m = int(self.m.get())
		# 	b = int(self.b.get())
		# 	spaces = int(self.spaces.get())

		# 	ciphertext = self.AffineChiper.encrypt_affine(plaintext, m, b, spaces)
		# 	self.ciphertext.delete("1.0", END)
		# 	self.ciphertext.insert("1.0", ciphertext)

	def decrypt_clicked(self):
		current = self.combobox_algorithms.current()
		
		# if current == 0 : # Vigenere
		# 	ciphertext = self.ciphertext.get("1.0", "end-1c")
		# 	key = self.key.get()
		# 	spaces = int(self.spaces.get())
			
		# 	plaintext = self.VigenereStandard.decrypt(key, ciphertext, spaces)	
		# 	self.plaintext.delete("1.0", END)
		# 	self.plaintext.insert("1.0", plaintext)
		# elif current == 1 : # Full Vigenere
		# 	ciphertext = self.ciphertext.get("1.0", "end-1c")
		# 	key = self.key.get()
		# 	spaces = int(self.spaces.get())
			
		# 	plaintext = self.FullVigenere.decrypt_full_vigenere(ciphertext, key, spaces)	
		# 	self.plaintext.delete("1.0", END)
		# 	self.plaintext.insert("1.0", plaintext)
		# elif current == 2 : # Auto-key Vigenere
		# 	ciphertext = self.ciphertext.get("1.0", "end-1c")
		# 	key = self.key.get()
		# 	spaces = int(self.spaces.get())
			
		# 	plaintext = self.AutoKeyVigenere.decrypt_auto_key_vigenere(ciphertext, key, spaces)	
		# 	self.plaintext.delete("1.0", END)
		# 	self.plaintext.insert("1.0", plaintext)
		# elif current == 3 : # Extended Vigenere
		# 	ciphertext = self.ciphertext.get("1.0", "end-1c")
		# 	key = self.key.get()
			
		# 	plaintext = self.VigenereExtended.decrypt(key, ciphertext, 0)	
		# 	self.plaintext.delete("1.0", END)
		# 	self.plaintext.insert("1.0", plaintext)

		# elif current == 4 : # Playfair
		# 	ciphertext = self.ciphertext.get("1.0", "end-1c")
		# 	key = self.key.get()
		# 	spaces = int(self.spaces.get())
			
		# 	plaintext = self.PlayFair.decrypt_playfair(ciphertext, key, spaces)	
		# 	self.plaintext.delete("1.0", END)
		# 	self.plaintext.insert("1.0", plaintext)

		# elif current == 5 : # Affine
		# 	ciphertext = self.ciphertext.get("1.0", "end-1c")
		# 	m = int(self.m.get())
		# 	b = int(self.b.get())
		# 	spaces = int(self.spaces.get())
			
		# 	plaintext = self.AffineChiper.decrypt_affine(ciphertext, m, b, spaces)	
		# 	self.plaintext.delete("1.0", END)
		# 	self.plaintext.insert("1.0", plaintext)

	def choose_plaintext_file(self) :
		filename = filedialog.askopenfilename()
		if filename != '' :
			file = open(filename, "rb")
			content = file.read()
			self.plaintext.delete("1.0", END)
			self.plaintext.insert("1.0", content)
			file.close()
	
	def choose_ciphertext_file(self) :
		filename = filedialog.askopenfilename()
		if filename != '' :
			file = open(filename, "rb")
			content = file.read()
			self.ciphertext.delete("1.0", END)
			self.ciphertext.insert("1.0", content)
			file.close()

	def save_ciphertext_file(self) :
		filename = filedialog.asksaveasfilename()
		if filename != '' :
			file = open(filename, "wb")
			content = self.ciphertext.get("1.0", "end-1c")
			file.write(bytes(content.encode()))
			file.close()

if __name__ == "__main__":
   gui = Gui()
   gui.window.mainloop()
   
