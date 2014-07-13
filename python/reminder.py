#!/usr/bin/python
# Reminder software
#
#

import sys
from datetime import timedelta
from datetime import datetime
import pickle
import shlex

version = 1.0
firstAvailableId = 0
tasks = {}

def TruncText(text, length):
	return (text[:length-2] + '..') if len(text)>length else text	

def int_input(prompt):
	valid = False
	while (valid == False):
		userInput = raw_input(prompt)
		try:
			val = int(userInput)
			valid = True
		except ValueError:
			print("That's not an integer value!")

	return val


def DisplayWelcomeMessage():
	print "TaskReminder v0.1"

def Print( parameters ):
	global tasks
	if len(parameters)>1:
		taskId = int(parameters[1])
		if taskId in tasks.keys():
			print "Id: {0}".format(taskId)
			print "Name: {0}".format(tasks[taskId][0])
			print "Description: {0}".format(tasks[taskId][1])
			print "Interval: {0}".format(tasks[taskId][2])
			print "Reminder: {0}".format(tasks[taskId][3])
			print "Last done: {0}".format(tasks[taskId][4])
		else:
			print "Wrong Id"
	else:
		if len(tasks) > 0:
			print '{0:5}{1:20}{2:15}{3:20}{4:20}{5:20}'.format('Id', 'Name', 'Description', 'Interval', 'Reminder', 'Last done')
			for k,v in tasks.iteritems():
				print '{0:5}{1:20}{2:15}{3:20}{4:20}{5:20}'.format( str(k), TruncText(v[0],19), TruncText(v[1],14), str(v[2]), str(v[3]), str(v[4]))
		else:
			print "No task"

def New( parameters ):
	global tasks
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
		taskInterval = int_input("Interval (days):")
	else:
		taskInterval = int(parameters[3])

	if len(parameters)<5:
		print "Reminder (days):",
		taskReminder = int(raw_input())
	else:
		taskReminder = int(parameters[4])

	tasks[firstAvailableId] = (taskName, taskDescription, taskInterval, taskReminder, datetime.max)
	firstAvailableId = firstAvailableId + 1

def Save( parameters ):
	global tasks
	global firstAvailableId
	global version
	fileName = 'tasks.pkl'
	if len(parameters)==2:
		fileName = parameters[1]
	with open(fileName, 'wb') as output:
		pickle.dump(version, output, pickle.HIGHEST_PROTOCOL)
		pickle.dump(firstAvailableId, output, pickle.HIGHEST_PROTOCOL)
		pickle.dump(tasks, output, pickle.HIGHEST_PROTOCOL)

def Load( parameters ):
	global tasks
	global firstAvailableId
	global version
	fileName = 'tasks.pkl'
	if len(parameters)==2:
		fileName = parameters[1]
	with open(fileName, 'rb') as input:
		version = pickle.load( input)
		firstAvailableId = pickle.load( input)
		tasks = pickle.load( input)

def Check( parameters ):
	currentDate = datetime.now()
	for k,v in tasks.iteritems():
		if (v[4]<>datetime.max):
			if ( v[4] + timedelta(minutes=v[2]) - timedelta(minutes=v[3]) < currentDate):
				print "{0} due date is {1}".format(k, v[4] + timedelta(minutes=v[2]))
				print "{0} reminder date is {1}".format(k, v[4] + timedelta(minutes=v[2])- timedelta(minutes=v[3]))
				if ( v[4] + timedelta(minutes=v[2]) < currentDate):
					print "{0} is late".format(k)
				else:
					print "{0} is due in {1}".format(k, currentDate - (v[4] + timedelta(minutes=v[2])))

def Delete( parameters ):
	global tasks
	if len(parameters)<2:
		print "Task to delete:",
		taskId = int(raw_input())
	else:
		taskId = int(parameters[1])
	if taskId in tasks.keys():
		print "Delete task {0} <y/N>?".format(taskId),
		rep = raw_input().lower()
		if rep == "y":
			del tasks[taskId]
			print "task deleted"
	else:
		print "Wrong Id"

def Edit( parameters ):
	global tasks
	global firstAvailableId

	if len(parameters)<2:
		print "Task to edit:",
		taskId = int(raw_input())
	else:
		taskId = int(parameters[1])
	if taskId in tasks.keys():
		print "Task name [%s]:" % tasks[taskId][0],
		taskName = raw_input() or tasks[taskId][0]
		print "Description [%s]:" % tasks[taskId][1],
		taskDescription = raw_input() or tasks[taskId][1]
		print "Interval (days) [%s]:" % tasks[taskId][2],
		taskInterval = int(raw_input() or tasks[taskId][2])
		print "Reminder (days) [%s]:" % tasks[taskId][3],
		taskReminder = int(raw_input() or tasks[taskId][3])
		tasks[taskId] = (taskName, taskDescription, taskInterval, taskReminder, tasks[taskId][4])
	else:
		print "Wrong Id"


def Validate( parameters ):
	global tasks
	if len(parameters)<2:
		print "Task to validate:",
		taskId = int(raw_input())
	else:
		taskId = int(parameters[1])
	if len(parameters)<3:
		validationTime = datetime.now()
	else:
		validationTime = datetime.strptime(parameters[2], "%X")
	if taskId in tasks.keys():
		tasks[taskId] = (tasks[taskId][0], tasks[taskId][1], tasks[taskId][2], tasks[taskId][3], validationTime)
		print "task validated"
	else:
		print "Wrong Id"

def Quit( parameters ):
	print "Bye, bye!"

def Help( parameters ):
	print "Help"
	print "h: display this help"
	print "p <Id>: list all tasks"
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
commands['p']= Print
commands['n']= New
commands['s']= Save
commands['d']= Delete
commands['e']= Edit
commands['l']= Load
commands['c']= Check
commands['v']= Validate

param = [""]
while (len(param)==0 or param[0] != "q"):
	# Get user input
	print ">>",
	userCommand = raw_input()

	# Get parameters
	param = shlex.split(userCommand)

	# Call the matching command (case insensitive) if it exists or display an error message
	if len(param)>0:
		cmd = param[0].lower()
		if cmd in commands:
			commands[cmd]( param )
		else:
			print "Command unknown"

