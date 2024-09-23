from os import read, write
import hashlib

class my_class(object):
    def sha256(self):
        password = input("Введите пароль: ")
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        print("Хэш пароля:"+hashed_password)


x=my_class()
x.sha256()

