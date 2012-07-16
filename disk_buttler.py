# -*- coding: utf-8 -*-
import sys
import os

#get src and dst path from user
src = os.path.abspath(sys.argv[1])
dst = os.path.abspath(sys.argv[2])

#create a list containing src subfolder foldernames
src_content = os.listdir(src)
