import base64

def hex264(hex_string):
  return base64.b16decode(hex_string, True)

if __name__ == "__main__":
  decoded = hex264('49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d').decode('utf-8')
  assert(decoded == "I'm killing your brain like a poisonous mushroom")
  print(decoded)
