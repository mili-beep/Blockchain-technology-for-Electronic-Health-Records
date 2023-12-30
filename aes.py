from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.fernet import Fernet
import base64
import random

class AES:
    def __init__(self):
        pass

    def derive_aes_key(self,shared_key):
        salt = b"some_salt"  # You may want to use a different salt for production
        key_material = HKDF(
            algorithm=hashes.SHA256(),
            length=32,  # AES-256 key size
            salt=salt,
            info=b"key derivation",
            backend=default_backend()
        ).derive(shared_key)
        return key_material

    def AES_encryption(self,readDocument,writeDocument, secretKey):
        with open(readDocument, 'rb') as file:
            document_data = file.read()
        bytes_val = secretKey.to_bytes(32, 'big') 
        # Provide your own key here
        your_key = self.derive_aes_key(bytes_val)

        # Pad the key if it's less than 32 bytes (required for AES-256)
        if len(your_key) < 32:
            your_key = your_key.ljust(32, b' ')

        # Initialize the Fernet cipher with the provided key
        cipher_suite = Fernet(base64.urlsafe_b64encode(your_key))

        # Encrypt the document
        encrypted_data = cipher_suite.encrypt(document_data)

        # Write the encrypted data to a new file
        with open(writeDocument, 'wb') as file:
            file.write(encrypted_data)

        print("\nDocument encrypted successfully with your own key.")

    def AES_decryption(self,readDocument,writeDocument,secretKey):
        bytes_val = secretKey.to_bytes(32, 'big')
        your_key = self.derive_aes_key(bytes_val)  # Replace with your generated key

        if len(your_key) < 32:
            your_key = your_key.ljust(32, b' ')
        # Read the encrypted data from the file
        with open(readDocument, 'rb') as file:
            encrypted_data = file.read()

        # Initialize the Fernet cipher with the key
        cipher_suite = Fernet(base64.urlsafe_b64encode(your_key))

        # Decrypt the data
        decrypted_data = cipher_suite.decrypt(encrypted_data)

        # Write the decrypted data to a new file
        with open(writeDocument, 'wb') as file:
            file.write(decrypted_data)

        print("\nDocument decrypted successfully.")

    def encrypt_str(self,encryptStr,secretKey):
        encryptStr = bytes(encryptStr,'utf-8')
   

        # Initialize the Fernet cipher with the provided key
        cipher_suite = Fernet(base64.urlsafe_b64encode(secretKey))

        # Encrypt the document
        encrypted_data = cipher_suite.encrypt(encryptStr)

        #print("String encrypted successfully with your own key.")

        return encrypted_data
    
    def decrypt_str(self,decryptStr,secretKey):
        

        # Initialize the Fernet cipher with the key
        cipher_suite = Fernet(base64.urlsafe_b64encode(secretKey))

        # Decrypt the data
        decrypted_data = cipher_suite.decrypt(decryptStr)

        print("\nDocument decrypted successfully.")

        return decrypted_data