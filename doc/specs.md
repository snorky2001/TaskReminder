Description:
------------
This application provide a mean to manage recurring tasks that have to be done every given time.
Ie: car revision, batteries charging, watering plants ...

Features:
---------
* Application is standalone.
* On launch, it displays the list of tasks with the next expected occurence.
* It is possible to edit each task
* On task deadline a reminder is displayed (popup window)
* On validation of the popup, the task is marked as done and a new reminder is restarted
* Tasks are saved in a file
* Log of tasks done must be written in a csv file. It includes:
 - task identifier
 - task name
 - date of the action
* A task has:
 - an identifier
 - a name
 - a description
 - an interval
 - a last action date
 - a reminder interval


Implementations:
----------------
For any implementation:
* Application have to be split in two parts:
- UI
- logic
* Must be multiplatform (not for the first version)
* Must have a console mode. The base software will be console app which will be used in background by graphical version

- C version
 
- C++ version
 
- Python version

- C# version
