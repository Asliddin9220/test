from place import Place  

class Passenger:
    def __init__(self,_place:Place):
        self._place = Place

    def get_place(self):
        return self._place