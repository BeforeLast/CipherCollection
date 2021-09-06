def encrypt (p,k):
    p = ''.join([char.upper() for char in p if char.isalpha()])
    k = ''.join([char.upper() for char in k if char.isalpha()])
    c = ""
    for i in range(len(p)):
        pi = ord(p[i]) - ord('A')
        ki = ord(k[i % len(k)]) - ord('A')
        vig = (pi + ki) % 26
        c += chr(vig + ord('A'))
    return c

def decrypt (c,k):
    c = ''.join([char.upper() for char in c if char.isalpha()])
    k = ''.join([char.upper() for char in k if char.isalpha()])
    p = ""
    for i in range(len(c)):
        ci = ord(c[i]) - ord('A')
        ki = ord(k[i % len(k)]) - ord('A')
        vig = (ci - ki) % 26
        p += chr(vig + ord('A'))
    return p

if __name__ == "__main__":
    p = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque dapibus placerat diam blandit euismod. Morbi in ligula orci. Integer facilisis."
    k = "bluesky"
    print("plaintext  :",p,end='\n\n')
    c = encrypt(p,k)
    print("ciphertext :",c)
    print("plaintext  :",decrypt(c,k))