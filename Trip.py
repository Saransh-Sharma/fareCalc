import json
class Trip:

    tripID = 1
    tripFare = 0
    remarks = ""

    def __init__(self, tripZone, day, time, origin, to):
        
        self.tripZone = None
        self.day = day
        self.time = time
        self.origin = origin
        self.to = to
        
        

    # def __init__(self):
    #     self.tripID = 1
    #     self.tripZone = None
    #     self.day = day
    #     self.time = time
    #     self.origin = origin
    #     self.to = to
    #     self.tripFare = 0
    #     self.remarks = ""

