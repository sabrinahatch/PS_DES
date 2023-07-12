**Pseudocode for PS single server model**
<br>
def handleArrival() 
Create new job object and assign it a size and arrivalTime
Determine the rpt of each job in the servingList by calculating: servingList[i].size - (clock - lastEvent)(serverCap/len(servingList))
Update lastEvent = clock
Update the counter for the number of jobs in servingList
Calculate the new rate = (serverCap/len(servingList)) and assign each job a new departureTime = (job.size/rate) + clock
Generate the next arrival time and set nextArrival
Get minimum departureTime of all jobs in servingList and set that as the next nextDepTime
set departingJob = job that has min dep time
def handleDeparture()  
Inc the departure counter to keep track of maxDepartures
Set completionTime = departingJob.departureTime - departingJob.arrivalTime and append to corr. list of completion times
Remove departingJob from servingList 
If len(servingList) != 0:
Determine the rpt of each job in the servingList by calculating: servingList[i].size - (clock - lastEvent)(serverCap/len(servingList))
Update lastEvent = clock
Update the counter for the number of jobs in servingList
Calculate the new rate = (serverCap/len(servingList)) and assign each job a new departureTime = (job.size/rate) + clock
Else (the server is empty):
departingJob = None
nextDepartureTime = inf

Sim logic:
Set seed = 0
Set max departures and initialized empty array for runCompletions
Set number of runs
For i in range(runs):
Generate random seed
Set departures to 0
Set next depTime to inf and initialize servingList, completionTimes, and jobSizes as empty lists
Set next arr time as clock + genArrTime()
While departures <= maxDep:
If nextArrTime <= nextDepTime:
Clock = nextArrTime
handleArr()
Else:
Clock = nextDepTime
handleDep()
Append last job in each run to list
Seed += 1




