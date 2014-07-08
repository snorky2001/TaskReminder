#!/usr/bin/python
# Remnder software
#
#

import sys

def DisplayWelcomeMessage():
	print "TaskReminder v0.1"

def List( parameters ):
	print "List"
	print "Parameters: [%s]" % ", ".join(map(str, parameters))

def Quit( parameters ):
	print "Quit"

def Help( parameters ):
	print "Help"
	print "h: display this help"
	print "l: list all tasks"
	print "q: quit application"

# main
DisplayWelcomeMessage()

# Create command list
commands = {}
commands['q']= Quit
commands['h']= Help
commands['l']= List

param = [""]
while (param[0] != "q"):
	# Get user input
	print ">>",
	command = raw_input()

	# Get parameters
	param = command.split()

	# Call the matching command if it exists or display an error message
	param[0] = param[0].lower()
	if param[0] in commands:
		commands[param[0]]( param )
	else:
		print "Command unknown"

