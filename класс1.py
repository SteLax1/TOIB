from os import read, write
import hashlib

class my_class(object):
    def sha256(self):
        password = input("������� ������: ")
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        print("��� ������:"+hashed_password)


x=my_class()
x.sha256()

