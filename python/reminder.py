#!/usr/bin/python
# Reminder software
#
#

from datetime import timedelta
from datetime import datetime
import shlex
import readline

from tasks import *

TXT_WRONG_INT_INPUT = "That's not an integer value!"
TXT_INVALID_PARAMETER = "Invalid parameter!"
TXT_WRONG_ID = "Wrong Id!"

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
			print(TXT_WRONG_INT_INPUT)

	return val

def	FormatDuration(duration):
	return str(duration)

def DisplayWelcomeMessage():
	print "TaskReminder v0.1"

def Print( taskList, parameters ):
	if len(parameters)>1:
		try:
			taskId = int(parameters[1])
		except ValueError:
			print(TXT_INVALID_PARAMETER)
			return

		if CheckTaskId( taskList, taskId):
			task = GetTask( taskList, taskId )
			print "Id: {0}".format(taskId)
			print "Name: {0}".format(task[0])
			print "Description: {0}".format(task[1])
			print "Interval: {0}".format(task[2])
			print "Reminder: {0}".format(task[3])
			print "Last done: {0}".format(task[4])
		else:
			print TXT_WRONG_ID
	else:
		tasks = GetTasks( taskList )
		if len(tasks) > 0:
			print '{0:5}{1:20}{2:15}{3:20}{4:20}{5:20}'.format(
					'Id',
					'Name',
					'Description',
					'Interval',
					'Reminder',
					'Last done')
			for k,v in tasks.iteritems():
				print '{0:5}{1:20}{2:15}{3:20}{4:20}{5:20}'.format(
						str(k),
						TruncText(v[0],19),
						TruncText(v[1],14),
						str(v[2]),
						str(v[3]),
						str(v[4]))
		else:
			print "No task"

def New( taskList, parameters ):
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
		try:
			taskInterval = int(parameters[3])
		except ValueError:
			print(TXT_INVALID_PARAMETER)
			return

	if len(parameters)<5:
		taskReminder = int_input("Reminder (days):")
	else:
		try:
			taskReminder = int(parameters[4])
		except ValueError:
			print(TXT_INVALID_PARAMETER)
			return
	AddTask( taskList, taskName, taskDescription, taskInterval, 
			 taskReminder)

def Save( taskList, parameters ):
	fileName = 'tasks.pkl'
	if len(parameters)>=2:
		fileName = parameters[1]
	try:
		SaveTasks( taskList, fileName)
	except IOError:
		print 'Unable to access file %s' % fileName	

def Load( taskList, parameters ):
	fileName = 'tasks.pkl'
	if len(parameters)>=2:
		fileName = parameters[1]
	try:
		LoadTasks( taskList, fileName)
	except IOError:
		print 'Unable to access file %s' % fileName

def Check( taskList, parameters ):
	currentDate = datetime.now()
	(due, late) = CheckTasks( taskList, currentDate )
	for task in due:
		print "{0} is due in {1}".format(task[0], task[1])
	for task in late:
		print "{0} is late of {1}".format(task[0], task[1])

def Delete( taskList, parameters ):
	if len(parameters)<2:
		taskId = int_input("Task to delete:")
	else:
		try:
			taskId = int(parameters[1])
		except ValueError:
			print TXT_INVALID_PARAMETER
			return
	if CheckTaskId(taskList, taskId):
		print "Delete task {0} <y/N>?".format(taskId),
		rep = raw_input().lower()
		if rep == "y":
			DeleteTask( taskList, taskId )
			print "Task deleted"
	else:
		print TXT_WRONG_ID

def Edit( taskList, parameters ):
	if len(parameters)<2:
		taskId = int_input("Task to edit:")
	else:
		try:
			taskId = int(parameters[1])
		except ValueError:
			print TXT_INVALID_PARAMETER
			return
	if CheckTaskId( taskList, taskId):
		task = GetTask( taskList, taskId )
		print "Task name [%s]:" % task[0],
		taskName = raw_input() or task[0]
		print "Description [%s]:" % task[1],
		taskDescription = raw_input() or task[1]
		print "Interval (days) [%s]:" % task[2],
		taskInterval = int(raw_input() or task[2])
		print "Reminder (days) [%s]:" % task[3],
		taskReminder = int(raw_input() or task[3])
		UpdateTask( taskList, taskId, taskName, taskDescription,
					taskInterval, taskReminder, task[4])
	else:
		print TXT_WRONG_ID


def Validate( taskList, parameters ):
	if len(parameters)<2:
		taskId = int_input("Task to validate:")
	else:
		try:
			taskId = int(parameters[1])
		except ValueError:
			print TXT_INVALID_PARAMETER
			return
	if len(parameters)<3:
		validationTime = datetime.now()
	else:
		try:
			validationTime = datetime.strptime(parameters[2], "%x %X")
		except ValueError:
			print "Format %s" % parameters[2]
			print 'Invalid time provided!'
			return
	if CheckTaskId( taskList, taskId):
		ValidateTask( taskList, taskId, validationTime )
		print "Task validated"
	else:
		print TXT_WRONG_ID

def Quit( taskList, parameters ):
	print "Bye, bye!"

def Help( taskList, parameters ):
	print "Help"
	print "h: display this help"
	print "p [<Id>]: list all tasks"
	print "n <Name> <Description> <Interval> <Reminder>: create a new task"
	print "d <Id>: delete a task"
	print "e <Id>: edit a task"
	print "s <file>: save tasks into a file"
	print "l <file>: load tasks from a file"
	print "c: check all tasks"
	print "v <CheckId> [""MM/DD/YY HH:MM:SS""]: mark a task as validate"
	print "q: quit application"

def main():
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

	taskList = CreateEmptyTaskList( )

	param = [""]
	while (len(param)==0 or param[0] != "q"):
		# Get user input
		userCommand = raw_input(">> ")

		# Get parameters
		param = shlex.split(userCommand)

		# Call the matching command (case insensitive) if it exists or display an error message
		if len(param)>0:
			cmd = param[0].lower()
			if cmd in commands:
				commands[cmd]( taskList, param )
			else:
				print "Command unknown"

if __name__ == "__main__":
    main()
