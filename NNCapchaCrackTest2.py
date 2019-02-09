from PIL import Image
from scipy import misc
import matplotlib.pyplot as plt
import  numpy as np
from scipy import ndimage


f = misc.face()
misc.imsave('face.jpg', f) # uses the Image module (PIL)

face = misc.imread('face.png')
type(face)

face.shape, face.dtype


face.tofile('face.raw') # Create raw file
face_from_raw = np.fromfile('face.raw', dtype=np.uint8)
face_from_raw.shape

face_from_raw.shape = (768, 1024, 3)

n = 10
l = 256
im = np.zeros((l, l))
np.random.seed(1)
points = l*np.random.random((2, n**2))
im[(points[0]).astype(np.int), (points[1]).astype(np.int)] = 1
im = ndimage.gaussian_filter(im, sigma=l/(4.*n))

mask = (im > im.mean()).astype(np.float)
mask += 0.1 * im
img = mask + 0.2*np.random.randn(*mask.shape)
# plt.imshow(img)
# plt.show()


hist, bin_edges = np.histogram(img, bins=60)
bin_centers = 0.5*(bin_edges[:-1] + bin_edges[1:])

binary_img = img > 0.5


# plt.imshow(binary_img)
# plt.show()



