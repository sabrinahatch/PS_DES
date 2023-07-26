# Sabrina Hatch
# July 10 2023
# CMU REUSE
# Program to simulate PS scheduling policy on a network with a exponential job size distribution

# generate my own arrival times and examples and run through print statements in the program
# generate more departures??
# inc the length of experiment
# run comparison for 70% load and compare for SPRT
# randomly generated and created by hand

import numpy as np

class Job:
    def __init__(self, arrivalTime, size, rpt):
        self.arrivalTime = arrivalTime
        self.size = size
        self.rpt = rpt
        self.pdt = None
        self.completionTime = None

# Function to generate job sizes
def generateJobSize():
    return np.random.exponential(1)

# Function that generates an interarrival time
def generateInterarrivalTime():
    return np.random.exponential(10 / 9)

def handleArr():
    global clock, lastEvent, departures, nextArrTime, nextDepTime, completionTimes, jobSizes, departingJob, rate, servingList

    # create a new job for the new arrival and assign corr. attributes
    size = generateJobSize()
    job = Job(arrivalTime=clock, size=size, rpt=size)
    # append size of job to list of job sizes
    jobSizes.append(job.size)

    # calculate the rpts for each job based on the interval between now and the last event as well as the number
    # of jobs that were in the system BEFORE adding the new job that was just created
    for x in servingList:
        x.rpt = x.rpt - ((clock - lastEvent) * (1 / len(servingList)))

    # append the new job to the list of jobs currently being serviced
    servingList.append(job)

    # update the lastEvent var to be now, signifying the arrival of the new job
    lastEvent = clock

    # update the new rate for the server
    rate = (1/len(servingList))

    # update all the pdts based on the newly calculated rate
    for x in servingList:
        x.pdt = ((x.rpt)/rate) + clock


    # find the job with the min departure time and set that departure time equal to the next dep time
    departingJob = min(servingList, key=lambda x: x.pdt)
    nextDepTime = departingJob.pdt
    # generate the next arrival time for the queue
    nextArrTime = clock + generateInterarrivalTime()


def handleDep():
    global clock, lastEvent, departures, nextArrTime, nextDepTime, completionTimes, jobSizes, departingJob, rate, servingList

    departures += 1
    departingJob.completionTime = departingJob.pdt - departingJob.arrivalTime

   # collect relevant data from the departing job
    if departures == maxDepartures:
        completionTimes.append(departingJob.completionTime)


    # update the serving rpts of each job still being serviced
    for x in servingList:
        x.rpt = x.rpt - ((clock - lastEvent) * (1 / len(servingList)))
    lastEvent = clock

    # remove job that just finished from the system
    servingList.remove(departingJob)

    if len(servingList) != 0:
        # set new rate now that job has left the system
        rate = (1 / len(servingList))

        # update the rpt of each job in the serving list
        for x in servingList:
            x.pdt = (x.rpt / rate) + clock
        departingJob = min(servingList, key=lambda x: x.pdt)
        nextDepTime = departingJob.pdt
    else:
        departingJob = None
        nextDepTime = float("inf")
        lastEvent = clock



# The following lines of code run the logic of the simulation
seed = 0
maxDepartures = 20000
completionTimes = []
count = 0
runs = 5000
for i in range(runs):
    count += 1
    np.random.seed(seed)
    nextDepTime = float('inf')
    nextArrTime = generateInterarrivalTime()
    servingList = []
    jobSizes = []
    departingJob = None
    rate = None
    departures = 0
    clock = 0.0
    lastEvent = clock
    print("********************* This is run: " + str(count) + " *****************************" + "\n")

    while departures <= maxDepartures:
        if nextArrTime <= nextDepTime:
            clock = nextArrTime
            handleArr()
        else:
            clock = nextDepTime
            handleDep()

    seed += 1


#load data into a txt file
with open("PS_LOAD_0.9.txt", "w") as fp:
    for item in completionTimes:
        fp.write("%s\n" % item)






