from abc import ABCMeta
from enum import Enum

class City(Object):

	def __init__(self, name, isLand, isSC):
		self.name = name
		self.isLand = isLand
		self.isSC = isSC
		self.neighbors = []
		self.troop = None

class Troop(Object):

	__metaclass__ = ABCMeta

	def __init__(self):
		self.city = None
		self.order = None

	def move(self, destination):
		if self.canMove(destination):
			self.city.troop = None
			destination.troop = self
			self.city = destination


class Order(Object):

	hold = 1
	move = 2
	support = 3
	convoy = 4


	def __init__(self, orderType, location, source, destination):
		self.orderType = orderType
		self.location = location
		self.source = source
		self.destination = destination

location
	location.troop ?= 0, 1, 2 #None, armyType, fleetType
	location.order ?= None
	location.isLand, location.isCoast, location.neighbors = [locations]
	location.isReachable(destination)

Map = [location1, location2]
moves = {}
convoys = {}

for order in orders:
	if order.orderType == supportType:
		# if not order.source.troop:
		# 	continue
		# if not order.source.order.orderType == moveType and order.source.order.destination == order.destination:
		# 	continue
		if not order.location.isReachable(order.destination):
			continue
		if order.destination in moves:
			if order.source in moves[order.destination]:
				moves[order.destination][order.source][1] += 1
			else:
				moves[order.destination][order.source] = (False, 1)
		else:
			moves[order.destination] = {order.source: (False, 1)}
	elif order.orderType == moveType:
		if order.destination in troops:
			s_order = order.destination.order
			if s_order.orderType == supportType and s_order.destination != order.location:
				if not s_order.source.isReachable(s_order.destination):
					continue
				if s_order.destination in moves:
					if s_order.source in moves[s_order.destination]:
						moves[s_order.destination][s_order.source][1] -= 1
					else:
						moves[s_order.destination][s_order.source] = (False, -1)
				else:
					moves[s_order.destination] = {s_order.source: (False, -1)}
		if order.destination in moves:
			if order.source in moves[order.destination]:
				moves[order.destination][order.source][0] = True
				moves[order.destination][order.source][1] += 1
			else:
				moves[order.destination][order.source] = (True, 1)
		else:
			moves[order.destination] = {order.source: (True, 1)}
	elif order.orderType == convoyType:
		if order.source.troop == armyType and order.destination.isLand

loop over orders
	if support, add 1 power to move in list of moves (supported destination must be reachable by supporting unit)
	if move, if unto a supporting order, remove 1 power from (supported) move in list of moves unless the target of the support is the moving piece
		add 1 power to move in list of moves and set is_executed to True
	if convoy
		add self to dictionary of convoys indexed by move
loop over moves with destination that are convoying
	greatest power = 0
	greatest source = None
	loop over sources
		if move is executed
		and if move is not possible via land route, check if convoys allow it
			if greater than greatest power
				set greatest power and greatest source
	if source != destination
		remove convoy from list of convoys
loop over other moves
	greatest power = 0
	greatest source = None
	loop over sources
		if move is executed
		and if move is not possible via land route, check if convoys allow it
			if greater than greatest power
				set greatest power and greatest source 

	

moves = {destination: {source: (is_executed, power), source2: (is_executed, power2)}}



class Game(Object):

	def __init__(self):
		self.cities = {}
		self.troops = []
		self.generateMap()

	def generateMap(self):
		addCity(City("London", True, True))

	def addCity(self, city, troop=False):
		self.cities[city.name] = city
		if troop:
			city.troop = troop
			troop.city = city
			self.troops.append(troop)

	def connectCities(self, city1, city2):
		self.cities[city1].neighbors.append(self.cities[city2])
		self.cities[city2].neighbors.append(self.cities[city1])





