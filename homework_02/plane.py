"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02 import exceptions
from homework_02.base import Vehicle


class Plane(Vehicle):
    max_cargo = 2500
    cargo = 0

    def __init__(self, weight, fuel, fuel_consumption, max_cargo, cargo=0):
        Vehicle.__init__(self, weight=weight, fuel=fuel, fuel_consumption=fuel_consumption)
        self.cargo = cargo
        self.max_cargo = max_cargo

    def load_cargo(self, expect_cargo):
        sum_cargo = self.cargo + expect_cargo
        if sum_cargo <= self.max_cargo:
            self.cargo = expect_cargo
            return self.cargo
        else:
            raise exceptions.CargoOverload

    def remove_all_cargo(self):
        result = self.cargo
        self.cargo = 0
        return result