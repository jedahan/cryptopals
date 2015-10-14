from challenge5 import xor
import base64

def hamming(this, that):
  return sum([ bin(ord(l) ^ ord(that[i])).count('1') for i, l in enumerate(this) ])

def guess_keysize(encrypted):
  distances = [ hamming(encrypted[:i], encrypted[i:2*i])/i for i in range(1,40) ]
  return distances.index(min(distances))+1

def guess_string(encrypted, keysize):
  encrypted = [x for x in base64.b64decode(encrypted)]
  blocks = [[],[],[]]
  for i,byte in enumerate(encrypted):
    blocks[i % keysize].append(byte)

  key = "".join([ guess_key(block) for block in blocks ])
  print(key)
  decrypt_string(encrypted, key)

def decrypt_string(encrypted, key):
  decrypted = ""
  for i, num in enumerate(encrypted):
    decrypted = decrypted + chr(num ^ ord(key[i % len(key)]))
  print(decrypted)

def histogram_distance(this, that):
    distances = [ (percent - that[i]) ** 2 for i, percent in enumerate(this) ]
    return sum(distances)

def guess_key(block):
  best_key = None
  min_distance = float("Inf")
  # space, a, b, ..., y, z
  histogram = [ .1918, .0812, .0149, .0271, .0432, .1202, .0230, .0203, .0592, .0731, .0010, .0069, .0398, .0261, .0695, .0768, .0182, .0011, .0602, .0628, .0910, .0288, .0111, .0209, .0017, .0211, .0007 ]

  for possible_key in range(255):
    hist = [ 0 for _ in range(27) ]
    for number in block:
      try:
        char = chr(possible_key ^ number).lower()
        index = ord(char) - ord('a') + 1
        if char == ' ': index = 0
        hist[index] = hist[index] + 1
      except:
        next
    # normalize histogram
    hist = [ n/len(block) for n in hist ]
    distance = histogram_distance(histogram, hist)
    if distance < min_distance:
      best_key = possible_key
      min_distance = distance
  print(best_key, min_distance)
  return chr(best_key)

if __name__ == "__main__":
  distance = hamming("this is a test", "wokka wokka!!!")
  encrypted = open('input/6.txt').read().strip()
  assert( distance == 37 )

  keysize = guess_keysize(encrypted)
  decrypted = guess_string(encrypted, keysize)
  print(decrypted)
