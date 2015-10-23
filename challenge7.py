from challenge5 import xor
from challenge3 import guess_single_key
import base64
from Crypto.Cipher import AES

def decrypt(encrypted, key):
  cipher = AES.new(key, AES.MODE_ECB)
  decrypted_bytes = bytes(cipher.decrypt(encrypted))
  return decrypted_bytes.decode("utf-8")

if __name__ == "__main__":
  encrypted = bytes([x for x in base64.b64decode(open('input/7.txt').read())])

  key = b'YELLOW SUBMARINE'
  print("using key %r" % key)

  decrypted = decrypt(encrypted, key)
  print(decrypted)
