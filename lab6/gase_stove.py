class GaseBurner:

    def __init__(self, name, burner_status, burner_use, boost):
        self.name = name
        self.burner_status = burner_status
        self.burner_use = burner_use
        

class Burner(GaseBurner):

    def __init__(self):
        self.stove = [
            GaseBurner(name="small", burner_status=False, burner_use=False, boost = 0.5),
            GaseBurner(name="middle", burner_status=False, burner_use=False, boost = 1),
            GaseBurner(name="big", burner_status=False, burner_use=False, boost = 1.2),
            GaseBurner(name="large", burner_status=False, burner_use=False, boost = 1.75),
        ]

    def get_burners_info(self):
        report = ""
        for burner in self.stove:
            report += f"{burner.name} burner: burner status - {burner.burner_status}, burner use - {burner.burner_use}\n"
        print(report)

    def use_burner(self):
        for burner in self.stove:
            if burner.name: #if burner is choiced
                self.burner_status = True
                self.burner_use = True
            return f"{self.name}: burner status - {self.burner_status}, burner use - {self.burner_use}/" 
