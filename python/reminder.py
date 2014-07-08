#!/usr/bin/python
# Remnder software
#
#

import sys

def DisplayWelcomeMessage():
	print "TaskReminder v0.1"


# main
DisplayWelcomeMessage()
command = ""
while (command != "q"):
	print ">>",
	command = raw_input()

