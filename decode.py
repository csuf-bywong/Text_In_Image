from PIL import Image
import sys #for command line args
import math #for ceil fcn

def main():
    path = sys.argv[1] #path to image file
    img = Image.open(path) #open the file

    width, height = img.size #width, height in pixels from PIL lib
    col = width - 1 #indexes start at 0
    row = height - 1

    msgSize = getBinary(img, width, col, row) #extract the binary from the first 11 pixels
    msgSize = msgSize[:32] #only gets the 32 bytes needed to tell us size of msg
    msgSize = int(msgSize, 2) #converts the size of msg from binary to integer type

    col = width - 12 #start from the 12th pixel
    pixelAmt = math.ceil(msgSize/3) #msgSize=bytes of msg, 3 bytes = 1 RGB = 1 pixel
    msg = getBinary(img, width, col, row, pixelAmt)
    msg = msg[:msgSize] #only gets the bytes with the msg in them
    decodedMsg = ''.join(chr(int(msg[i:i+8],2)) for i in range(0, len(msg),8)) #range is from beginning to end of msg in steps of 8
    #chr(int()) converts 8 bits of binary into a single char and joins it to decodedMsg
    print('decoded message is: \n' , decodedMsg)

def getBinary(img, width, col, row, lastPixel = 11):
    binaryNum = ''
    pix = img.load() #get all the pixels of the image
    for i in range(int(lastPixel)): #for some reason it's reading lastPixel as a float
        r, g, b = pix[col,row] #gives back something like (x,y,z)
        binaryNum += str(bin(r))[-1] #the pixels returned are ints and we want the last num of the binary form
        binaryNum += str(bin(g))[-1] #concatenate them to binaryNum
        binaryNum += str(bin(b))[-1]
        if col == 0:
            col = width
            row = row -1
        col = col -1
    return binaryNum

if __name__ == '__main__':
    main()
