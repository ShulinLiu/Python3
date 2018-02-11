# -*- coding: utf-8 -*-
"""
Created on Sun Feb 4 2018

@author: ShulinLiu

Describes:
Classes and objects used in the play board
"""
from constant import PlaceType, StreetRent, StreetCost, StreetColor
# from objects import position

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

    def showDeedInfo(self):
        print("## Deed Info ##")
        if not (self.m_owner is None):
            print("Owner: " + str(self.m_owner))
        else:
            print("Not belong to anyone.")
        print("Purchase Price: " + str(self.m_purchasePrice))
        print("Mortgage Value: " + str(self.m_mortgageValue))
        print("Un-mortgage Price: " + str(self.m_unmortage))
        # print("###############################")

    # def getOwner(self):
    #     return self.m_owner

    # def getPrice(self):
    #     return self.m_purchasePrice

    # def getMortgageValue(self):
    #     return self.m_mortgageValue


class streetdeeds(deeds):
    """deeds of street"""

    # 7 kinds of rent price,and 2 kinds of costs
    def __init__(self, purchaseprice=0, mortgageValue=0, unmortage=0,
                 rentprice=[0, 0, 0, 0, 0, 0, 0], cost=[0, 0], owner=None):
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
    def __init__(self, purchaseprice=0, mortgageValue=0, unmortage=0,
                 rentprice=[0, 0, 0, 0], owner=None):
        self.m_owner = owner
        self.m_purchasePrice = purchaseprice
        self.m_mortgageValue = mortgageValue
        self.m_unmortage = unmortage
        self.m_rentPrice = rentprice


class utilitydeeds(deeds):
    """deeds of utilities"""

    def __init__(self, purchaseprice=0, mortgageValue=0, unmortage=0,
                 rent=0, owner=None):
        self.m_owner = owner
        self.m_purchasePrice = purchaseprice
        self.m_mortgageValue = mortgageValue
        self.m_unmortage = unmortage
        self.m_rent = rent


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
        print("============ Info ============")
        print("Place Type: " + str(self.m_type))
        print("Place name: " + str(self.m_name))
        if not (self.m_owner is None): # show owner info
            print("Owner: " + str(self.m_owner))
        else:
            print("Not belong to anyone.")

        print("Posiition: " + str(self.m_position))
        # if(self.m_position is None): # show position info
        #     print("No position info.")
        # else:
        #     print("Place position: (" + str(self.m_position.X) +","+str(self.m_position.Y) +")")

        if(self.m_deed is None): # show deed info
            print("No deed info.")
        else:
            self.m_deed.showDeedInfo()

        print("==============================")

# place.showPlaceInfo =place._decorator(place.showPlaceInfo)


class go(place):
    """place: GO, first place in play board"""

    def __init__(self):
        self.m_name = 'GO'
        self.m_type = PlaceType.GO
        self.m_position = 0
        # self.m_position = position(0, 0)
        self.m_owner = 'no'
        self.m_deed = None


class jail(place):
    """docstring for jail"""

    def __init__(self):
        super(jail, self).__init__()
        self.m_name = 'Jail'
        self.m_type = PlaceType.JAIL
        self.m_position = 10
        # self.m_position = position(10, 0)
        self.m_owner = 'no'
        self.m_deed = None

class parking(place):
    """docstring for jail"""

    def __init__(self):
        super(parking, self).__init__()
        self.m_name = 'FreeParking'
        self.m_type = PlaceType.PARKING
        self.m_position = 20
        # self.m_position = position(10, 0)
        self.m_owner = 'no'
        self.m_deed = None

class gotojail(place):
    """docstring for jail"""

    def __init__(self):
        super(gotojail, self).__init__()
        self.m_name = 'GoToJail'
        self.m_type = PlaceType.GOTOJAIL
        self.m_position = 30
        # self.m_position = position(10, 0)
        self.m_owner = 'no'
        self.m_deed = None

class chance(place):
    """docstring for chance"""

    def __init__(self, position):
        super(chance, self).__init__()
        self.m_name = 'Chance'
        self.m_type = PlaceType.CHANCE
        self.m_position = position
        self.m_owner = 'no'
        self.m_deed = None


class communitychess(place):
    """docstring for chance"""

    def __init__(self, position):
        super(communitychess, self).__init__()
        self.m_name = 'Community Chest'
        self.m_type = PlaceType.COMMUNITY_CHEST
        self.m_position = position
        self.m_owner = 'no'
        self.m_deed = None


class tax(place):
    """docstring for chance"""

    def __init__(self,name, position):
        super(tax, self).__init__()
        self.m_name = name
        self.m_type = PlaceType.TAX
        self.m_position = position
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

# encoding: utf-8
def load_dict_from_file(filepath):
    _dict = {}
    try:
        dict_file =  open(filepath, 'r')
        for line in dict_file:
            (key, value) = line.strip().split('\t')
            _dict[int(key)] = value
    except IOError as ioerr:
        print ("文件 %s 不存在" % (filepath))

    return _dict

NameDict = load_dict_from_file ('namedict.txt')

StreetDict = {}

def getStreetName(streetid):
    return NameDict.get(streetid)


# def getStreetPosition(streetid):
#     return PosDict.get(streetid)


def getStreetDeeds(streetid):
    # hard code first
    if streetid == 0:
        return streetdeeds(60,30,33,[2,4,10,30,90,160,250], [50,50])
    elif streetid == 1:
        return streetdeeds(60, 30, 33, [4,8,20,60,180,320,450], [50,50])
    elif streetid == 10:
        return streetdeeds(100, 50, 55, [6, 12, 30, 90, 270, 400, 550], [50, 50])
    elif streetid == 11:
        return streetdeeds(100, 50, 55, [6, 12, 30, 90, 270, 400, 550], [50, 50])
    elif streetid == 12:
        return streetdeeds(120, 60, 66, [8, 16, 40, 100, 300, 450, 600], [50, 50])
    elif streetid == 20:
        return streetdeeds(140, 50, 55, [10, 20, 50, 150, 450, 625, 750], [100, 100])
    elif streetid == 21:
        return streetdeeds(140, 50, 55, [10, 20, 50, 150, 450, 625, 750], [100, 100])
    elif streetid == 22:
        return streetdeeds(160, 50, 55, [12, 24, 60, 180, 500, 700, 900], [100, 100])
    # elif streetid == 30:
    #     return streetdeeds(140, 50, 55, [10, 20, 50, 150, 450, 625, 750], [100, 100])
    # elif streetid == 31:
    #     return streetdeeds(140, 50, 55, [10, 20, 50, 150, 450, 625, 750], [100, 100])
    # elif streetid == 32:
    #     return streetdeeds(160, 50, 55, [12, 24, 60, 180, 500, 700, 900], [100, 100])
    else:
        return streetdeeds(400, 50, 55, [12, 24, 60, 180, 500, 700, 900], [100, 100])

class street(place):
    """Street: street in play board"""

    def __init__(self, streetid, position, owner='no'):
        self.m_name = getStreetName(streetid)  # street name
        self.m_type = PlaceType.STREET  # place type
        self.m_position = position  # street position
        self.m_owner = owner  # street owner
        self.m_deed = getStreetDeeds(streetid)  # street deed


######################## utility ############################

def getUltilityDeed(name):
    # use hard word first
    # To do: change to read from file
    if name == "WATER WORKS":
        return utilitydeeds(150, 75, 83)
    elif name == "ELECTRIC COMPANY":
        return utilitydeeds(150, 75, 83)
    else:
        print("Not valid utility!")
        return None


class utility(place):
    """docstring for utility"""

    def __init__(self, name, position):
        super(utility, self).__init__()
        self.m_name = name
        self.m_type = PlaceType.UTILITY
        self.m_position = position
        self.m_deed = getUltilityDeed(name)


######################## station ############################

def getStationDeed(name):
    if name == "KING CROSS STATION" or name == "MARYLEBONE STATION"\
            or name == "FENCHURCH STREET STATION" or name == "LIVERPOOL STREET STATION":
        return stationdeeds(200, 100, 110, [25, 50, 100, 200])
    else:
        print("station error.")
    # elif name == "MARYLEBONE STATION":
    #     return stationdeeds(200,100,110,[25,50,100,200])

class station(place):
    """docstring for station"""

    def __init__(self, name, position):
        super(station, self).__init__()
        self.name = name
        self.m_position = position
        self.m_type = PlaceType.STATION
        self.m_deed = getStationDeed(name)

######################## station ############################

