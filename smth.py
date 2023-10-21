class Driver:
    def __init__(self, name):
        self.name = name
        self.races = []

    def getName(self):
        return self.name

    def addRace(self, race):
        self.races.append(race)

    def getPoints(self):
        points = 0
        for race in self.races:
            position = race.getPosition(self)
            if position <= 10:
                points += [25, 18, 15, 12, 10, 8, 6, 4, 2, 1][position - 1]
        return points


class GrandPrix:
    def __init__(self, name):
        self.name = name
        self.races = []

    def getName(self):
        return self.name

    def addRace(self, race):
        self.races.append(race)

    def getGPRanking(self):
        ranking = sorted(self.races, key=lambda x: x.time)
        return ranking


class Race:
    def __init__(self, grand_prix, driver, time):
        self.grand_prix = grand_prix
        self.driver = driver
        self.time = time

    def getPosition(self, driver):
        ranking = self.grand_prix.getGPRanking()
        for i in range(len(ranking)):
            if ranking[i].driver == driver:
                return i + 1
        return -1


class Championship:
    def __init__(self):
        self.drivers = []
        self.grand_prixs = []

    def createDriver(self, name):
        driver = Driver(name)
        self.drivers.append(driver)
        return driver

    def getDrivers(self):
        return self.drivers

    def getDriver(self, name):
        for driver in self.drivers:
            if driver.getName() == name:
                return driver
        return None

    def defineGrandPrix(self, name):
        grand_prix = GrandPrix(name)
        self.grand_prixs.append(grand_prix)
        return grand_prix

    def getGrandPrix(self, name):
        for grand_prix in self.grand_prixs:
            if grand_prix.getName() == name:
                return grand_prix
        return None

    def getChampionshipRanking(self):
        ranking = sorted(self.drivers, key=lambda x: x.getPoints(), reverse=True)
        return ranking


class Time:
    def __init__(self, gp, driver, hours, minutes, seconds, ms):
        self.gp = gp
        self.driver = driver
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.ms = ms

    def toString(self):
        return f"{self.hours}:{self.minutes}:{self.seconds}.{self.ms}"



championship = Championship()


driver1 = championship.createDriver("Cristiano Ronaldo")
driver2 = championship.createDriver("Lionel Messi")


gp1 = championship.defineGrandPrix("Bahrain Grand Prix")
gp2 = championship.defineGrandPrix("Spanish Grand Prix")


race1 = Race(gp1, driver1, Time(gp1, driver1, 1, 30, 12, 500))
race2 = Race(gp1, driver2, Time(gp1, driver2, 1, 31, 15, 200))
race3 = Race(gp2, driver1, Time(gp2, driver1, 1, 28, 45, 800))
race4 = Race(gp2, driver2, Time(gp2, driver2, 1, 29, 30, 600))

gp1.addRace(race1)
gp1.addRace(race2)
gp2.addRace(race3)
gp2.addRace(race4)


ranking = championship.getChampionshipRanking()
for i, driver in enumerate(ranking):
    print(f"{i+1}. {driver.getName()}: {driver.getPoints()} points")
