# -*- coding: utf-8 -*-
import sys
import os

#get src and dst path from user
src = os.path.abspath(sys.argv[1])
dst = os.path.abspath(sys.argv[2])

#create a list containing src subfolder foldernames
src_content = os.listdir(src)
print src_content

only_dir_names = []
for src_element in src_content:
	fullpath = os.path.join(src, src_element)
	if os.path.isdir(fullpath):
		only_dir_names.append(src_element)

print only_dir_names
