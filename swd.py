from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.fernet import Fernet
import base64
import random


class SWD():
    def __init__(self):
        pass

    public_key = 0
    private_key = 0

    def write_encrypted_key(self, writeDocument,encrypted_key):
        with open(writeDocument, 'wb') as file:
            file.write(encrypted_key)

    def write_encrypted_leave(self,writeDocument,encrypted_data):
        with open(writeDocument, 'wb') as file:
            file.write(encrypted_data) 