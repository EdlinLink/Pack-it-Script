#########################################################################
# Author:   LIN Junhao (Edlin)                                          #
# Email:    edlinlink@qq.com                                            #
# Date:     Mar. 19, 2015                                               #
#                                                                       #
# Output the grey value of the picture under dir "DIR".                 #
# The resize picture will be store in "DIR"+"NEWFOLDER".                #
#                                                                       #
# * This script is for Mac OSX.                                         #
#########################################################################

import os,sys
from PIL import Image

#########################################################################
# Variable Define Area                                                  #
#########################################################################
DIR = '/Users/edlin/Desktop/Pack-it-now/4clothes/TEST'
PIC_SIZE = 20
AROUND = 0


#########################################################################

filenames=os.listdir(DIR)
size = len(filenames)

for index in range(0,size):

    #try:
    fn = filenames[index]

    im = Image.open(DIR + os.sep+fn)
    rgb_im = im.convert('RGB')
    
    for i in range(0+AROUND, PIC_SIZE-AROUND):
        for j in range(0+AROUND, PIC_SIZE-AROUND):
            r,g,b = rgb_im.getpixel((i, j))
            grey = (r+g+b)/3
            print grey/255.0,
    print

    #except:
    #    print fn
