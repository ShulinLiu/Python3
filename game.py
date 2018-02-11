# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 2018

@author: ShulinLiu

Describes:
logic method design to play game

"""
# -*- coding: utf-8 -*-

import place

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
layoutList = SinCycLinkedlist()
layoutList.add(place.go())
layoutList.add(place.street(00, 1))
layoutList.add(place.communitychess(2))
layoutList.add(place.street(01, 3))
layoutList.add(place.tax(4))
layoutList.add(place.station("KING CROSS STATION",5))

turn = 0 #initial turn number

def getTurn(turnNum):
    pass

def makeMove(moveNum):
    pass

def getPlaceInfo(position):
    pass

def IsBankrupt(player):
    pass

while True:
    turn = 0    # init turn
    player1 = player()  # init player
    player2 = player()
    inplay = player1

    if(turn%2 == 0): # player1's turn
        getDice()

