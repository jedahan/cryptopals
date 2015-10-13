def xor(line, key):
  encrypt = ""
  for i,char in enumerate(line):
    xord = hex(ord(line[i]) ^ ord(key[i % len(key)]))[2:]
    if len(xord) == 1: xord = "0" + xord
    encrypt = encrypt + xord
  return encrypt

if __name__ == "__main__":
  encrypted = xor("""Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal""","ICE")
  assert(encrypted == "0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f")
  print(encrypted)
