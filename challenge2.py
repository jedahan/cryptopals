import base64
from challenge1 import hex264

# Expects cryp and key to be a hex string, returns a byte string/byte array
def xor(encrypted, key):
  encrypted = hex264(encrypted)
  key = hex264(key)
  return bytes([ encrypted[i] ^ key[i % len(key)] for i in range(len(encrypted)) ])

if __name__ == "__main__":
  decoded = xor('1c0111001f010100061a024b53535009181c', '686974207468652062756c6c277320657965').decode('utf-8')
  assert(decoded == "the kid don't play")
  print(decoded)
