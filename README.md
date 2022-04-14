# Colour-Swatch | Image to Hex Code
Get the hex colour of any image simply by providing the URL of the image.

# Initial Prerequisites 
`Python` - Downloadable here: https://www.python.org/downloads/

# Python Requirements 
`requests` package - installable via python `pip install requests`

`PIL` package - installable via python `pip install Pillow`


# Usage guide
Provide the number of `snapshots` - the more the better
Supply the `URL` of the `image` you would like to get the hex colour for.

# Function to retrieve data

```
# The image URL
image = "https://www.clker.com/cliparts/C/H/o/A/i/k/pink-shirt-hi.png"

# The number of snapshots to take of the image
snapshots = 25

# Function to gather data
get_image(image, snapshots)
```
