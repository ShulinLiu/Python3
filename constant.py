# -*- coding: utf-8 -*-
"""
Created on Sun Feb 4 2018

@author: ShulinLiu

Describes:
Classes and objects used in the play board
"""


from enum import Enum, unique

class PlaceType(Enum):
    GO = 0
    STREET = 1
    STATION = 2
    UTILITY = 3
    CHANCE = 4
    COMMUNITY_CHEST = 5
    JAIL = 6
    TAX = 7

class StreetRent(Enum):
    RENT = 0
    RENTWITHCOLORSET = 1
    RENTWITH1 = 2
    RENTWITH2 = 3
    RENTWITH3 = 4
    RENTWITH4 = 5
    RENTHOTEL = 6

class StreetCost(Enum):
    HOUSECOST = 0
    HOTELCOST = 1

class StreetColor(Enum):
    GREY = 0
    SKYBLUE = 1
    PINK = 2
    ORINGE = 3
    RED = 4
    YELLOW = 5
    GREEN = 6
    BLUE = 7