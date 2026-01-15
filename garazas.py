from models.automobilis import Automobilis
from models.elektromobilis import Elektromobilis


class Garazas:
    def __init__(self):
        self.automobiliai = []

    def prideti_auto(self):
        marke = input("Markė: ")
        modelis = input("Modelis: ")
        metai = int(input("Metai: "))
        auto = Automobilis(marke, modelis, metai)
        self.automobiliai.append(auto)

    def prideti_elektro(self):
        marke = input("Markė: ")
        modelis = input("Modelis: ")
        metai = int(input("Metai: "))
        talpa = int(input("Talpa: "))
        auto = Elektromobilis(marke, modelis, metai, talpa)
        self.automobiliai.append(auto)

    def atvaizduoti_auto(self):
        for auto in self.automobiliai:
            print(auto)
           