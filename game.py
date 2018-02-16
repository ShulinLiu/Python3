# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 2018

@author: ShulinLiu

Describes:
logic method design to play game

"""
# -*- coding: utf-8 -*-

from place import *
from constant import *
import objects

class Node:
    def __init__(self, initdata):
        self.__data = initdata
        self.__next = None

    def getData(self):
        return self.__data

    def getNext(self):
        return self.__next

    def setData(self, newdata):
        self.__data = newdata

    def setNext(self, newnext):
        self.__next = newnext

class SinCycLinkedlist:
    def __init__(self):
        self.head = Node(None)
        self.head.setNext(self.head)

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head.getNext())
        self.head.setNext(temp)

    def remove(self, item):
        prev = self.head
        while prev.getNext() != self.head:
            cur = prev.getNext()
            if cur.getData() == item:
                prev.setNext(cur.getNext())
            prev = prev.getNext()

    def search(self, item):
        cur = self.head.getNext()
        while cur != self.head:
            if cur.getData() == item:
                return True
            cur = cur.getNext()

        return False

    def empty(self):
        return self.head.getNext() == self.head

    def size(self):
        count = 0
        cur = self.head.getNext()
        while cur != self.head:
            count += 1
            cur = cur.getNext()

        return count

# init layout list
# layoutList = SinCycLinkedlist()
# layoutList.add(place.go())
# layoutList.add(place.street(00, 1))
# layoutList.add(place.communitychess(2))
# layoutList.add(place.street(01, 3))
# layoutList.add(place.tax(4))
# layoutList.add(place.station("KING CROSS STATION",5))

layoutList = []
layoutList.append(go())
# layoutlist[0].showPlaceInfo()
layoutList.append(street(00, 1))
layoutList.append(communitychess(2))
layoutList.append(street(1, 3))
layoutList.append(tax("Income tax", 4))
layoutList.append(station("KING CROSS STATION",5))
layoutList.append(street(10, 6))
layoutList.append(chance(7))
layoutList.append(street(11,8))
layoutList.append(street(12,9))
layoutList.append(jail())

layoutList.append(street(20,11))
layoutList.append(utility("ELECTRIC COMPANY",12))
layoutList.append(street(21,13))
layoutList.append(street(22,14))
layoutList.append(station("MARYLEBONE STATION",15))
layoutList.append(street(30,16))
layoutList.append(communitychess(17))
layoutList.append(street(31,18))
layoutList.append(street(32,19))
layoutList.append(parking())

layoutList.append(street(40,21))
layoutList.append(chance(22))
layoutList.append(street(41,23))
layoutList.append(street(42,24))
layoutList.append(station("FENCHURCH STREET STATION",25))
layoutList.append(street(50,26))
layoutList.append(street(51,27))
layoutList.append(utility("WATER WORKS",28))
layoutList.append(street(52,29))
layoutList.append(gotojail())

layoutList.append(street(60,31))
layoutList.append(street(61,32))
layoutList.append(communitychess(33))
layoutList.append(street(62,34))
layoutList.append(station("LIVERPOOL STREET STATION",35))
layoutList.append(chance(36))
layoutList.append(street(70,37))
layoutList.append(tax("Super Tax",38))
layoutList.append(street(71,39))

turn = 0 #initial turn number
def getDice():
    pass

def getTurn(turnNum):
    pass

def makeMove(player, moveNum):
    player.m_position += moveNum


def getPlaceInfo(position):
    pass

def IsBankrupt(player):
    pass

def auction(place):
    # auction for place
    pass

def pay_rent(player, place):
    pass

def street_action(player, place):
    # actions when player move to a street
    if place.m_owner is None:  # no one own it now
        place.showPlaceInfo()
        print(player.m_name + ', do you want to buy it?')
        if str(input()).startswith() == 'y':
            # while (player.m_account.m_balance >= place.m_deed.m_purchasePrice
            #     and player.m_account.m_currencies < place.m_deed.m_purchasePrice):
                # print('Your currencies is not enough.\nDo you want to mortgage a porperties?')
                # if str(input().startswith() == 'y'):
                # else:
                #     break
            if player.m_account.m_currencies < place.m_deed.m_purchasePrice:
                # buy a street
                player.m_account.m_currencies -= place.m_deed.m_purchasePrice
                player.m_account.m_streetList.append(place)
        else:
            # go auction
            auction(place)

    elif place.m_owner == player.m_name:
        return

    else:
        # other player own this street
        pay_rent(player,place)

def get_chance(player):
    pass

while True:
    turn = 0    # init turn
    accountList = [] # account list
    accountList.append(objects.account(1,200,200)) # player1's account
    accountList.append(objects.account(2,200,200)) # player2's account
    player1 = objects.player(1,'player1',accountList[0],1,0)  # init player # position in 0
    player2 = objects.player(2, 'player2', accountList[1],2,0)

    # which player's turn and begin player
    if(turn%2 == 0): # player1's turn
        player = player1
    else:
        player = player2

    # player games
    turnnochange = False
    move = getDice()
    makeMove(player, move)

        # judge witch place player is, and what action should he do
    movetoplace = layoutList[player.getCurrentPos()]
    if movetoplace.m_type == PlaceType.STREET:
        # move to street, need buy or pay rent
        street_action(player, movetoplace)
    elif movetoplace.m_type == PlaceType.CHANCE:
        # get chance
        get_chance(player)
    elif movetoplace.m_type ==PlaceType.COMMUNITY_CHEST:
        get_community_chest(player1)
    elif movetoplace.m_type == PlaceType.GOTOJAIL:
        turnnochange = True
        player1.m_position = 10 # move to jail
    elif movetoplace.m_type ==PlaceType.STATION:
        station_action(player1,movetoplace)
    elif movetoplace.m_type == PlaceType.UTILITY:
        utility_action(player1,movetoplace)
    elif movetoplace.m_type == PlaceType.TAX:
        player1.m_account.m_currencies -= 100 # pay tax
        player1.m_account.m_balance -= 100
        #elif movetoplace.m_type == PlaceType.JAIL or movetoplace.m_type == PlaceType.PARKING:
    else:
        print('no action')

    if(turnnochange):
        turn = turn
    else:
        turn += 1


