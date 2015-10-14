import base64
from challenge3 import find_best_string, score

if __name__ == "__main__":
  lines = [line.strip() for line in open('input/4.txt').readlines()]
  strings = [find_best_string(line) or '' for line in lines]
  scores = [score([x for x in bytes(string,'utf8')]) for string in strings]
  best = strings[scores.index(max(scores))].strip()
  assert(best == "Now that the party is jumping")
  print(best)
