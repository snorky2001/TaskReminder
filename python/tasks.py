import sys
import pickle
from datetime import timedelta
from datetime import datetime


def CreateEmptyTaskList( ):
	# taskList = list (firstAvailableId, tasks dict)
	return [0, {}]

def AddTask( taskList, Name, Description, Interval, Reminder ):
	firstAvailableId = taskList[0]
	tasks = taskList[1]
	tasks[firstAvailableId] = (Name, Description, Interval, Reminder, datetime.max)
	taskList[0] = firstAvailableId + 1

def SaveTasks( taskList, filename ):
	version = 1.0
	with open(filename, 'wb') as output:
		pickle.dump(version, output, pickle.HIGHEST_PROTOCOL)
		pickle.dump(taskList[0], output, pickle.HIGHEST_PROTOCOL)
		pickle.dump(taskList[1], output, pickle.HIGHEST_PROTOCOL)

def LoadTasks( taskList, filename ):
	with open(filename, 'rb') as input:
		version = pickle.load(input)
		taskList[0] = pickle.load(input)
		taskList[1] = pickle.load( input)

def CheckTasks( taskList, checkDate ):
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
					dueIn.append( (k, checkDate - dueDate) )
	return (dueIn, lateOf)

def CheckTaskId( taskList, taskId):
	if taskId in taskList[1].keys():
		return True
	else:
		return False

def DeleteTask( taskList, taskId):
	if taskId in taskList[1].keys():
		del taskList[1][taskId]
	else:
		raise IndexError

def UpdateTask( taskList, taskId, Name, Description, Interval, Reminder, ValidatedDate ):
	if taskId in taskList[1].keys():
		taskList[1][taskId] = (Name, Description, Interval, Reminder, ValidatedDate)
	else:
		raise IndexError

def GetTask( taskList, taskId):
	if taskId in taskList[1].keys():
		return taskList[1][taskId]
	else:
		raise IndexError

def GetTasks( taskList):
	return taskList[1]

def ValidateTask( taskList, taskId, ValidateDate ):
	if taskId in taskList[1].keys():
		taskList[1][taskId] = (taskList[1][taskId][0],
							   taskList[1][taskId][1],
							   taskList[1][taskId][2],
							   taskList[1][taskId][3],
							   ValidateDate)
	else:
		raise IndexError


