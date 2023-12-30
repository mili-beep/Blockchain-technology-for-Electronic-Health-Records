from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.fernet import Fernet
import base64
import random

class DiffieHelman():
    def __init__(self):
        pass
    def generate_dh_key(self,prime, base):
        private_key = random.randint(2, prime - 1)
        public_key = (base ** private_key) % prime
        return private_key, public_key
    def calculate_shared_secret(self,privateKey, receivedPublicKey, prime):
        sharedSecret = (receivedPublicKey ** privateKey) % prime
        return sharedSecret