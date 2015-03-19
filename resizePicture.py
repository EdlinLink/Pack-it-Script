#########################################################################
# Author:   LIN Junhao (Edlin)                                          #
# Email:    edlinlink@qq.com                                            #
# Date:     Mar. 19, 2015                                               #
#                                                                       #
# Change the picture size under dir "DIR"+"FOLDER".                     #
# The resize picture will be store in "DIR"+"NEWFOLDER".                #
#                                                                       #
# * This script is for Mac OSX.                                         #
#########################################################################

import os, sys
from wand.image import Image

#########################################################################
# Variable Define Area                                                  #
#########################################################################
DIR = '/Users/edlin/Desktop/Pack-it-now/4clothes'

FOLDER = '/TEST'
NEWFOLDER = '/TEST'

RESIZE = 20
#########################################################################


filenames = os.listdir(DIR + FOLDER)
size = len(filenames)

os.system("rm" + DIR + FOLDER + os.sep + ".DS_Store")

for index in range(0,size):
    fn = DIR + FOLDER + os.sep + filenames[index]

    try:
        with Image(filename = fn) as img:
            img.resize(RESIZE, RESIZE) # width, height
            img.save(filename = DIR + NEWFOLDER + os.sep + filenames[index][:-3]+"bmp")
    except:
        print filenames[index]

