# -*- coding: utf-8 -*-
import sys
import os

#get src and dst path from user
src = os.path.abspath(sys.argv[1])
dst = os.path.abspath(sys.argv[2])

#create a list containing src subfolder foldernames
src_content = os.listdir(src)

only_dir_names = []
for src_element in src_content:
	# combine the user src path with subfolder to a full path,
	# so path.isdir can check if it is dir or not
	fullpath = os.path.join(src, src_element)
	#check if path end with dir or file and write dirs into "only_dir_names"
	if os.path.isdir(fullpath):
		only_dir_names.append(src_element)

print only_dir_names

#next up:
#generate folder in dst path based on only_dir_names

