#!/usr/bin/python
# Reminder software
#
#

import sys
from datetime import timedelta
import pickle
import shlex

firstAvailableId = 0
task = []

def TruncText(text, length):
	return (text[:length-2] + '..') if len(text)>length else text	

def DisplayWelcomeMessage():
	print "TaskReminder v0.1"

def List( parameters ):
	global task
	if len(task) > 0:
		print '{0:5}{1:20}{2:15}{3:20}{4:20}'.format('Id', 'Name', 'Description', 'Interval', 'Reminder')
		for x in task:
			print '{0:5}{1:20}{2:15}{3:20}{4:20}'.format( str(x[0]), TruncText(x[1],19), TruncText(x[2],14), x[3], x[4])
	else:
		print "No tasks"

def New( parameters ):
	global task
	global firstAvailableId
	print "Task name:",
	taskName = raw_input()
	print "Description:",
	taskDescription = raw_input()
	print "Interval (days):",
	taskInterval = timedelta(days=int(raw_input()))
	print "Reminder (days):",
	taskReminder = timedelta(days=int(raw_input()))
	task.append((firstAvailableId, taskName, taskDescription, taskInterval, taskReminder))
	firstAvailableId = firstAvailableId + 1

def Save( parameters ):
	global task
	global firstAvailableId
	with open('tasks.pkl', 'wb') as output:
		pickle.dump(firstAvailableId, output, pickle.HIGHEST_PROTOCOL)
		pickle.dump(task, output, pickle.HIGHEST_PROTOCOL)

def Load( parameters ):
	global task
	global firstAvailableId
	with open('tasks.pkl', 'rb') as input:
		firstAvailableId = pickle.load( input)
		task = pickle.load( input)

def Check( parameters ):
	print "Check"

def Quit( parameters ):
	print "Bye, bye!"

def Help( parameters ):
	print "Help"
	print "h: display this help"
	print "p: list all tasks"
	print "n: create a new task"
	print "d: delete a task"
	print "e: edit a task"
	print "s: save tasks"
	print "l: load tasks"
	print "c: check all tasks"
	print "q: quit application"

# main
DisplayWelcomeMessage()

# Create command list
commands = {}
commands['q']= Quit
commands['h']= Help
commands['help']= Help
commands['p']= List
commands['n']= New
commands['s']= Save
commands['l']= Load
commands['c']= Check

param = [""]
while (param[0] != "q"):
	# Get user input
	print ">>",
	command = raw_input()

	# Get parameters
	param = shlex.split(command)

	# Call the matching command if it exists or display an error message
	param[0] = param[0].lower()
	if param[0] in commands:
		commands[param[0]]( param )
	else:
		print "Command unknown"

