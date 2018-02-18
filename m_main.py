from game import *

turn = 0    # init turn
accountList = [] # account list
accountList.append(objects.account(1,200,200)) # player1's account
accountList.append(objects.account(2,200,200)) # player2's account
player1 = objects.player(1,'player1',accountList[0],1,0)  # init player # position in 0
player2 = objects.player(2, 'player2', accountList[1],2,0)
player = player1
while True:

    # which player's turn and begin player
    if(turn%2 == 0): # player1's turn
        player = player1
    else:
        player = player2

    print("It is " + player.m_name + "'s turn.")

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
        get_community_chest(player)
    elif movetoplace.m_type == PlaceType.GOTOJAIL:
        turnnochange = True
        player.m_position = 10 # move to jail
    elif movetoplace.m_type ==PlaceType.STATION:
        station_action(player,movetoplace)
    elif movetoplace.m_type == PlaceType.UTILITY:
        utility_action(player,movetoplace)
    elif movetoplace.m_type == PlaceType.TAX:
        player.m_account.m_currencies -= 100 # pay tax
        player.m_account.m_balance -= 100
        #elif movetoplace.m_type == PlaceType.JAIL or movetoplace.m_type == PlaceType.PARKING:
    else:
        print('no action')

    if turnnochange == True:
        turn = turn
    else:
        turn += 1

    player.showAcountInfo()
    player1.showAcountInfo()
    player2.showAcountInfo()

    # whether one of player is bankrupt
    if IsBankrupt(player1):
        print("player: "+ player1.m_name + "is bankrupt.")
        print("Game over!")
    elif IsBankrupt(player2):
        print("player: " + player2.m_name + "is bankrupt.")
        print("Game over!")

    print("Do you want to quit?")
    if str(input()).startswith('y'):
        break

print("Game over!")
# To do:
# change list info to global variable, use id to access list