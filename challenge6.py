from challenge5 import xor
from challenge3 import guess_single_key
import base64

# expects two lists of bytes
def hamming(this, that):
  return sum([ bin(l ^ that[i]).count('1') for i, l in enumerate(this) ])

def guess_keysize(encrypted):
  distances = []
  for i in range(2,41):
    chunks = int((len(encrypted)-i)/i)
    some_distance = [ hamming(encrypted[l*i:(l+1)*i], encrypted[(l+1)*i:(l+2)*i])/chunks for l in range(chunks) ]
    distances.append(sum(some_distance)/i)

  # this is not returning the right thing, it should return something like 37...
  return distances.index(min(distances))+2

# expects encrypted to be bytes
def guess_key(encrypted, keysize):
  blocks = [[] for _ in range(keysize)]
  for i,byte in enumerate(encrypted):
    blocks[i % keysize].append(byte)

  return "".join([ guess_single_key(block) for block in blocks ])

def decrypt(encrypted, key):
  decrypted = ""
  for i, num in enumerate(encrypted):
    decrypted = decrypted + chr(num ^ ord(key[i % len(key)]))
  return decrypted

def str2bytes(string):
    return [ord(x) for x in string]

if __name__ == "__main__":
  assert(hamming(str2bytes("this is a test"),str2bytes("wokka wokka!!!"))==37)
  encrypted = [x for x in base64.b64decode(open('input/6.txt').read().strip())]

  keysize = guess_keysize(encrypted)
  print("keysize is maybe %s" % keysize)
  key = guess_key(encrypted, keysize)
  print("key is maybe %r" % key)
  decrypted = decrypt(encrypted, key)
  print(decrypted)
