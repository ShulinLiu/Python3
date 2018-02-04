# -*- coding: utf-8 -*-
"""
Created on Sun Feb 4 2018

@author: ShulinLiu

Describes:
Classes and objects used in the play board
"""
from constant import PlaceType,StreetRent,StreetCost,StreetColor
from objects import position

class deeds(object):
    """deeds of properties"""
    def __init__(self, owner=None, purchaseprice=0, mortgageValue=0, unmortage=0):
        super(deeds, self).__init__()
        self.m_owner = owner
        self.m_purchasePrice = purchaseprice
        self.m_mortgageValue = mortgageValue
        self.m_unmortage = unmortage

class streetdeeds(deeds):
    """deeds of street"""

    # 7 kinds of rent price,and 2 kinds of costs
    def __init__(self, owner=None, purchaseprice=0, mortgageValue=0, unmortage=0,
                 rentprice=[0,0,0,0,0,0,0],cost=[0,0]):
        self.m_owner = owner
        self.m_purchasePrice = purchaseprice
        self.m_mortgageValue = mortgageValue
        self.m_unmortage = unmortage
        self.m_rentPrice = rentprice
        self.m_cost = cost

class stationdeeds(deeds):
    """deeds of stations"""

    # 4 kinds of rent price
    def __init__(self, owner=None, purchaseprice=0, mortgageValue=0, unmortage=0,
                 rentprice=[0,0,0,0]):
        self.m_owner = owner
        self.m_purchasePrice = purchaseprice
        self.m_mortgageValue = mortgageValue
        self.m_unmortage = unmortage
        self.m_rentPrice = rentprice

class utilitydeeds(deeds):
    """deeds of utilities"""

    def __init__(self, owner=None, purchaseprice=0, mortgageValue=0, unmortage=0,
                 rent= 0):
        self.m_owner = owner
        self.m_purchasePrice = purchaseprice
        self.m_mortgageValue = mortgageValue
        self.m_unmortage = unmortage
        self.m_rent = rent

class place(object):
    """base class for place in the play board"""
    # __type = PlaceType()

    def __init__(self, name=None,types=None,position=None,owner=None):
        super(place, self).__init__()
        self.m_name = name
        self.m_type = types
        self.m_position = position
        self.m_owner = owner

class go(place):
    """place: GO, first place in play board"""

    def __init__(self):
        self.m_name = 'GO'
        self.m_type = PlaceType.GO
        self.m_position = position(self, 0, 0)
        self.m_owner = 'no'

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
    pass

def getStreetPosition(streetid):
    pass

class street(place):
    """Street: street in play board"""

    def __init__(self,streetid,owner='no'):
        self.m_name = getStreetName(streetid)
        self.m_type = PlaceType.STREET
        self.m_position = getStreetPosition(streetid)
        self.m_owner = owner
        # self.m_position = position
        # self.m_owner = owner