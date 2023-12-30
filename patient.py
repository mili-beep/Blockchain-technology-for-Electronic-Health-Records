from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.fernet import Fernet
import base64
import random

from diffiehelman import DiffieHelman
from digitalsignature import DigitalSignature



class Patient():
    def __init__(self):
        pass

    def name(self):
        name = input("\nEnter Patient's name: ")
        return name
    
    dh = DiffieHelman()
    private_dh_key, public_dh_key = dh.generate_dh_key(23,4)
    #print(private_dh_key,public_dh_key)
    secret_dh_key = 0
    
    dsa = DigitalSignature()
    private_dsa_key,public_dsa_key = dsa.generate_key_pair()