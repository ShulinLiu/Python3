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
    GOTOJAIL = 7
    TAX = 8
    PARKING = 9

class StreetID(Enum):
    OLD_KENT_ROAD = 0
    WHITECHAPEL_ROAD = 1
    THE_ANGEL_ISLINGTON = 2
    EUSTON_ROAD = 3
    PENTONVILLE_ROAD = 4
    PALL_MALL = 5
    WHITEHALL = 6
    NORTHUMBND_AVENUE = 7
    BOW_STREET = 8
    MARLBOROUGH_STREET = 9
    VINE_STREET = 10
    STRAND = 11
    FLEET_STREET = 12
    TRAFALGAR_SQUARE = 13
    LEICHESTER_SQUARE = 14
    COVENTRY_STREET = 15
    PICCADILLY = 16
    REGENT_STREET = 17
    OXFORD_STREET = 18
    BOND_STREET = 19
    PARK_LINE = 20
    MAYFAIR = 21


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