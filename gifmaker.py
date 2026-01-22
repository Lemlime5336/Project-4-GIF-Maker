#v3 as we are using version 3 of the library
#as allows to alias the library to make coding easier
import imageio.v3 as iio

#list for locations of the image files
filenames = ['1.png','2.png','3.png']
#empty list to store actual image data from the files
images = []

#for loop to go through filepaths and read images using imageio library's imread()
#imread loads an image based on filepath, so images variable has all images
for filename in filenames:
    images.append(iio.imread(filename))

#use imwrite() to turn the images into a GIF
#takes in 4 arguments:
#   1. name of the gif
#   2. list containing the image data
#   3. how long each picture is shown
#   4. how many times the GIF repeats 0 = infinity
iio.imwrite('faces.gif', images, duration=500, loop=0)
