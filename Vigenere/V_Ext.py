import os

def encrypt (in_file,out_file,k):
    filelength = os.path.getsize(in_file)
    rb = open(in_file,mode='rb')
    wb = open('./output/'+out_file,mode='wb')
    for i in range(filelength):
        rb.seek(0,1)
        plain_byte_value = int.from_bytes(rb.read(1),'little',signed=False)
        encrypted_byte_value = (plain_byte_value + ord(k[i % len(k)])) % 256
        byte = encrypted_byte_value.to_bytes(1,'little')
        wb.seek(0,1)
        wb.write(byte)

def decrypt (in_file,out_file,k):
    filelength = os.path.getsize(in_file)
    rb = open(in_file,mode='rb')
    wb = open('./output/'+out_file,mode='wb')
    for i in range(filelength):
        rb.seek(0,1)
        plain_byte_value = int.from_bytes(rb.read(1),'little',signed=False)
        encrypted_byte_value = (plain_byte_value - ord(k[i % len(k)])) % 256
        byte = encrypted_byte_value.to_bytes(1,'little')
        wb.seek(0,1)
        wb.write(byte)

if __name__ == "__main__":
    encrypt('./File/A','./File/A-e','bluesky')
    decrypt('./File/A-e','./File/A-d','bluesky')