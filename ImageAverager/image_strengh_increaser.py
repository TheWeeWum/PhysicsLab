import os, numpy, PIL
from PIL import Image

subpath = "\\ImageAverager\\images"
subpath2 = "ImageAverager\\images\\"
savepath = "\\ImageAverager\\postEditedImages\\"

factor_of_increase = 2

# Access all PNG files in directory
allfiles=os.listdir(os.getcwd() + subpath)
print(allfiles)

imlist=[filename for filename in allfiles if  (filename[-4:] in [".png",".PNG"] or filename[-5:] == ".jpeg")]
print(imlist)


for im in imlist:
    w,h=Image.open(subpath2 + imlist[0]).size
    imarr=numpy.array(Image.open(subpath2 + im),dtype=float)
    
    arr=(imarr * factor_of_increase).clip(0, 255)

    # Round values in array and cast as 8-bit integer
    arr=numpy.array(numpy.round(arr),dtype=numpy.uint8)

    # Generate, save and preview final image
    out=Image.fromarray(arr,mode="RGB")
    out.save("Doubled.png")