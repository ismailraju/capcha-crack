from scipy import misc
import numpy as np
from PIL import Image
import glob
import re

input=[]
output=[]
map=[]
outArray=[]
count=0;

for image_path in sorted(glob.glob("dataSet/*.png")):
    image = misc.imread(image_path,'L')
    # print image.shape
    # print image.dtype
    print image_path
    # print  image_path.split("/")[-1].split(".")[0]
    output.append(str(  image_path.split("/")[-1].split(".")[0]))

    arr = np.array(image).astype(int)
    arr[arr == 0] = int(1)
    arr[arr == 255] = 0

    # print arr

    flat_arr = arr.ravel()
    # print flat_arr
    input.append(flat_arr )
    map.append(count)
    x = [0] * 36
    x[count] = 1
    outArray.append(x)
    count=count+1

    vector = np.matrix(flat_arr)
    # print vector
# print input
# print output
# print map

print outArray




img = Image.open('dataSet/B.png').convert('L')
arr = np.array(img)
# print arr

# record the original shape
shape = arr.shape
# print shape

# make a 1-dimensional view of arr
flat_arr = arr.ravel()
# print flat_arr

# convert it to a matrix
vector = np.matrix(flat_arr)

# do something to the vector
vector[:,::10] = 128

# reform a numpy array of the original shape
arr2 = np.asarray(vector).reshape(shape)

# make a PIL image
# img2 = Image.fromarray(arr2, 'RGBA')
# img2.show()
