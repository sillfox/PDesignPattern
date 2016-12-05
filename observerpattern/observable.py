#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'still_fox'


class Observable(object):
    def __init__(self):
        self.changed = False
        self.observers = list()

    def add_observer(self, observer):
        self.observers.append(observer)

    def delete_observer(self, observer):
        if observer in self.observers:
            self.observers.remove(observer)

    def notify_observers(self, *args):
        """
        通过是否传递参数来判断更新数据的方式是采用push还是pull。
        如果没有传入参数，则使用pull的方式：observer主动从observable获取。
        如果有传入参数，则使用push的方式：observable通过update方法推送数据。
        """
        if len(args) == 0:
            # pull
            for obs in self.observers:
                obs.update(self)
        elif len(args) > 0:
            # push
            for obs in self.observers:
                obs.update(self, *args)

    def set_changed(self):
        self.changed = True

    def get_changed(self):
        return self.changed

    def has_changed(self):
        return self.changed == True
