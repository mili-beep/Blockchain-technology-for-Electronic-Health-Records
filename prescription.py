from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.fernet import Fernet
import base64
import random

from aes import AES


class Perscription():
    def __init__(self):
        pass

    symptoms = ""
    diagnosis = ""
    medicines = ""
    leave = ""

    symptomsKey = ""
    diagnosisKey = ""
    medicinesKey = ""
    leaveKey = ""

    encryptedSymptoms = ""
    encryptedDiagnosis = ""
    encryptedMedicines = ""
    encryptedLeave = ""

    def generatePrescriptionSymptoms(self):
        #f = open("p.txt", "w")
        aes = AES()
        self.symptoms = input('\nPlease enter the symptoms: ')
        with open("prescriptionOriginal.txt", 'w', encoding = 'utf-8') as f:
            f.write("Symptoms: ")
            f.write(self.symptoms)
            f.write("\n")
        self.symptomsKey = self.generateKey()
        self.encryptedSymptoms = aes.encrypt_str(self.symptoms,self.symptomsKey)


    def generatePrescriptionDiagnosis(self):
        #f = open("p.txt", "w")
        aes = AES()
        self.diagnosis = input('\nPlease enter the diagnosis: ')
        with open("prescriptionOriginal.txt", 'a+', encoding = 'utf-8') as f:
            f.write("Diagnosis: ")
            f.write(self.diagnosis)
            f.write("\n")
        self.diagnosisKey = self.generateKey()
        self.encryptedDiagnosis = aes.encrypt_str(self.diagnosis,self.diagnosisKey)


    def generatePrescriptionMedicines(self):
        #f = open("p.txt", "w")
        aes = AES()
        self.medicines = input('\nPlease enter the Medicines: ')
        with open("prescriptionOriginal.txt", 'a+', encoding = 'utf-8') as f:
            f.write("Medicines: ")
            f.write(self.medicines)
            f.write("\n")
        self.medicinesKey = self.generateKey()
        self.encryptedMedicines = aes.encrypt_str(self.medicines,self.medicinesKey)


    def generatePrescriptionLeave(self):
        #f = open("p.txt", "w")
        aes = AES()
        self.leave = input('\nIs the Patient sick enough for leave?: ')
        with open("prescriptionOriginal.txt", 'a+', encoding = 'utf-8') as f:
            f.write("Leave Required?: ")
            f.write(self.leave)
            f.write("\n")
        self.leaveKey = self.generateKey()
        self.encryptedLeave = aes.encrypt_str(self.leave,self.leaveKey)


    def generateKey(self):
        aes = AES()
        key = random.randint(2, 23)
        bytes_val = key.to_bytes(32, 'big')
        your_key = aes.derive_aes_key(bytes_val)  # Replace with your generated key

        if len(your_key) < 32:
            your_key = your_key.ljust(32, b' ')
        return your_key