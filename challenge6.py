def hamming(this, that):
  return sum([ bin(ord(l) ^ ord(that[i])).count('1') for i, l in enumerate(this) ])

def check_key(encrypted, key):
  return false

if __name__ == "__main__":
  distance = hamming("this is a test", "wokka wokka!!!")
  assert( distance == 37 )
  print(distance)
