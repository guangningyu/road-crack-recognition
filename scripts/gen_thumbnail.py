import os, sys
from PIL import Image

size = (960, 540)

for infile in sys.argv[1:]:
    outfile = os.path.splitext(infile)[0] + "_thumbnail.JPG"
    if infile != outfile:
        try:
            im = Image.open(infile)
            im.thumbnail(size)
            im.save(outfile, "JPEG")
        except IOError:
            print("cannot create thumbnail for", infile)
