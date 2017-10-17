import gzip
import numpy as np


def read_labels_from_file(filename):
    # open the provided file with gzip
    with gzip.open(filename, 'rb') as f:
        # Read the first byte which should be the magic number
        magic = f.read(4)
        magic = int.from_bytes(magic, 'big')
        print("The Magic number is:", magic)
        
        # Read the next byte which will be the number of labels
        nolab = f.read(4)
        nolab = int.from_bytes(nolab, 'big')
        print("Number of labels:", nolab)
        #Fill the labels list with bytes and then parse the bytes
        labels = [f.read(1) for i in range(nolab)]
        labels = [int.from_bytes(label, 'big') for label in labels]
    
    return labels
#The training sets we will be using
train_labels = read_labels_from_file('data/train-labels-idx1-ubyte.gz')
test_labels = read_labels_from_file('data/t10k-labels-idx1-ubyte.gz')

train_images = read_images_from_file('data/train-images-idx3-ubyte.gz')
test_images = read_images_from_file('data/t10k-images-idx3-ubyte.gz')


for img in train_images:
    
    for row in img:
        #
        for col in row:
           
            try:
                print('.' if col <= 127 else '#', end = '.')
            except TypeError as err:
                print('.', end = '.')

        print() # New line to break up imgs

import PIL.Image as pil #Import Python Image Library
img = pil.fromarray(np.array(train_images[5]).astype('uint8')) #Astype used to set encoding
img = img.convert('RGB') 
img.show() #Open the file
img.save(str(5)+'.png') # Save the file