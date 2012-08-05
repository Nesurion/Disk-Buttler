# -*- coding: utf-8 -*-
import sys
import os

import argparse


########################################## 
#  	Argument parsing
##########################################
# See http://docs.python.org/library/argparse.html#module-argparse

# create a argument parser from the library
args_parser = argparse.ArgumentParser(description='Disk Buttler')

# 1st argument is the source directory
args_parser.add_argument('source', 
	type=str,
	help='directory to read the subfolder names from')

# 2nd argument is the source directory
args_parser.add_argument('destination', 
	type=str,
	help='directory where the new empty subfolders should be created')

arguments = args_parser.parse_args()

########################################## 
#  	Argument parsing END
##########################################


#get src and dst path from user
src = arguments.source
dst = arguments.destination




def mirror_dir(src, dst):
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


	#generate folder in dst path based on only_dir_names
	for dst_element in only_dir_names:
		dst_path = os.path.join(dst, dst_element)
		os.mkdir(dst_path)

mirror_dir(src, dst)

src_serien = os.path.join(src, "tv")
dst_serien = os.path.join(dst, "tv")

mirror_dir(src_serien, dst_serien)