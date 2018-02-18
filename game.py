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
import random

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
    dice1 = random.randint(1,7)
    dice2 = random.randint(1,7)
    return (dice1 + dice2)

def getTurn(turnNum):
    pass

def makeMove(player, moveNum):
    print(player.m_name + " move "+ str(moveNum) + " steps.")
    player.m_position += moveNum


def getPlaceInfo(position):
    pass

def IsBankrupt(player):
    if player.m_account.m_currencies <= 0 and player.m_account.m_balance <=0:
        return True
    else:
        return False

def auction(place):
    # auction for place
    print("Auction begin:")
    place.showPlaceInfo()
    print("Player1: " + player1.m_name + " please offer your price:")
    # if not (int(input()))
    price1 = int(input())
    print("Player2: " + player2.m_name + " please offer your price:")
    # if not (int(input()))
    price2 = int(input())
    while price1 != 0 or price2 != 0:
        if price1 < price2:
            print("Player1: " + player1.m_name + " would you like to offer another price or quit?")
            if str(input()).startswith('y'):
                winner = player2
                pirce = price2
                break
            else:
                price1 = int(input())
        else:
            print("Player2: " + player2.m_name + " would you like to offer another price or quit?")
            if str(input()).startswith('y'):
                winner = player1
                price = price1
                break
            else:
                price1 = int(input())

    if winner.m_account.m_currencies < place.m_deed.m_purchasePrice:
        winner.m_account.m_currencies -= price
        if place.m_type == PlaceType.STREET:
            winner.m_account.m_streetList.append(place)
        elif place.m_type == PlaceType.STATION:
            winner.m_account.m_stationList.append(place)
        elif place.m_type == PlaceType.UTILITY:
            winner.m_account.m_utilityList.append(place)
        else:
            print("Wrong place for auction!")


def pay_rent(player, place):
    if player.m_name == place.m_owner:
        # no need to pay rent
        return
    else:
        if player1.m_name == place.m_owner:
            owner = player1
        elif player2.m_name == place.m_owner:
            owner = player2
        else:
            print("Error, no one own this property!")

        if place.m_type == PlaceType.STREET:
            print("player " + player.m_name + " need to pay rent: "+ str(place.m_deed.m_rentPrice))
            player.m_account.m_currencies = player.m_account.m_currencies - place.m_deed.m_rentPrice[0]
            player.m_account.m_balance = player.m_account.m_balance - place.m_deed.m_rentPrice[0]
            owner.m_account.m_currencies = owner.m_account.m_currencies - place.m_deed.m_rentPrice[0]
            owner.m_account.m_balance = owner.m_account.m_balance - place.m_deed.m_rentPrice[0]
        elif place.m_type == PlaceType.STATION:
            print("player " + player.m_name + " need to pay rent: "+ str(place.m_deed.m_rentPrice[0]))
            player.m_account.m_currencies = player.m_account.m_currencies - place.m_deed.m_rentPrice[0]
            player.m_account.m_balance = player.m_account.m_balance - place.m_deed.m_rentPrice[0]
            owner.m_account.m_currencies = owner.m_account.m_currencies - place.m_deed.m_rentPrice[0]
            owner.m_account.m_balance = owner.m_account.m_balance - place.m_deed.m_rentPrice[0]
        elif place.m_type == PlaceType.UTILITY:
            print("player " + player.m_name + " need to pay rent: "+ str(place.m_deed.m_rent))
            player.m_account.m_currencies = player.m_account.m_currencies - place.m_deed.m_rent
            player.m_account.m_balance = player.m_account.m_balance - place.m_deed.m_rent
            owner.m_account.m_currencies = owner.m_account.m_currencies - place.m_deed.m_rent
            owner.m_account.m_balance = owner.m_account.m_balance - place.m_deed.m_rent

def street_action(player, place):
    # actions when player move to a street
    if place.m_owner is None or place.m_owner == 'no':  # no one own it now
        place.showPlaceInfo()
        print(player.m_name + ', do you want to buy it?')
        if str(input()).startswith('y'):
            # while (player.m_account.m_balance >= place.m_deed.m_purchasePrice
            #     and player.m_account.m_currencies < place.m_deed.m_purchasePrice):
                # print('Your currencies is not enough.\nDo you want to mortgage a porperties?')
                # if str(input().startswith() == 'y'):
                # else:
                #     break
            if player.m_account.m_currencies >= place.m_deed.m_purchasePrice:
                # buy a street
                player.m_account.m_currencies = player.m_account.m_currencies - place.m_deed.m_purchasePrice
                player.m_account.m_streetList.append(place)
                place.m_deed.m_owner = player.m_name
        else:
            # go auction
            auction(place)

    elif place.m_owner == player.m_name:
        return

    else:
        # other player own this street
        print(place.m_owner + " own this place.")
        pay_rent(player, place)

def get_chance(player):
    print("player: "+ player.m_name + " get chance.")

def get_community_chest(player):
    print("player: " + player.m_name + " get community chest.")

def station_action(player,place):
    if place.m_owner is None or place.m_owner == 'no':  # no one own it now
        place.showPlaceInfo()
        print(player.m_name + ', do you want to buy it?')
        if str(input()).startswith('y'):
            # while (player.m_account.m_balance >= place.m_deed.m_purchasePrice
            #     and player.m_account.m_currencies < place.m_deed.m_purchasePrice):
                # print('Your currencies is not enough.\nDo you want to mortgage a porperties?')
                # if str(input().startswith() == 'y'):
                # else:
                #     break
            if player.m_account.m_currencies >= place.m_deed.m_purchasePrice:
                # buy a street
                player.m_account.m_currencies = player.m_account.m_currencies - place.m_deed.m_purchasePrice
                player.m_account.m_stationList.append(place)
                place.m_deed.m_owner = player.m_name
        else:
            # go auction
            auction(place)

    elif place.m_owner == player.m_name:
        return

    else:
        # other player own this street
        print(place.m_owner + " own this place.")
        pay_rent(player, place)

def utility_action(player,place):
    if place.m_owner is None or place.m_owner == 'no':  # no one own it now
        place.showPlaceInfo()
        print(player.m_name + ', do you want to buy it?')
        if str(input()).startswith('y'):
            # while (player.m_account.m_balance >= place.m_deed.m_purchasePrice
            #     and player.m_account.m_currencies < place.m_deed.m_purchasePrice):
                # print('Your currencies is not enough.\nDo you want to mortgage a porperties?')
                # if str(input().startswith() == 'y'):
                # else:
                #     break
            if player.m_account.m_currencies >= place.m_deed.m_purchasePrice:
                # buy a street
                player.m_account.m_currencies = player.m_account.m_currencies - place.m_deed.m_purchasePrice
                player.m_account.m_utilityList.append(place)
                place.m_deed.m_owner = player.m_name
        else:
            # go auction
            auction(place)

    elif place.m_owner == player.m_name:
        return

    else:
        # other player own this utility
        print(place.m_owner + " own this place.")
        pay_rent(player, place)



