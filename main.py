from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.fernet import Fernet
import base64
import random

from aes import AES
from diffiehelman import DiffieHelman
from digitalsignature import DigitalSignature
from doctor import Doctor
from getmessage import get_message
from patient import Patient
from pharmacy import Pharmacy
from prescription import Perscription
from publickey import PublicKey
from swd import SWD





    
def main():

    prime = 23
    base = 4
        
    doc = Doctor()
    pat = Patient()
    
    perscription = Perscription()    
    dh = DiffieHelman()
    aes = AES()
    pharmacy = Pharmacy()
    publicKey = PublicKey()
    swd = SWD()
    ds = DigitalSignature()

    print("\n--------------------------------------------\n")
    print("Hello! Welcome to BITS Medical Interface!")
    print("\n-------------------------------------------\n")

    while True:

        print("\n-------------------------------------\n")         
        print("Please select one of the following: \n1: Patient-Doctor session\n2: Pharmacy\n3: SWD\n")

        userType = input("Enter your choice: ")

        if (userType == "1"):



            prime = 23
            base = 4
            
            doc.name()
            pat.name()
            doc.secret_dh_key = dh.calculate_shared_secret(doc.private_dh_key,pat.public_dh_key,prime)
            pat.secret_dh_key = dh.calculate_shared_secret(pat.private_dh_key,doc.public_dh_key,prime)
            if(doc.secret_dh_key == pat.secret_dh_key):
                print("Key exchange successful")
            else:
                print("Key exchange unsuccessful")

            print("\n-------------------------------\n")
            print("\nCreating a new prescription!\n")
            print("\n-------------------------------\n")        

            patientSymptoms = perscription.generatePrescriptionSymptoms()
            patientDiagnosis = perscription.generatePrescriptionDiagnosis()
            patientMedicines = perscription.generatePrescriptionMedicines()
            patientLeave = perscription.generatePrescriptionLeave()


            #print(perscription.symptomsKey)

            #print(perscription.encryptedSymptoms)
           # print(aes.decrypt_str(perscription.encryptedSymptoms,perscription.symptomsKey))


            answer = input("\nDo you wish to encrypt the document?: ")

            if (answer == "Yes" or "yes"):
                aes.AES_encryption("prescriptionOriginal.txt","encrypted_document.txt", doc.secret_dh_key)
                aes.AES_decryption("encrypted_document.txt","decrypted_document.txt",pat.secret_dh_key)


            pharmacy.private_key,pharmacy.public_key = publicKey.generate_key_pair()
            swd.private_key,swd.public_key = publicKey.generate_key_pair()

            encrypted_key_pharmacy = publicKey.encrypt_message(str(perscription.medicinesKey),pharmacy.public_key)
            #print(encrypted_key_pharmacy)

            encrypted_key_swd = publicKey.encrypt_message(str(perscription.leaveKey),swd.public_key)
            #print(encrypted_key_swd)
  
            sign_doc = ds.sign_prescription(doc.private_dsa_key,"prescriptionOriginal.txt")
            #print(sign_doc)
            ds.write_digital_sign("doctor_sign.txt",sign_doc)
            sign_pat = ds.sign_prescription(pat.private_dsa_key, "prescriptionOriginal.txt")
            #print(sign_pat)
            ds.write_digital_sign("patient_sign.txt",sign_pat)


            senderPharmacy = input("\nDo you want to send this document to Pharmacy?: ")

            if (senderPharmacy == "yes"):

                with open("PharmacyEncrypted.txt", 'w', encoding = 'utf-8') as f:
                    #f.seek(0)
                    f.write("Encrypted text: \n")
                    f.write(str(perscription.encryptedMedicines))
                    f.write("\nEncrypted key: \n")
                    f.write(str(encrypted_key_pharmacy))
                    f.write("\nDoctor's signature: \n")
                
                    f.write(str(ds.sign_prescription_string(doc.private_dsa_key, perscription.medicines)))
                    f.write("\nPatients's signature: \n")
                    f.write(str(ds.sign_prescription_string(pat.private_dsa_key, perscription.medicines)))

                    f.close()

                print("\nPharmacyEncrypted.txt ready to be sent to Pharmacy!")
                    

            
 


            senderSWD = input("\nDo you want to send this document to SWD?: ")

            if (senderSWD == "yes"):

                with open("SWDEncrypted.txt", 'w', encoding = 'utf-8') as f:
                    #f.seek(0)
                    f.write("Encrypted text: \n")
                    f.write(str(perscription.encryptedLeave))
                    f.write("\nEncrypted key: \n")
                    f.write(str(encrypted_key_swd))
                    f.write("\nDoctor's signature: \n")
                
                    f.write(str(ds.sign_prescription_string(doc.private_dsa_key, perscription.leave)))
                    f.write("\nPatients's signature: \n")
                    f.write(str(ds.sign_prescription_string(pat.private_dsa_key, perscription.leave)))

                    f.close()

                print("\nSWDEncrypted.txt ready to be sent to SWD!")
            
        elif(userType == '2'):
            print("Pharmacy")

            file = open("pharmacyEncrypted.txt",encoding='utf-8')
            content = file.readlines()

            pharmacy_encrypted_data = content[1]
            pharmacy_encrypted_key = content[3]

            #print(content[1][0])
            decrepytedPharmacyPrivateKey = publicKey.decrypt_message(pharmacy_encrypted_key, pharmacy.private_key)
            decryptedPharmacyText = aes.decrypt_str(pharmacy_encrypted_data, decrepytedPharmacyPrivateKey)

            print(ds.verify_signature_string(doc.public_dsa_key, decryptedPharmacyText, content[5]))

        elif(userType == 'w'):
            print("SWD")

            file = open("SWDEncrypted.txt",encoding='utf-8')
            content = file.readlines()

            swd_encrypted_data = content[1]
            swd_encrypted_key = content[3]

            #print(content[1][0])
            decrepytedswdPrivateKey = publicKey.decrypt_message(swd_encrypted_key, swd.private_key)
            decryptedswdText = aes.decrypt_str(swd_encrypted_data, decrepytedswdPrivateKey)

            print(ds.verify_signature_string(doc.public_dsa_key, decryptedswdText, content[5]))



        else:
            break



        



if __name__ == "__main__":
    main()





