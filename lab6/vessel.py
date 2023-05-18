class Vessel:

    def __init__(self, name, volume, time, filling):
        self.name = name
        self.volume = volume
        self.time = time
        self.filling = filling

    def get_vessel_info(self):
        report = f"{self.name} vessel:\n volume = {self.volume}\n time = {self.time}\n filling = {self.filling}\n"
        print(report)

class VesselPlacing:

    def fill_vessel(self):
        self.filling = True
        print("Vessel is filled by water,", end = '')

    def put_on(self):
        self.putting = True
        print(" put on the burner", end = '')


    def set_fire(self):
        self.ignition = True
        print(" and burner is ignited.\n")


class VesselUpdate(VesselPlacing):

    def pour_out(self):
        self.filling = True
        print("Vessel is empty.")
    

class Kettle(Vessel):

    def __init__(self):
        self.name = "Tefal kettle"
        self.volume = 1.7
        self.time = 5
        self.filling = False

#class SoupPot(Vessel):

    #def __init__(self):
        #self.name = "Tefal soup pot"
       # self.volume = 5
        #self.time = 10

    




