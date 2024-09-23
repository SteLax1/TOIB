from os import read, write
import hashlib

class SHA256Decoder(object):
    def sha256(self):
        password = input("Ââåäèòå ïàðîëü: ")
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        print("Õýø ïàðîëÿ:"+hashed_password)


x=SHA256Decoder()
x.sha256()

