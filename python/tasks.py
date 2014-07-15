version = 1.0
firstAvailableId = 0
tasks = {}

" taskList = tuple (firstAvailableId, tasks dict)
taskList = (0, {})

def AddTask( taskList, Name, Description, Interval, Reminder, ValidatedDate ):
	firstAvailableId = taskList[0]
	tasks = taskList[1]
	tasks[firstAvailableId] = (Name, Description, Interval, Reminder, datetime.max)
	taskList[0] = firstAvailableId + 1

def SaveTask( taskList, filename ):
	version = 1.0
	with open(fileName, 'wb') as output:
		pickle.dump(version, output, pickle.HIGHEST_PROTOCOL)
		pickle.dump(taskList[0], output, pickle.HIGHEST_PROTOCOL)
		pickle.dump(taskList[1], output, pickle.HIGHEST_PROTOCOL)

def Load( parameters ):
	global tasks
	global firstAvailableId
	global version
	fileName = 'tasks.pkl'
	if len(parameters)>=2:
		fileName = parameters[1]
	try:
		with open(fileName, 'rb') as input:
			version = pickle.load( input)
			firstAvailableId = pickle.load( input)
			tasks = pickle.load( input)
	except IOError:
		print 'Unable to access file %s' % fileName

def Check( parameters ):
	currentDate = datetime.now()
	for k,v in tasks.iteritems():
		if (v[4]<>datetime.max):
			dueDate = v[4] + timedelta(days=v[2])  
			reminderDate = dueDate - timedelta(days=v[3]) 
			if ( reminderDate < currentDate):
				print "{0} due date is {1}".format(k, dueDate)
				print "{0} reminder date is {1}".format(k, reminderDate )
				if ( dueDate < currentDate):
					print "{0} is late".format(k)
				else:
					print "{0} is due in {1}".format(k, currentDate - dueDate)

def Delete( parameters ):
	global tasks
	if len(parameters)<2:
		taskId = int_input("Task to delete:")
	else:
		try:
			taskId = int(parameters[1])
		except ValueError:
			print TXT_INVALID_PARAMETER
			return
	if taskId in tasks.keys():
		print "Delete task {0} <y/N>?".format(taskId),
		rep = raw_input().lower()
		if rep == "y":
			del tasks[taskId]
			print "Task deleted"
	else:
		print TXT_WRONG_ID

def Edit( parameters ):
	global tasks
	global firstAvailableId

	if len(parameters)<2:
		taskId = int_input("Task to edit:")
	else:
		try:
			taskId = int(parameters[1])
		except ValueError:
			print TXT_INVALID_PARAMETER
			return
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
		print TXT_WRONG_ID


def Validate( parameters ):
	global tasks
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
			validationTime = datetime.strptime(parameters[2], "%X")
		except ValueError:
			print 'Invalid time provided!'
			return
	if taskId in tasks.keys():
		tasks[taskId] = (tasks[taskId][0], tasks[taskId][1],
						 tasks[taskId][2], tasks[taskId][3],
						 validationTime)
		print "Task validated"
	else:
		print TXT_WRONG_ID


