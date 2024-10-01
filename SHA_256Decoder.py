import hashlib


class SHA256Decoder(object):
    def decodeSha256(password):
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        return hashed_password;

decoder=SHA256Decoder
print("To end the program enter exit\n")
while True: 
    password = input("Enter password: ")
    if password == "exit":
        break
    hashed_password = decoder.decodeSha256(password) 
    print(f"Hashed password: {hashed_password}\n")

