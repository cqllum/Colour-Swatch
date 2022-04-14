#!/usr/bin/env python
# coding: utf-8

# # Gather Swatch Hex Colour of Images
# Using this script, you are able to gather the Hex Colour code for images by providing only the URL of the image.
# 
# # Purpose?
# If you sell goods on a website, you can generate bulk swatch colours in seconds.
# 
# # How accurate is it?
# This script allows you to declare how many snapshots to take of random coordinates on the image - the more snapshots, the better.

# In[199]:


## Imports 
from PIL import Image
import requests
import random


# After declaring the imports, add functions to make calculations later on.

# In[200]:


# Get the average of a list
def get_average(ds):
    return sum(ds) / len(ds)

# Convert RGB to HEX code format
def rgbhex(rgb):
        return '#%02x%02x%02x' % rgb


# Next, load the main function that will be gathering the data for processing.

# In[201]:


# Load and gather image hex from URL
def get_image(url, snaps = 5):
    
    # Prepare arrays for multiple data retrieval
    xr = []
    xg = []
    xb = []
    
    # Request and stream URL, then open raw data via PIL
    im = Image.open(requests.get(url, stream=True).raw)
    
    # convert image to RGB
    rgb_im = im.convert('RGB')

    # Get the size of image
    dims = im.size

    # Declare coordinates based on x and y axis
    x = dims[0]
    y = dims[1]
    
    # Loop through snapshots provided by function
    for snap in range(snaps):
        
            # Calculate random coordinates to get colour for (accuracy)
            xaxis = int(x) / random.randint(2, 5)
            yaxis = int(y) / random.randint(2, 5)
            
            # Get the RGB of calculated pixel
            ds = rgb_im.getpixel((int(xaxis), int(yaxis)))
            
            # Push each coordinate into list
            xr.append(ds[0])
            xg.append(ds[1])
            xb.append(ds[2])
        
    # Get the average R,G,B values based on snapshots
    swatch = int(get_average(xr)),  int(get_average(xg)),  int(get_average(xb))
    
    # Get hex colour for RGB
    return "snaps", snaps, rgbhex(swatch)


# Then finally, execute the given code to gather the perfect hex colour.

# In[206]:


# Image URL
url = "https://www.clker.com/cliparts/C/H/o/A/i/k/pink-shirt-hi.png"

# How many snap shots should be captured of the hex colours? The higher, the better.
snapshots = 25

print(get_image(url, snapshots))


# The results of 25 snapshots grouped together, produces #e59cc0 (pink) for an image of a pink shirt.

# # Do you have multiple images to iterate through?
# Not an issue! You can simply loop through your images, and produce hex colours for your entire list.

# In[213]:


images = [
    "https://www.clker.com/cliparts/C/H/o/A/i/k/pink-shirt-hi.png",
    "https://wallpapertops.com/walldb/original/8/a/f/123350.jpg",
    "https://wallpapercave.com/wp/wp2466652.jpg"
]

for image in images:
    print(get_image(image, snapshots), image)


# # Other uses:
# If you own a website, you're able to reprogram this script to gather hex colours for every image on your website, desktop, shared area.

# ~~ github/cqllum
