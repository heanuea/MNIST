import gzip

f=gzip.open('C:\Users\heanu\Desktop\Minst/train-images-idx3-ubyte.gz', 'rb')

# firstbyte = f.read(1)
# print(firstbyte)

magicNumber = f.read(4)
print(magicNumber)

print(int.from_bytes(magicNumber, byteorder='big'))


f.close()



# couldnt get the first working on this klaptop but i did on the other so i went with this solution 
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image

from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("MNIST_data", one_hot=True)