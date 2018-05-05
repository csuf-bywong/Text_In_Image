Author: Belinda Wong

DESCRIPTION
decode.py decodes a message within a picture.  Message will be output to the command line.
encode.py takes an image and a text file's contents, putting the text into an image.  You need to supply a name for the image outputted.
Utilizes python3 and python pillow library.

EXECUTION
python3 decode.py <image-file>
example: python3 decode.py testImage.png

python3 encode.py <image-file> <text-file> <output-image-name>
example: python3 encode.py testImage.png encode.txt change.png

OTHER FILES
-testImage.png is the unaltered image provided by the professor.
-change.png was one of the output images created by encode.py
-test.png is also an output image created by encode.py
-encode.txt is a text file supplied in testing encode.py.  Contents in the text file are the same as encode.py.
