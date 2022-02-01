import os
import codecs
from pylibscrypt import scrypt
message = input("Type your message to be encrypted... \n")
message = bytes(message, "utf8")
secret_key = input("Type your secret key... \n")
secret_key = bytes(secret_key, "utf8")
hashed = scrypt(secret_key, message, 2 ** 15, 8, 1, 32)
res = codecs.encode(hashed, 'hex').decode('utf-8')[:32]
res = "!A" + res[:-2]
print(res)
