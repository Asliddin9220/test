from place import Place
from trip import Trip
class Taxi:
    def __init__(self,id):
        self._id = id
        self._is_busy=False
        self._passenger=None
        self._trips:list[Trip] = []

    def __str__(self):
        return f"Taksi ID: {self._id}"
    

    def begin_trip(self, destination):
        if self._is_busy:
            return "Taksi allaqachon band"
        else:
            self.passenger._place= destination
            self._is_busy = True
            return f"Safar boshlandi {destination.__str__()}"

    def terminate_trip(self):
        if self._is_busy:
            self._is_busy = False
            self.passenger = None
            return "safar yakunlandi"
        else:
            return "hech qanday safar davom etmayapti"
        
    def get_trips(self):
        return [trip.__str__() for trip in self._trips]