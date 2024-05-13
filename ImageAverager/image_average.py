import os, numpy, PIL
from PIL import Image

subpath = "\\ImageAverager\\images"
subpath2 = "ImageAverager\\images\\"
savepath = "\\ImageAverager\\postEditedImages\\"

# Access all PNG files in directory
allfiles=os.listdir(os.getcwd() + subpath)
print(allfiles)

imlist=[filename for filename in allfiles if  (filename[-4:] in [".png",".PNG"] or filename[-5:] == ".jpeg")]
print(imlist)

# Assuming all images are the same size, get dimensions of first image
w,h=Image.open(subpath2 + imlist[0]).size
N=len(imlist)

# Create a numpy array of floats to store the average (assume RGB images)
arr=numpy.zeros((h,w,3),dtype=float)

# Build up average pixel intensities, casting each image as an array of floats
for im in imlist:
    imarr=numpy.array(Image.open(subpath2 + im),dtype=float)
    arr=arr+imarr/N

# Round values in array and cast as 8-bit integer
arr=numpy.array(numpy.round(arr),dtype=numpy.uint8)

# Generate, save and preview final image
out=Image.fromarray(arr,mode="RGB")
out.save(savepath + "Average.png")
out.show()