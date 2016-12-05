#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'still_fox'
from abc import ABCMeta, abstractmethod


class Observer(metaclass=ABCMeta):
    @abstractmethod
    def update(self, observable, *args):
        """
        这个是开放给observable用于更新数据的接口。
        具体的子类中应该根据使用push、pull的不同方式，确定是否传入参数。
        """
        pass