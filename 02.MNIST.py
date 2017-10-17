import gzip # open gzip file



# This function reads labels from a specified file
def read_labels_from_file(filename):
    with gzip.open(filename, 'rb') as f: 
        magic = f.read(4) 
        magic = int.from_bytes(magic, 'big') 
        print("Magic is: ", magic) #  should be 2049.

        nolab = f.read(4) # Read the next 4 bytes to get the number of labels.
        nolab = int.from_bytes(nolab, 'big') 
        print("Number of labels: ", nolab) 

# This function reads images from a specified file
def read_images_from_file(filename):
    with gzip.open(filename, 'rb') as f: 
        magic = f.read(4) 
        magic = int.from_bytes(magic, 'big') 
        print("Magic is: ", magic) 

        noimg = f.read(4) 
        noimg = int.from_bytes(noimg, 'big')
        print("Number of images: ", noimg) 

        nocol = f.read(4) # Read the next 4 bytes to get the number of columns.
        nocol = int.from_bytes(nocol, 'big') 
        print("Number of column: ", nocol)

        # Read the next 4 bytes to get the number of rows.
        norow = f.read(4) 
        norow = int.from_bytes(norow, 'big') 
        print("Number of labels: ", norow) 

        images = [] # Image the [] represents an array 
        # Loop through all images
        for i in range(noimg):
            row = []
            for r in range(norow):
                cols = []
                for c in range(nocol):
                    cols.append(int.from_bytes(f.read(1), 'big'))
                row.append(cols)
            images.append(row)

        return images 

# Function to print out an image to the console
def print_out_image(image_array):
    for row in image_array:
        for col in row:
            print("." if col <= 127 else "#", end="")
        print()


train_images = read_images_from_file("data/train-images-idx3-ubyte.gz")
print_out_image(train_images[2])