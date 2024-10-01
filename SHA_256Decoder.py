import hashlib


class SHA256Decoder(object):
    def decodeSha256(password):
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        return hashed_password;

decoder=SHA256Decoder
password = input("Enter password: ")
hashed_password = decoder.decodeSha256(password) 
print(f"Hashed password: {hashed_password}")

