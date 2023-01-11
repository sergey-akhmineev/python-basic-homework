from abc import ABC
from homework_02 import exceptions

class Vehicle(ABC):
    pass
    default_weight = 1000
    default_fuel = 10
    default_fuel_consumption = 25

    def __init__(self, weight, fuel, fuel_consumption, started=False):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.started = started

    def start(self):
        if self.fuel > 0:
            self.started = True
        else:
            raise exceptions.LowFuelError

    def move(self, distance):
        expected_fuel_to_spend = distance * self.fuel_consumption
        if expected_fuel_to_spend > self.fuel:
            raise exceptions.NotEnoughFuel
        self.fuel -= expected_fuel_to_spend