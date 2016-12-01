#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'still_fox'
from abc import ABCMeta, abstractmethod
from strategypattern.flybehavior import (
    FlyBehavior, FlyWithWings, FlyNoWay, FlyRocketPowered
)
from strategypattern.quackbehavior import QuackBehavior, Quack


class Duck(metaclass=ABCMeta):
    def __init__(self):
        self._quack_behavior = None
        self._fly_behavior = None

    @abstractmethod
    def display(self):
        pass

    @property
    def fly_behavior(self):
        return self._fly_behavior

    @fly_behavior.setter
    def fly_behavior(self, fly_behavior):
        if isinstance(fly_behavior, FlyBehavior):
            self._fly_behavior = fly_behavior
        else:
            raise TypeError("Must be FlyBehavior subclass instance.")

    def perform_fly(self):
        if self._fly_behavior:
            self._fly_behavior.fly()
        else:
            raise AttributeError("Must set fly_behavior first.")

    @property
    def quack_behavior(self):
        return self._quack_behavior

    @quack_behavior.setter
    def quack_behavior(self, quack_behavior):
        if isinstance(quack_behavior, QuackBehavior):
            self._quack_behavior = quack_behavior
        else:
            raise TypeError("Must be QuackBehavior subclass instance.")

    def perform_quack(self):
        if self._quack_behavior:
            self._quack_behavior.quack()
        else:
            raise AttributeError("Must set quack_behavior first.")


class MallardDuck(Duck):
    def __init__(self):
        super(MallardDuck, self).__init__()
        self._quack_behavior = Quack()
        self._fly_behavior = FlyWithWings()

    def display(self):
        print("I'm a real Mallard duck")


class ModelDuck(Duck):
    def __init__(self):
        super(ModelDuck, self).__init__()
        self._quack_behavior = Quack()
        self._fly_behavior = FlyNoWay()

    def display(self):
        print("I'm a model duck")


if __name__ == "__main__":
    mallard = MallardDuck()
    mallard.perform_fly()
    mallard.perform_quack()

    model = ModelDuck()
    model.perform_fly()
    model.fly_behavior = FlyRocketPowered()
    model.perform_fly()

