def transformkey(key):
    temp = []
    for char in key:
        if char.isalpha() and char.upper() not in temp and char.upper() != 'J':
            temp.append(char.upper())
    for i in range(26):
        if i == ord('J')-ord('A') or chr(i+ord('A')) in temp:
            continue
        temp.append(chr(i+ord('A')))
    keytable = [[temp[i*5+j] for j in range(5)] for i in range(5)]
    return keytable

def getrc (char,table):
    for i in range(len(table)):
        for j in range(len(table[i])):
            if char == table[i][j]:
                return i,j

def transformpair (pair,encrypt,table):
    rp1,cp1 = getrc(pair[0],table)
    rp2,cp2 = getrc(pair[1],table)
    returnpair = ""
    if rp1==rp2:
        # same row
        returnpair += (table[rp1][(cp1 + (1 if encrypt else -1)) % len(table[rp1])])
        returnpair += (table[rp2][(cp2 + (1 if encrypt else -1)) % len(table[rp2])])
    elif cp1==cp2:
        # same col
        returnpair += (table[(rp1 + (1 if encrypt else -1)) % len(table)][cp1])
        returnpair += (table[(rp2 + (1 if encrypt else -1)) % len(table)][cp2])
    else:
        # diff row and col
        returnpair += (table[rp1][cp2] + table[rp2][cp1])
    return returnpair

def createpair (string):
    string = ''.join([char.upper() for char in string if char.isalpha()])
    string = string.replace('J','I')
    pair = []
    temp = ''
    for i in range(len(string)):
        if string[i]==temp: # duplicate
            temp += 'X'
            pair.append(temp)
            temp = string[i]
        else: # normal
            temp += string[i]

        if len(temp) == 2: # pair completed
            pair.append(temp)
            temp = ''
        elif i==len(string)-1 and len(temp)==1: # last alphabet dont have pair
            temp += 'X'
            pair.append(temp)
    # print(pair)
    return pair

def encrypt (p,k):
    p = createpair(p)
    k = transformkey(k)
    c = ""
    for pair in p:
        c += transformpair(pair,True,k)
    return c

def decrypt (c,k):
    c = createpair(c)
    k = transformkey(k)
    p = ""
    for pair in c:
        p += transformpair(pair,False,k)
    return p

if __name__ == "__main__":
    p = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque dapibus placerat diam blandit euismod. Morbi in ligula orci. Integer facilisis."
    k = "bluesky"
    print("plaintext  :",p,end='\n\n')
    c = encrypt(p,k)
    print("ciphertext :",c)
    print("plaintext  :",decrypt(c,k))