from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel

class Vehicle(ABC):
    weight: int = 1500
    started: bool = False
    fuel: float = 115.5
    fuel_consumption: float = 6.5

    def __init__(self, weight, fuel, fuel_consumption):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        
    def start(self):
        if not self.started:
            if self.fuel > 0:
                self.started = True
            else:
                raise LowFuelError("Low fuel level")
            
    def move(self, distance_km: float):
       fuel_consumption_per_distance = distance_km * self.fuel_consumption
       
       if self.fuel < fuel_consumption_per_distance:
           raise NotEnoughFuel("Not enough fuel")
       
       self.fuel -= fuel_consumption_per_distance