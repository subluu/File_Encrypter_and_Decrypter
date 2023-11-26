from cryptography.fernet import Fernet
import time

class Encrypt:
    pref = input("""
                 [!] Welcome, to the FileEncrypter
                 Type '--start' to start: """)
    if pref == '--start':
        def __init__(self):
            print("""\nNote: This is a symmetric encryption system so decryption will
only work with the same key you used to encrypt the file.
If you would like to use your own symmetric key, replace 
the key in the key.key file.""")
            time.sleep(1)
            self.key = Fernet.generate_key()
            self.fernet = Fernet(self.key)
            self.encrypt()
            self.decrypt()

        def encrypt(self):
            file = input("\n" + r"What file would you like to encrypt? ")
            print('\n')
            with open('key.key', 'rb') as keyFile:
                keyFile.read()
            with open(file, 'rb') as ogFile:
                og = ogFile.read()
            token = self.fernet.encrypt(og)
            with open(file, 'wb') as encFile:
                encFile.write(token)
                time.sleep(1)
                print(f"Your File Has Been Encrypted!:\n {token}\n")

        def decrypt(self):
            file = input("\n" + r"What file would you like to decrypt? ")
            with open('key.key', 'rb') as keyFile:
                keyFile.read()
            with open(file, 'rb') as encryptedFile:
                encrypt = encryptedFile.read()
            enc = self.fernet.decrypt(encrypt)
            with open(file, 'wb') as decFile:
                decFile.write(enc)
                time.sleep(1)
                print(f"\nYour File Has Beed Decrypted!:\n {enc}")
                time.sleep(1)

if __name__ == "__main__":
    Encrypt()