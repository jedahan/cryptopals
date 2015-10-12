import base64
from challenge2 import xor

def score(word):
  word = word.lower()
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
  for letter in frequencies:
    score = score + (frequencies[letter] * word.count(letter))
  return score

def find_best_string(string):
  words = [ xor(string, chr(n)) for n in range(ord('A'),ord('z')) ]

  scores = [ score(word) for word in words ]

  return words[scores.index(max(scores))]

if __name__ == "__main__":
  print(find_best_string("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"))
  lines = [line.strip() for line in open('input/3.txt').readlines()]
  strings = [find_best_string(line) for line in lines]
  print(strings)
