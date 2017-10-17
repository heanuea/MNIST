# MNIST

### **_What is MNIST_**

 
The MNIST database of handwritten digits, available from this page, has a training set of 60,000 examples, and a test set of 10,000 examples. It is a subset of a larger set available from NIST. The digits have been size-normalized and centered in a fixed-size image.
It is a good database for people who want to try learning techniques and pattern recognition methods on real-world data while spending minimal efforts on preprocessing and formatting.


## 1. Read the data files
Download the image and label files.
Have Python decompress and read them byte by byte into appropriate data structures in memory.


## 2. Output an image to the console
Output the third image in the training set to the console.
Do this by representing any pixel value less than 128 as a full stop and any other pixel value as a hash symbol.


## 3. Output the image files as PNGs
Use Python to output the image files as PNGs, saving them in a subfolder in your repository.
Name the images in the format `train-XXXXX-Y.png` or `test-XXXXX-Y.png` where `XXXXX` is the image number (where it occurs in the data file) and `Y` is its label.
For instance, the five-thousandth training image is labelled 2, so its file name should be `train-04999-2.png`.
Note the images are indexed from 0, so the five-thousandth image is indexed as 4999.
See below for an example of it.
Commit these image files to GitHub.

![5000th training image labelled 2](../images/05000-2.png)
