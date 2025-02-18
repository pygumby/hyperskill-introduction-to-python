import argparse

# Insert your decode_Caesar_cipher function here
def decode_caesar_cipher(s, n):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',.?!"
    s = s.strip()
    text = ''
    for c in s:
        text += alpha[(alpha.index(c) + n) % len(alpha)]
    print(text)

# Write your parser here
parser = argparse.ArgumentParser()

parser.add_argument("-w", "--word")
parser.add_argument("-o", "--offset")

args = parser.parse_args()

decode_caesar_cipher(args.word, -int(args.offset))
