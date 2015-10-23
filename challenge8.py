import base64

if __name__ == "__main__":
    for line in open('input/8.txt').readlines():
        encrypted = [x for x in base64.b64decode(line.strip())]
        # no matter what the key is, for ecb, the block is always 16 bytes!
        ecb_size = 16
        blocks = [tuple(encrypted[ecb_size*i:ecb_size*(i+1)]) for i in range(int(len(encrypted)/ecb_size))]
        if len(blocks) != len(set(blocks)):
            print(encrypted)
