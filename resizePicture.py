#########################################################################
# Author:   LIN Junhao (Edlin)                                          #
# Email:    edlinlink@qq.com                                            #
# Date:     Mar. 19, 2015                                               #
#                                                                       #
# Change the picture size under dir "DIR"+"FOLDER".                     #
# The resize picture will be store in "DIR"+"NEWFOLDER".                #
# 
#                                                                       #
# * This script is for Mac OSX.                                         #
#########################################################################

import os, sys
from wand.image import Image

#########################################################################
# Variable Define Area                                                  #
#########################################################################
DIR = '/Users/edlin/Desktop/Pack-it-now/3clothes'

FOLDER = '/trousers_jpg'
NEWFOLDER = '/trousers_bmp'

RESIZE = 40
#########################################################################


filenames = os.listdir(DIR + FOLDER)

os.system("rm " + DIR + FOLDER + os.sep + ".DS_Store")
os.system("rm " + DIR + NEWFOLDER + os.sep + "*")

size = len(filenames)

for index in range(0,size):
    fn = DIR + FOLDER + os.sep + filenames[index]

    try:
        with Image(filename = fn) as img:
            img.resize(RESIZE, RESIZE) # width, height
            img.save(filename = DIR + NEWFOLDER + os.sep + filenames[index][:-3]+"bmp")
    except:
        print filenames[index]

