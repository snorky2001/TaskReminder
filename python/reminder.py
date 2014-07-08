#!/usr/bin/python
# Reminder software
#
#

import sys
from datetime import timedelta
import pickle

task = []

def DisplayWelcomeMessage():
	print "TaskReminder v0.1"

def List( parameters ):
	global task
	if len(task) > 0:
		for x in task:
			print x
	else:
		print "No tasks"

def New( parameters ):
	global task
	print "Task name:",
	taskName = raw_input()
	print "Description:",
	taskDescription = raw_input()
	print "Interval (days):",
	taskInterval = timedelta(days=int(raw_input()))
	print "Reminder (days):",
	taskReminder = timedelta(days=int(raw_input()))
	task.append((taskName, taskDescription, taskInterval, taskReminder))

def Save( parameters ):
	global task
	with open('tasks.pkl', 'wb') as output:
		pickle.dump(task, output, pickle.HIGHEST_PROTOCOL)

def Load( parameters ):
	global task
	with open('tasks.pkl', 'rb') as input:
		task = pickle.load( input)

def Quit( parameters ):
	print "Bye, bye!"

def Help( parameters ):
	print "Help"
	print "h: display this help"
	print "p: list all tasks"
	print "n: create a new task"
	print "s: save tasks"
	print "l: load tasks"
	print "q: quit application"

# main
DisplayWelcomeMessage()

# Create command list
commands = {}
commands['q']= Quit
commands['h']= Help
commands['p']= List
commands['n']= New
commands['s']= Save
commands['l']= Load

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

