import random

def generate_vig_table():
    row = [chr(ord('A')+i) for i in range(26)]
    random.shuffle(row)
    with open('./table/VigenereFullTable.txt',mode='w') as f:
        for i in range(len(row)):
            f.write(row[i])
            if i<len(row)-1:
                f.write(' ')

def read_vig_table(filename):
    table = [[] for i in range(26)]
    with open(filename,mode='r') as f:
        code = f.read().split(' ')
        for i in range(26):
            table[i] = code[i:] + code[:i]
        return table

def encrypt (p,k,filename='./table/VigenereFullTable.txt'):
    p = ''.join([char.upper() for char in p if char.isalpha()])
    k = ''.join([char.upper() for char in k if char.isalpha()])
    vig_code = read_vig_table(filename)
    c = ""
    for i in range(len(p)):
        pi = ord(p[i]) - ord('A')
        ki = ord(k[i % len(k)]) - ord('A')
        c += vig_code[pi][ki]
    return c

def decrypt (c,k,filename='./table/VigenereFullTable.txt'):
    c = ''.join([char.upper() for char in c if char.isalpha()])
    k = ''.join([char.upper() for char in k if char.isalpha()])
    vig_code = read_vig_table(filename)
    p = ""
    for i in range(len(c)):
        ki = ord(k[i % len(k)]) - ord('A')
        p += chr(vig_code[ki].index(c[i]) + ord('A'))
    return p

if __name__ == "__main__":
    p = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque dapibus placerat diam blandit euismod. Morbi in ligula orci. Integer facilisis."
    print("plaintext       :",p,end='\n\n')
    k = "bluesky"
    c = encrypt(p,k,'./File/VigenereTableCode.txt')
    print("ciphertext full :",c)
    print("plaintext full  :",decrypt(c,k,'./File/VigenereTableCode.txt'))