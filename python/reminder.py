#!/usr/bin/python
# Remnder software
#
#

import sys

task = []

def DisplayWelcomeMessage():
	print "TaskReminder v0.1"

def List( parameters ):
	global task
	print "List"
	print "Parameters: [%s]" % ", ".join(map(str, parameters))
	for x in task:
		print x

def New( parameters ):
	global task
	print "Task name:",
	taskName = raw_input()
	print "Description:",
	taskDescription = raw_input()
	print "Interval (days):",
	taskInterval = raw_input()
	print "Reminder (days):",
	taskReminder = raw_input()
	task.append((taskName, taskDescription, taskInterval, taskReminder))


def Quit( parameters ):
	print "Quit"

def Help( parameters ):
	print "Help"
	print "h: display this help"
	print "l: list all tasks"
	print "n: creqte a new task"
	print "q: quit application"

# main
DisplayWelcomeMessage()

# Create command list
commands = {}
commands['q']= Quit
commands['h']= Help
commands['l']= List
commands['n']= New

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

