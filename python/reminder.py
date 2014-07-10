#!/usr/bin/python
# Reminder software
#
#

import sys
from datetime import timedelta
import pickle
import shlex

firstAvailableId = 0
task = {}

def TruncText(text, length):
	return (text[:length-2] + '..') if len(text)>length else text	

def DisplayWelcomeMessage():
	print "TaskReminder v0.1"

def List( parameters ):
	global task
	if len(task) > 0:
		print '{0:5}{1:20}{2:15}{3:20}{4:20}'.format('Id', 'Name', 'Description', 'Interval', 'Reminder')
		for k,v in task.iteritems():
			print '{0:5}{1:20}{2:15}{3:20}{4:20}'.format( str(k), TruncText(v[0],19), TruncText(v[1],14), v[2], v[3])
	else:
		print "No tasks"

def New( parameters ):
	global task
	global firstAvailableId

	if len(parameters)<2:
		print "Task name:",
		taskName = raw_input()
	else:
		taskName = parameters[1]

	if len(parameters)<3:
		print "Description:",
		taskDescription = raw_input()
	else:
		taskDescription = parameters[2]

	if len(parameters)<4:
		print "Interval (days):",
		taskInterval = timedelta(days=int(raw_input()))
	else:
		taskInterval = timedelta(days=int(parameters[3]))

	if len(parameters)<5:
		print "Reminder (days):",
		taskReminder = timedelta(days=int(raw_input()))
	else:
		taskReminder = timedelta(days=int(parameters[4]))

	task[firstAvailableId] = (taskName, taskDescription, taskInterval, taskReminder)
	firstAvailableId = firstAvailableId + 1

def Save( parameters ):
	global task
	global firstAvailableId
	fileName = 'tasks.pkl'
	if len(parameters)==2:
		fileName = parameters[1]
	with open(fileName, 'wb') as output:
		pickle.dump(firstAvailableId, output, pickle.HIGHEST_PROTOCOL)
		pickle.dump(task, output, pickle.HIGHEST_PROTOCOL)

def Load( parameters ):
	global task
	global firstAvailableId
	fileName = 'tasks.pkl'
	if len(parameters)==2:
		fileName = parameters[1]
	with open(fileName, 'rb') as input:
		firstAvailableId = pickle.load( input)
		task = pickle.load( input)

def Check( parameters ):
	print "Check"

def Delete( parameters ):
	global task
	if len(parameters)<2:
		print "Task to delete:",
		taskId = int(raw_input())
	else:
		taskId = int(parameters[1])
	if taskId in task.keys():
		print "Delete task {0} <y/N>?".format(taskId),
		rep = raw_input().lower()
		if rep == "y":
			del task[taskId]
			print "Task deleted"
	else:
		print "Wrong Id"

def Edit( parameters ):
	print "Edit"

def Validate( parameters ):
	print "Validate"

def Quit( parameters ):
	print "Bye, bye!"

def Help( parameters ):
	print "Help"
	print "h: display this help"
	print "p: list all tasks"
	print "n <Name> <Description> <Interval> <Reminder>: create a new task"
	print "d <Id>: delete a task"
	print "e <Id>: edit a task"
	print "s <file>: save tasks into a file"
	print "l <file>: load tasks from a file"
	print "c: check all tasks"
	print "v <CheckId>: mark a task as validate"
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
commands['d']= Delete
commands['e']= Edit
commands['l']= Load
commands['c']= Check
commands['v']= Validate

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

