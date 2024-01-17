from Crypto.Cipher import AES

with open('key.bin', 'rb') as f:
    key = f.read()

cipher = AES.new(key, AES.MODE_EAX)

with open('sample_data.txt', 'rb') as f:
    data = f.read()

ciphertext, tag = cipher.encrypt_and_digest(data)

file_out = open("encrypted.bin", "wb")
[file_out.write(x) for x in (cipher.nonce, tag, ciphertext)]
file_out.close()
