from tkinter import *
from tkinter import scrolledtext
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
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
		self.window.geometry('640x620')
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

		self.label_m = Label(self.window, text='m :')
		self.m = Entry(self.window, width=40)

		self.label_b = Label(self.window, text='b :')
		self.b = Entry(self.window, width=40)
		
		self.label_spaces = Label(self.window, text='Spaces :')
		self.label_spaces.grid(column=0, row=5, sticky=W, padx=10)

		self.is_spaces = BooleanVar(value=False)

		self.spaces_0 = Radiobutton(self.window, text="No spaces", variable=self.is_spaces, value=False)
		self.spaces_0.grid(column=1, row=5, sticky=W)

		self.spaces_5 = Radiobutton(self.window, text="5 letter groups", variable=self.is_spaces, value=True)
		self.spaces_5.grid(column=2, row=5, sticky=W)

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
		self.btn_savefile_ciphertext.grid(column=0, sticky=S, pady=(20, 5), padx=20, columnspan=3)

	def handler(self, event):
		current = self.combobox_algorithms.current()

		if current == 5: # Affine
			self.label_m.grid(column=0, row=4, sticky=W, padx=10)
			self.m.grid(column=1, row=4, sticky=W)

			self.label_b.grid(column=0, row=5, sticky=W, padx=10)
			self.b.grid(column=1, row=5, sticky=W)

			self.label_key.grid_remove()
			self.key.grid_remove()

			self.label_spaces.grid(column=0, row=6, sticky=W, padx=10)
			self.spaces_0.grid(column=1, row=6, sticky=W)
			self.spaces_5.grid(column=2, row=6, sticky=W)
		
		else:
			self.label_m.grid_remove()
			self.m.grid_remove()

			self.label_b.grid_remove()
			self.b.grid_remove()

			self.label_key.grid(column=0, row=4, sticky=W, padx=10)
			self.key.grid(column=1, row=4, sticky=W)
		
			self.label_spaces.grid(column=0, row=5, sticky=W, padx=10)
			self.spaces_0.grid(column=1, row=5, sticky=W)
			self.spaces_5.grid(column=2, row=5, sticky=W)

	def encrypt_clicked(self):
		current = self.combobox_algorithms.current()
		plaintext = self.plaintext.get("1.0", "end-1c")
		spaces = self.is_spaces.get()

		try:
			if current == 5:
				ciphertext = self.ciphers[current].encrypt(plaintext, int(self.m.get()), int(self.b.get()), spaces)
			else:
				ciphertext = self.ciphers[current].encrypt(plaintext, self.key.get(), spaces)
		except Exception as e:
			ciphertext = ''
			messagebox.showerror("Error", e)

		self.ciphertext.delete("1.0", END)
		self.ciphertext.insert("1.0", ciphertext)

	def decrypt_clicked(self):
		current = self.combobox_algorithms.current()
		ciphertext = self.ciphertext.get("1.0", "end-1c")
		spaces = self.is_spaces.get()

		try:
			if current == 5:
				plaintext = self.ciphers[current].decrypt(ciphertext, int(self.m.get()), int(self.b.get()), spaces)
			else:
				plaintext = self.ciphers[current].decrypt(ciphertext, self.key.get(), spaces)
		except Exception as e:
			plaintext = ''
			messagebox.showerror("Error", e)

		self.plaintext.delete("1.0", END)
		self.plaintext.insert("1.0", plaintext)

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
