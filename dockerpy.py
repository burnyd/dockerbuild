"""This is a small python script that will spin up as many container using a for loop someone wants to use
-Daniel Hertzberg"""

import base64
import httplib
import time
import sys
import os
import commands

#Declair variables for arguments

NUM_CONTAINERS = input("How many containers would you like to create?")
DOCKER_COMMANDS =  raw_input("What command would you like to execute do not forget the /bin/bash example /bin/bash -c ping x.x.x.x ")
DOCKER_IMAGE = raw_input("Which image would you like to use?")

"""Error Checking First"""

#Check first to see if the Docker Daemon is running.  This command uses the commands python module and does a simple linux command line to check.  If the return does not contain Docker service is running then it will tell the user to run the command.

def checkstatus():
	checkdaemon = commands.getoutput('service docker status')
	if 'start/running' in checkdaemon:
		print("Docker service is running")
	else: 
		print("Make sure that the docker daemon is running by trying service docker status or service docker start") 

#Makes sure that the NUM_CONTAINERS is actually a number and not numeric so it trys to format it with the int.  
try:
   int(NUM_CONTAINERS)
except:
   print "Number of containers must be a number."

#execute the function   
checkstatus()

#Simple range command will take the amount of containers from the NUM_CONTAINERS input and run the command from os.system as many times in the range.
for runcontainers in range(NUM_CONTAINERS):
	os.system('docker run -dit ' + DOCKER_IMAGE + ' ' + DOCKER_COMMANDS + ' ')

#Function that will simply stop all the containers after enter is pressed.
def stopcontainers():
	DOCKER_STOP = raw_input("\n Hit enter to stop all the containers ")
	os.system('docker stop $(docker ps -a -q)')
        os.system('docker rm $(docker ps -a -q)')

stopcontainers()





