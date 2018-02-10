# -*- coding: utf-8 -*-
"""
Created on Sun Feb 4 2018

@author: ShulinLiu

Describes:
Classes and objects used in the play board
"""
from constant import PlaceType, StreetRent, StreetCost, StreetColor
from objects import position

def decor(func):
    def wrap():
        print("=================")
        func()
        print("=================")
    return wrap()

class deeds(object):
    """deeds of properties"""

    def __init__(self, owner=None, purchaseprice=0, mortgageValue=0, unmortage=0):
        super(deeds, self).__init__()
        self.m_owner = owner
        self.m_purchasePrice = purchaseprice
        self.m_mortgageValue = mortgageValue
        self.m_unmortage = unmortage

    # def getOwner(self):
    #     return self.m_owner

    # def getPrice(self):
    #     return self.m_purchasePrice

    # def getMortgageValue(self):
    #     return self.m_mortgageValue


class streetdeeds(deeds):
    """deeds of street"""

    # 7 kinds of rent price,and 2 kinds of costs
    def __init__(self, owner=None, purchaseprice=0, mortgageValue=0, unmortage=0,
                 rentprice=[0, 0, 0, 0, 0, 0, 0], cost=[0, 0]):
        self.m_owner = owner
        self.m_purchasePrice = purchaseprice
        self.m_mortgageValue = mortgageValue
        self.m_unmortage = unmortage
        self.m_rentPrice = rentprice
        self.m_cost = cost
    #
    # @decor # decorator
    # def showDeedInfo(self):
    #     print("Street price: " + str(self.m_purchasePrice))
    #     print("Mortgage value: " + str(self.m_mortgageValue))
    #     print("UnMortgage value: " + str(self.m_unmortgageValue))


class stationdeeds(deeds):
    """deeds of stations"""

    # 4 kinds of rent price
    def __init__(self, owner=None, purchaseprice=0, mortgageValue=0, unmortage=0,
                 rentprice=[0, 0, 0, 0]):
        self.m_owner = owner
        self.m_purchasePrice = purchaseprice
        self.m_mortgageValue = mortgageValue
        self.m_unmortage = unmortage
        self.m_rentPrice = rentprice


class utilitydeeds(deeds):
    """deeds of utilities"""

    def __init__(self, owner=None, purchaseprice=0, mortgageValue=0, unmortage=0,
                 rent=0):
        self.m_owner = owner
        self.m_purchasePrice = purchaseprice
        self.m_mortgageValue = mortgageValue
        self.m_unmortage = unmortage
        # self.m_rent = rent


class place(object):
    """base class for place in the play board"""

    # __type = PlaceType()

    # @classmethod
    # def _decorator(cls, func):
    #     # def wrap():
    #         print("=================")
    #         func()
    #         print("=================")
    #
    #     # return wrap()

    def __init__(self, name=None, types=None, position=None, owner=None, deed=None):
        super(place, self).__init__()
        self.m_name = name
        self.m_type = types
        self.m_position = position
        self.m_owner = owner
        self.m_deed = deed

    #
    #@_decorator
    def showPlaceInfo(self):
        print("Place Type: " + str(self.m_type))
        print("Place name: " + str(self.m_name))
        if not (self.m_owner is None):
            print("Owner: " + str(self.m_owner))
        else:
            print("Not belong to anyone.")

# place.showPlaceInfo =place._decorator(place.showPlaceInfo)


class go(place):
    """place: GO, first place in play board"""

    def __init__(self):
        self.m_name = 'GO'
        self.m_type = PlaceType.GO
        self.m_position = position(0, 0)
        self.m_owner = 'no'
        self.m_deed = None


class jail(place):
    """docstring for jail"""

    def __init__(self, arg):
        super(jail, self).__init__()
        self.m_name = 'Jail'
        self.m_type = PlaceType.JAIL
        self.m_position = position(10, 0)
        self.m_owner = 'no'
        self.m_deed = None


class chance(place):
    """docstring for chance"""

    def __init__(self, arg):
        super(chance, self).__init__()
        self.m_name = 'Chance'
        self.m_type = PlaceType.CHANCE
        # self.m_position = position(self, 10, 0)
        self.m_owner = 'no'
        self.m_deed = None


class communitychess(place):
    """docstring for chance"""

    def __init__(self, arg):
        super(chance, self).__init__()
        self.m_name = 'Community Chest'
        self.m_type = PlaceType.COMMUNITY_CHEST
        # self.m_position = position(self, 10, 0)
        self.m_owner = 'no'
        self.m_deed = None


class tax(place):
    """docstring for chance"""

    def __init__(self, arg):
        super(chance, self).__init__()
        self.m_name = 'Super Tax'
        self.m_type = PlaceType.TAX
        # self.m_position = position(self, 10, 0)
        self.m_owner = 'no'
        self.m_deed = None


######################## street ############################
# use dict store deeds of 22 streets
# key: name of the street
# value: deeds of the street
"""
structure of street id:
  colorID + groupID
 example:
    2 --- StreetColor = 2, PINK
    1 --- the 2nd item in group PINK, whitehall

"""
# To do: use streetid to access info,
# such as position, color, rent price


StreetDict = {}


def getStreetName(streetid):
    return NameDict.get(streetid)


def getStreetPosition(streetid):
    return PosDict.get(streetid)


def getStreetDeeds(streetid):
    # TO DO
    pass


class street(place):
    """Street: street in play board"""

    def __init__(self, streetid, owner='no'):
        self.m_name = getStreetName(streetid)  # street name
        self.m_type = PlaceType.STREET  # place type
        self.m_position = getStreetPosition(streetid)  # street position
        self.m_owner = owner  # street owner
        self.m_deed = getStreetDeeds(streetid)  # street deed


######################## utility ############################

def getUltilityDeed(name):
    pass


class utility(place):
    """docstring for utility"""

    def __init__(self, name):
        super(utility, self).__init__()
        self.m_name = name
        self.m_type = PlaceType.UTILITY
        self.m_deed = getUltilityDeed(name)


######################## station ############################

def getStationDeed(name):
    pass


class station(place):
    """docstring for station"""

    def __init__(self, name):
        super(station, self).__init__()
        self.name = name
        self.m_type = PlaceType.STATION
        self.m_deed = getStationDeed(name)

######################## station ############################

