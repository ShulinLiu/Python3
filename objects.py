# -*- coding: utf-8 -*-
"""
Created on Sun Feb 4 2018

@author: ShulinLiu

Describes:
Classes and objects used in monopoly game
"""
# class position:
#     """XY coordinate"""
#
#     def __init__(self, x=0, y=0):
#         self.X = x
#         self.Y = y

class account(object):
    """Account info class"""

    def __init__(self, id=-1, currencies=0, balance=0, streetlist=[],
                 stationlist=[], utilitylist=[], mortgagelist=[]):
        self.m_accountID = id
        self.m_streetList = streetlist
        self.m_stationList = stationlist
        self.m_utilityList = utilitylist
        self.m_mortgageList = mortgagelist
        self.m_currencies = currencies
        self.m_balance = balance

    def showAccountInfo(self):
        print("Account ID: " + str(self.m_accountID))
        print("balance: " + str(self.m_balance))
        print("Currencies: " + str(self.m_currencies))
        if self.m_streetList != []:
            print("street: ")
            list = self.m_streetList.copy()
            while list != []:
                print(list.pop().m_name)
            # print(self.m_streetList)
        if self.m_stationList != []:
            print("station: ")
            list = self.m_stationList.copy()
            while list != []:
                print(list.pop().m_name)
            # print(self.m_stationList)
        if self.m_utilityList != []:
            print("utility: ")
            list = self.m_utilityList.copy()
            while list != []:
                print(list.pop().m_name)
            # print(self.m_utilityList)


class player(object):
    """The base class for player"""
    # __pID = -1  # not valid

    def __init__(self, pid=-1, name=None, account=None,token=None,position=None):
        super(player, self).__init__()
        self.__pID = pid
        self.m_name = name
        self.m_account = account
        self.m_token = token
        self.m_position = position

    def isvalid(self):
        if(self.__pID == -1):
            return False
        else:
            return True

    def getName(self):
        return self.m_name

    def getCurrentPos(self):
        return self.m_position

    def getToken(self):
        return self.m_token

    def showAcountInfo(self):
        # print("Player ID: " + self.m_nameID)
        # print("Token: " + self.m_token)
        print("Current Position: " + str(self.m_position))
        if(self.m_account == None):
            print("Error: account info is not valid!")
            return False
        else:
            self.m_account.showAccountInfo()
            return True




