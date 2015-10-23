from challenge5 import xor
from challenge3 import guess_single_key
import base64
from Crypto.Cipher import AES

def decrypt(encrypted, key):
  decrypted = ""
  for i, num in enumerate(encrypted):
    decrypted = decrypted + chr(num ^ ord(key[i % len(key)]))
  return decrypted

if __name__ == "__main__":
  encrypted = bytes([x for x in base64.b64decode(open('input/7.txt').read())])

  key = b'YELLOW SUBMARINE'
  print("using key %r" % key)
  cipher = AES.new(key, AES.MODE_ECB)

  decrypted = cipher.decrypt(encrypted)
  print(decrypted.decode("utf-8"))
