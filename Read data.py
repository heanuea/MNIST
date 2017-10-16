import gzip

f=gzip.open('C:\Users\heanu\Desktop\Minst/train-images-idx3-ubyte.gz', 'rb')

# firstbyte = f.read(1)
# print(firstbyte)

magicNumber = f.read(4)
print(magicNumber)

print(int.from_bytes(magicNumber, byteorder='big'))


f.close()