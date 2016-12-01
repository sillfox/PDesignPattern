#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'still_fox'
from abc import ABCMeta, abstractmethod


class FlyBehavior(metaclass=ABCMeta):
    @abstractmethod
    def fly(self):
        pass


class FlyWithWings(FlyBehavior):
    def fly(self):
        print("I'm flying!")


class FlyNoWay(FlyBehavior):
    def fly(self):
        print("I can't fly.")


class FlyRocketPowered(FlyBehavior):
    def fly(self):
        print("I'm flying with a rocket!")
