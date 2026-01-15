from models.automobilis import Automobilis
from dataclasses import dataclass


@dataclass
class Elektromobilis(Automobilis):
    talpa: int
