import base64
from challenge2 import xor

# word is actually a byte array
def score(word):
  # from http://www.data-compression.com/english.html
  frequencies = {
    ' ': .1918,
    'e': .1202,
    't': .0910,
    'a': .0812,
    'o': .0768,
    'i': .0731,
    'n': .0695,
    's': .0628,
    'r': .0602,
    'h': .0592,
    'd': .0432,
    'l': .0398,
    'u': .0288,
    'c': .0271,
    'm': .0261,
    'f': .0230,
    'y': .0211,
    'w': .0209,
    'g': .0203,
    'p': .0182,
    'b': .0149,
    'v': .0111,
    'k': .0069,
    'x': .0017,
    'q': .0011,
    'j': .0010,
    'z': .0007,
   }
  score = 0
  for letter, percent in frequencies.items():
    score = score + percent * (word.count(ord(letter)) + word.count(ord(letter.upper())))
  score = score - word.count(ord(' ')) * frequencies[' ']
  return score

def decrypt(encrypted_bytes, key):
  decrypted = ""
  for byte in encrypted_bytes:
    decrypted = decrypted + chr(byte ^ ord(key))
  return decrypted

def guess_single_key(encrypted_bytes):
  best_score = 0
  best_key = None
  for n in range(255):
    this_score = score(xor(encrypted_bytes, [n]))
    if this_score > best_score:
      best_score = this_score
      best_key = chr(n)

  return best_key

def find_best_string(encrypted):
  encrypted = [x for x in base64.b16decode(encrypted, True)]
  key = guess_single_key(encrypted)
  decrypted = decrypt(encrypted, key)
  return (key, decrypted)

if __name__ == "__main__":
  key, decrypted = find_best_string("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736")
  assert(decrypted == "Cooking MC's like a pound of bacon")
  print(key, decrypted)
