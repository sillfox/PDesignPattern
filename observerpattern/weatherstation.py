#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'still_fox'
from abc import ABCMeta, abstractmethod
from observerpattern.observer import Observer
from observerpattern.observable import Observable


class DisplayElement(metaclass=ABCMeta):
    @abstractmethod
    def display(self):
        pass


class GeneralDisplay(DisplayElement, Observer):
    def __init__(self, observable):
        self.observable = observable
        self.observable.add_observer(self)
        self.temperature = None
        self.humidity = None

    def display(self):
        print(
            "Current conditions: {0} F degress and {1} % humidity".format(
                self.temperature, self.humidity
            )
        )

    def update(self, observable, *args):
        if len(args) == 0:
            # pull
            self.temperature = self.observable.get_temperature()
            self.humidity = self.observable.get_humidity()
        else:
            # push
            self.temperature, self.humidity = args
        self.display()


class WeatherData(metaclass=ABCMeta):
    def __init__(self):
        self.temperature = None
        self.humidity = None
        self.pressure = None

    @abstractmethod
    def measurementsChanged(self):
        pass

    def set_measurements(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.measurementsChanged()

    def get_temperature(self):
        return self.temperature

    def get_humidity(self):
        return self.humidity

    def get_pressure(self):
        return self.pressure


class PullWeatherData(Observable, WeatherData):
    def __init__(self):
        super(PullWeatherData, self).__init__()


    def measurementsChanged(self):
        self.set_changed()
        # pull
        self.notify_observers()


class PushWeatherData(Observable, WeatherData):
    def measurementsChanged(self):
        self.set_changed()
        # push
        self.notify_observers(self.temperature, self.humidity)


if __name__ == '__main__':
    pull_weather_data = PullWeatherData()
    pull_display = GeneralDisplay(pull_weather_data)
    pull_weather_data.set_measurements(80, 65, 30.4)
    pull_weather_data.set_measurements(82, 70, 29.2)
    pull_weather_data.set_measurements(78, 90, 29.2)

    push_weather_data = PullWeatherData()
    push_display = GeneralDisplay(push_weather_data)
    push_weather_data.set_measurements(30, 22, 13.4)
    push_weather_data.set_measurements(33, 21, 13.4)