#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'still_fox'
from abc import ABCMeta, abstractmethod


class QuackBehavior(metaclass=ABCMeta):
    @abstractmethod
    def quack(self):
        pass


class Quack(QuackBehavior):
    def quack(self):
        print("Quack")


class MuteQuack(QuackBehavior):
    def quack(self):
        print("<< Silence >>")


class Squack(QuackBehavior):
    def quack(self):
        print("Squack")