import rsa
message = input("Enter your message to be encrypted... \n")
publicKey, privateKey = rsa.newkeys(2048)
pub = rsa.PublicKey.save_pkcs1(publicKey)
pri = rsa.PrivateKey.save_pkcs1(privateKey)
with open('pubkey.pem', 'w') as f:
    f.write(pub.decode("utf-8"))
with open('privkey.pem', 'w') as f:
    f.write(pri.decode("utf-8"))
ciphertext = rsa.encrypt(message.encode(), publicKey)
print("Writing ciphertext to file... \n")
with open('cypertext', 'wb') as f:
    f.write(ciphertext)
