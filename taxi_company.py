from taxi import Taxi
from Exception import InvalidTaxiName
from trip import Trip

class TaxiCompany:
    def __init__(self):
        self.taxis = []
        self._lost_trips = 0 

    def add_taxi(self, taxi:Taxi):
        for t in self.taxis:
            if t._id == taxi._id:
                raise InvalidTaxiName
        self.taxis.append(taxi)

    def get_available(self):
        return [taxi.str() for taxi in self.taxis]
    
 
    def call_taxi(self, passenger):
        for taxi in self.taxis:
            if not taxi._is_busy:
                taxi.passenger = passenger
                return taxi
        self._lost_trips += 1
        return None

    def get_lost_trips(self):
        return self._lost_trips

    def get_trips(self, taxi_id):
        for taxi in self.taxis:
            if taxi._id == taxi_id:
                return taxi.get_trips()
        raise InvalidTaxiName("Taksi topilmadi")
