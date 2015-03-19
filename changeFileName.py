#########################################################################
# Author:   LIN Junhao (Edlin)                                          #
# Email:    edlinlink@qq.com                                            #
# Date:     Mar. 18, 2015                                               #
#                                                                       #
# Change the filename under dir "DIR".                                  #
# The filename will be: "PREDIX"_"INDEX-NUM".                           #
#                                                                       #
# * This script is for Mac OSX.                                         #
#########################################################################

import os,sys

#########################################################################
# Variable Define Area                                                  #
#########################################################################

DIR = '/Users/edlin/Desktop/Pack-it-now/4clothes/trousers'
PREFIX = "trousers"

os.system("rm .DS_Store")

filenames = os.listdir(DIR)
file_num = len(filenames)

for index in range(0, file_num):
    os.rename(DIR + os.sep + filenames[index], DIR + os.sep + PREFIX + "_" + str(index+1)+'.jpg')
    index = index +1

print file_num
