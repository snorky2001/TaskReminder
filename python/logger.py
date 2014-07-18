#!/usr/bin/python 
#
# Library to manage a file logger
#

import sys
import os

def InitLogger(filename):
	if os.path.exists(filename):
		result = True
	else:
		result = False
	" create file and check right"
	with open(filename, 'a') as output:
		pass
	return result

def PrintLogger(logger, text):
		with open(logger, 'a') as output:
			output.write(text)

