import base64

def xor(cryp, key):
  crypt = base64.b16decode(cryp, True)
  key = base64.b16decode(key, True)
  print(key)
  return bytes([ crypt[i] ^ key[i] for i in range(len(crypt)) ])

xord = xor(b'1c0111001f010100061a024b53535009181c', b'686974207468652062756c6c277320657965')

print(xord)
