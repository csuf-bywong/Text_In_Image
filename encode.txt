from PIL import Image
import sys
import math

def main():
    inImage = sys.argv[1] #img that is consumed
    inFile = sys.argv[2] #txt file that is the msg
    outImg = sys.argv[3] #img that is produced

    file = open(inFile)
    msg = file.read() #get the text from the txt file and assign it to msg
    file.close()
    img = Image.open(inImage) #open the img to be consumed
    encode(msg, img, outImg) #write msg
    img.save(outImg, 'PNG') #save as a separate image

def encode(msg, img, output):
    width, height = img.size #width, height in pixels from PIL lib
    col = width-1 #indexes start at 0
    row = height-1

    msgLength = len(msg) * 8 #we wanna convert the msg length to total bytes
    print ('msg length = ', msgLength, 'bytes')
    binaryMsgLength = str(bin(msgLength)) #this gives binary with 0b....
    binaryMsgLength = binaryMsgLength[2:] #chops off the 0b
    binaryMsgLength = ('0' * (32 - len(binaryMsgLength))) + binaryMsgLength + '0' #attach a bunch of 0's so it's a 32 byte number

    binaryMsg = str(bin(int.from_bytes(msg.encode(), 'big'))) #returns the binary values of the bytes with the MSB at the beginning of the array
    binaryMsg = '0' + binaryMsg[2:] #gets rid of the 0b, added the 0 cuz error was being thrown down the line

    pixelAmt = int(msgLength/3) #divide by 3 cuz 1 RGB = 3 bytes
    print('writing size of', pixelAmt, 'pixels')
    overwrite(img, width, col, row, 11, binaryMsgLength)
    print('size written')
    col = width-12 #start msg on the 12 pixel
    print('writing message')
    overwrite(img, width, col, row, pixelAmt, binaryMsg)
    print('message written into file', output)

def overwrite(img, width, col, row, end, msg): #msg is a very long binary string
    index = 0 #the i in the for loop was being wonky so i used this to iterate
    pix = img.load() #get all the pixels of the image
    for i in range(end):
        r, g, b = pix[col, row] #gives back something like (x,y,z) in integer form
        r = newValue(r, int(msg[index]))
        index += 1
        g = newValue(g, int(msg[index]))
        index += 1
        b = newValue(b, int(msg[index]))
        index += 1
        img.putpixel((col,row),(r,g,b)) #modifies the pixel at the position
        if col is 0:
            col = width
            row = row - 1
        col = col - 1

def newValue(imageRGB, swap):
    if(imageRGB % 2 is 1): #odd #'s LSB's are 1
        return (imageRGB-1) + swap #subtract 1 and then add swap to make sure that the LSB will hold the swap value
    else: #otherwise the LSB is already 0
        return imageRGB + swap #and you just add the swap value

if __name__ == '__main__':
    main()
