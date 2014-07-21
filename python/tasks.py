#!/usr/bin/python 
#
# Library to manage a list of task repeated at fixed interva Library to manage a list of task repeated at fixed intervall
#

import sys
import pickle
from datetime import timedelta
from datetime import datetime

def CreateEmptyTaskList( ):
	# Create a new empty taskList
	# taskList = list (firstAvailableId, tasks dict)
	return [0, {}]

def AddTask(taskList, Name, Description, Interval, Reminder):
	# Add a task to a taskList
	firstAvailableId = taskList[0]
	tasks = taskList[1]
	tasks[firstAvailableId] = (Name, Description, Interval, Reminder, datetime.max)
	taskList[0] = firstAvailableId + 1

def SaveTasks(taskList, filename):
	# Save the taskList in a file
	# Can return IOError exception for wrong filename
	version = 1.0
	with open(filename, 'wb') as output:
		pickle.dump(version, output, pickle.HIGHEST_PROTOCOL)
		pickle.dump(taskList[0], output, pickle.HIGHEST_PROTOCOL)
		pickle.dump(taskList[1], output, pickle.HIGHEST_PROTOCOL)

def LoadTasks(taskList, filename):
	# Load a taskList from a file
	# Can return IOError exception for wrong filename
	with open(filename, 'rb') as input:
		version = pickle.load(input)
		taskList[0] = pickle.load(input)
		taskList[1] = pickle.load( input)

def CheckTasks(taskList, checkDate):
	# Check the taskList status at checkDate date
	# return a tuple (dueIn, lateOf)
	# where dueIn is a list of (Id, delta to due date)
	# and lateOf is a list of (Id, delta passed of due date)
	dueIn = []
	lateOf = []
	for k,v in taskList[1].iteritems():
		if (v[4]<>datetime.max):
			dueDate = v[4] + timedelta(days=v[2])  
			reminderDate = dueDate - timedelta(days=v[3]) 
			if ( reminderDate < checkDate):
				if ( dueDate < checkDate):
					lateOf.append( (k, checkDate - dueDate) )
				else:
					dueIn.append( (k, dueDate - checkDate) )
	return (dueIn, lateOf)

def CheckTaskId(taskList, taskId):
	# Check if the taskId is a valid Id in taskList
	if taskId in taskList[1].keys():
		return True
	else:
		return False

def DeleteTask(taskList, taskId):
	# Delete the task with taskId from the taskList
	# Can return IndexError if invalid taskId is passed
	if taskId in taskList[1].keys():
		del taskList[1][taskId]
	else:
		raise IndexError

def UpdateTask(taskList, taskId, Name, Description, Interval, Reminder, ValidatedDate):
	# Update the task with taskId from the taskList
	# Can return IndexError if invalid taskId is passed
	if taskId in taskList[1].keys():
		taskList[1][taskId] = (Name, Description, Interval, Reminder, ValidatedDate)
	else:
		raise IndexError

def GetTask(taskList, taskId):
	# Return the task with taskId from the taskList
	# Can return IndexError if invalid taskId is passed
	if taskId in taskList[1].keys():
		return taskList[1][taskId]
	else:
		raise IndexError

def GetTasks(taskList):
	# Return the list of all tasks in taskList
	return taskList[1]

def ValidateTask(taskList, taskId, ValidateDate):
	# Set the validation time of the task with id taskId
	# The ValidateDate is ued to compute the next DueDate
	if taskId in taskList[1].keys():
		taskList[1][taskId] = (taskList[1][taskId][0],
				   taskList[1][taskId][1],
				   taskList[1][taskId][2],
				   taskList[1][taskId][3],
				   ValidateDate)
	else:
		raise IndexError


