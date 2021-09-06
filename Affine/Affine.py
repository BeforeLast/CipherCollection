def encrypt (p,m,b):
    p = ''.join([char.upper() for char in p if char.isalpha()])
    c = ""

    n = 26 # alphabet count

    for char in p:
        pi = ord(char) - ord('A')
        aff = ((m*pi) + b) % n
        c += chr(aff + ord('A'))
    return c

def decrypt (c,m,b):
    c = ''.join([char.upper() for char in c if char.isalpha()])
    p = ""

    n = 26 # alphabet count

    for char in c:
        ci = ord(char)-ord('A')
        minv = pow(m,-1,n)
        aff = minv*(ci-b) % n
        p += chr(aff + ord('A'))
    return p

if __name__ == "__main__":
    p = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque dapibus placerat diam blandit euismod. Morbi in ligula orci. Integer facilisis."
    print("plaintext  :",p,end='\n\n')
    c = encrypt(p,7,10)
    print("ciphertext :",c)
    print("plaintext  :",decrypt(c,7,10))