# -*- coding: utf-8 -*-
import sys
import os

#get src and dst path from user
src = os.path.abspath(sys.argv[1])
dst = os.path.abspath(sys.argv[2])

#create a list containing src subfolder foldernames
src_content = os.listdir(src)

#deleting the filenames from listdir
def f(src_element):
	return os.path.join(src, src_element)

src_with_prefix = map(f, src_content)
dirs_only = filter(os.path.isdir, src_with_prefix) 
print dirs_only
