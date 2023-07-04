class Ride:
    def __init__(self, rideNumber, rideCost, tripDuration):
        self.rideNumber = rideNumber
        self.rideCost = rideCost
        self.tripDuration = tripDuration

    def lessThan(self, other_ride):
        if self.rideCost < other_ride.rideCost:
            return True
        elif self.rideCost > other_ride.rideCost:
            return False
        elif self.rideCost == other_ride.rideCost:
            if self.tripDuration > other_ride.tripDuration:
                return False
            else:
                return True
