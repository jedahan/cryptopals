import base64
from challenge1 import hex264

def xor(cryp, key):
  crypt = hex264(cryp)
  key = hex264(key)
  if(len(key)==1):
    return bytes([ crypt[i] ^ key for i in range(len(crypt)) ])
  else:
    return bytes([ crypt[i] ^ key[i] for i in range(len(crypt)) ])

if __name__ == "__main__":
  decoded = xor('1c0111001f010100061a024b53535009181c', '686974207468652062756c6c277320657965').decode('utf-8')
  assert(decoded == "the kid don't play")
  print(decoded)
