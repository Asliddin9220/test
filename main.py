from place import Place
from passenger import Passenger
from taxi import Taxi
from taxi_company import TaxiCompany
from Exception import InvalidTaxiName
from trip import Trip

place_1 = Place("Zargarlik 4 St", "Chilonzor", "Mehrjon MFY")
place_2 = Place("Farhod 21 St", "Uchtepa", "Foziltepa MFY")

passenger = Passenger(place_1)
taxi01 = Taxi(1)
taxi02 = Taxi(2)

company = TaxiCompany()
company.add_taxi(taxi01)
company.add_taxi(taxi02)

uclon_taxi = company.call_taxi(passenger)
if uclon_taxi:
        print(f"Taksi {uclon_taxi._id} yo'lovchilarni olib ketishga chaqirdi")

        print(uclon_taxi.begin_trip(place_2))

        print(uclon_taxi.terminate_trip())

        print(f"Lost trips: {company.get_lost_trips()}")

        
        trips = company.get_trips(1)
        print(f"Trips for Taxi 1: {trips}")
        
else:
    print("Mavjud taksilar yo'q. Qongiroq bekor qilindi.")