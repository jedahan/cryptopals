import base64
from challenge3 import find_best_string, score

if __name__ == "__main__":
  lines = [line.strip() for line in open('4.txt').readlines()]
  strings = [find_best_string(line) for line in lines]
  print(strings)
