"""
создайте класс `Plane`, наследник `Vehicle`
"""

from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload

class Plane(Vehicle):
    cargo: float = 0
    max_cargo: float = 100
    
    def __init__(self, weight, fuel, fuel_consumption, max_cargo):
        super().__init__(weight, fuel, fuel_consumption)
        self.max_cargo = max_cargo
        
    def load_cargo(self, cargo: float):
        if self.max_cargo < self.cargo + cargo:
            raise CargoOverload("Cargo over load")
        
        self.cargo += cargo
        
    def remove_all_cargo(self) -> float:
        removed_cargo = self.cargo
        self.cargo = 0
        
        return removed_cargo