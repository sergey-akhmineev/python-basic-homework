"""
создайте класс `Car`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02.engine import Engine


class Car(Vehicle):

    def __init__(self, weight=Vehicle.default_weight, fuel=Vehicle.default_fuel,
                 fuel_consumption=Vehicle.default_fuel_consumption, engine=100):
        Vehicle.__init__(self, weight=weight, fuel=fuel, fuel_consumption=fuel_consumption)
        self.engine = engine

    def set_engine(self, engine):
        self.engine = engine