from place import *

# Go = go()

# Go.showPlaceInfo()

# Jail = jail()

# Jail.showPlaceInfo()

# water = utility("WATER WORKS")

# water.showPlaceInfo()

# street = street(21,3)

# street.showPlaceInfo()

# print(NameDict)
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

# test for place
layoutList[38].showPlaceInfo()