# Sabrina Hatch
# July 10 2023
# CMU REUSE
# Program to simulate PS scheduling policy on a network with a exponential job size distribution
import numpy as np

class Job:
    def __init__(self, arrivalTime, size, rpt):
        self.arrivalTime = arrivalTime
        self.size = size
        self.rpt = rpt
        self.departureTime = None
        self.completionTime = None

# Function to generate job sizes
def generateJobSize():
    return np.random.exponential(1)

# Function that generates an interarrival time
def generateInterarrivalTime():
    return np.random.exponential(10 / 8)

def handleArr():
    global clock, lastEvent, departures, nextArrTime, nextDepTime, completionTimes, jobSizes, departingJob, rate, servingList

    size = generateJobSize()
    job = Job(arrivalTime=clock, size=size, rpt=size)
    jobSizes.append(job.size)

    # calculate the rpts for each job based on the interval between now and the last event as well as the number
    # of jobs that were in the system BEFORE adding the new job that was just created

    print("this is the servingList: " + str(servingList))
    for x in servingList:
        print("This is the jobsize " + str(x.size) + " of " + str(x))
        print("This is the rate " + str(rate))
        print("This is the rpt before: " + str(x.rpt) + " of " + str(x))
        print("This is the time elapsed " + str(clock - lastEvent))
        x.rpt = x.rpt - (clock - lastEvent) * (1 / len(servingList))
        print("this is the rpt of job after " + str(x) + " " + str(x.rpt))

        print("\n")

    # append the new job to the list of jobs currently being serviced
    servingList.append(job)
    print("New arrival of " + str(job))

    job = None
    # update the lastEvent var
    lastEvent = clock
    # update the new rate for the server
    rate = (1/len(servingList))

    # update all the predicted departureTimes based on the newly calculated rate
    for x in servingList:
        x.departureTime = ((x.rpt)/rate) + clock

    # generate the nextArrTime


    # find the job with the min departure time and set that departure time equal to the next dep time
    departingJob = min(servingList, key = lambda x:x.departureTime)
    nextDepTime = departingJob.departureTime
    job = None
    nextArrTime = clock + generateInterarrivalTime()


def handleDep():
    global clock, lastEvent, departures, nextArrTime, nextDepTime, completionTimes, jobSizes, departingJob, rate, servingList
    departures += 1

    departingJob.completionTime = departingJob.departureTime - departingJob.arrivalTime
    if departures == maxDepartures:
        completionTimes.append(departingJob.completionTime)
        print("New departure of " + str(departingJob))
    servingList.remove(departingJob) # equivalent to pop first from the list



    if len(servingList) != 0:
        # update the serving rpts of each job still being serviced
        for x in servingList:
            x.rpt = x.rpt - ((clock - lastEvent) * (1 / len(servingList)))
        lastEvent = clock
        # set new rate
        rate = (1 / len(servingList))


        for x in servingList:
            x.departureTime = (x.rpt / rate) + clock
        departingJob = min(servingList, key=lambda x: x.departureTime)  # this will be the head of the queue
        nextDepTime = departingJob.departureTime
    else:
        departingJob = None
        nextDepTime = float("inf")
        lastEvent = clock
# The following lines of code run the logic of the simulation
seed = 0
maxDepartures = 5
completionTimes = []
count = 0
runs = 2
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


# load data into a txt file
# with open("PS_LOAD_0.8.txt", "w") as fp:
#     for item in completionTimes:
#         fp.write("%s\n" % item)
#
#




