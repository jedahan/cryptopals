import base64
from challenge1 import hex264

# Expects cryp and key to be an array of bytes, returns a byte string/byte array
def xor(encrypted, key):
  return bytes([ encrypted[i] ^ key[i % len(key)] for i in range(len(encrypted)) ])

if __name__ == "__main__":
  encrypted = hex264('1c0111001f010100061a024b53535009181c')
  key = hex264('686974207468652062756c6c277320657965')
  decoded = xor(encrypted, key).decode('utf-8')
  assert(decoded == "the kid don't play")
  print(decoded)
