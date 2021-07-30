import json  
from Trip import Trip
    
def getTrips(filePath):
    inputFile = open(filePath,'r')
    inputJsonData = inputFile.read()
    parsedData = json.loads(inputJsonData)
    tripListJson = parsedData['trips']

    tripObjList = [Trip]

    
    for i in range(len(tripListJson)):
        trip = Trip(1, "Mon", 1.0,1,2)

        trip.tripID = tripListJson[i].get('trip-id')
        trip.tripZone = tripListJson[i].get('tripzone')
        trip.day = tripListJson[i].get('day')
        trip.time = tripListJson[i].get('time')
        trip.origin = tripListJson[i].get('origin')
        trip.to = tripListJson[i].get('to')
        trip.fare = tripListJson[i].get('fare')
        trip.remarks = tripListJson[i].get('remarks')

        print('*****')
        print(type(trip))
        tripObjList.append(trip)

    print("trip list size is yy  --> {}".format(len(tripObjList)))
    return tripObjList

def printTrips(Trips):
    pass

def getFirstTrip():
    pass

def getLastTrip():
    pass



n = getTrips('Cust-ABC.json')
m = getTrips('Cust-DEF.json')
print("-----------> {}".format(len(n)))
print("-----------> {}".format(len(m)))
printTrips(getTrips('Cust-ABC.json'))
printTrips(getTrips('Cust-DEF.json'))

