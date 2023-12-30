from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.fernet import Fernet
import base64
import random

class DigitalSignature():
    def __init__(self):
        pass
    def generate_key_pair(self):
        private_key = rsa.generate_private_key(
                public_exponent=65537,
                key_size=2048,
                backend=default_backend()
            )

        public_key = private_key.public_key()
        return private_key, public_key

    def sign_prescription(self, doctor_private_key, filePathPrescription):
        #data = open(filePathPrescription, "r")
        with open(filePathPrescription, "r") as s:
            data = s.read()
            
        signature = doctor_private_key.sign(
                data.encode('utf-8'),
                padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )

        return signature
    def sign_prescription_string(user, doctor_private_key, data):
        #data = open(filePathPrescription, "r")

        signature = doctor_private_key.sign(
                data.encode('utf-8'),
                padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )

        return signature
        
    def verify_signature(doctor_public_key, filePathPrescription, signature):
        data = open(filePathPrescription, "r")
        try:
            doctor_public_key.verify(
                signature,
                data.encode('utf-8'),
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH
                ),
                hashes.SHA256()
            )
            return True
        except Exception as e:
            print(f"Signature verification failed: {e}")
            return False

    def verify_signature_string(doctor_public_key, data, signature):
        try:
            doctor_public_key.verify(
                signature,
                data.encode('utf-8'),
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH
                ),
                hashes.SHA256()
            )
            return True
        except Exception as e:
            print(f"Signature verification failed: {e}")
            return False
        
    def write_digital_sign(self,writeDocument,text):
        with open(writeDocument, 'wb') as file:
            file.write(text)
