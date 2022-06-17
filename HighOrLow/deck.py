import random
from card import Card

class Deck():
	SUIT_TUPLE = ('spades', 'hearts', 'clubs', 'diamonds')
	STANDARD_DICT = {'ace':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'jack':11, 'queen':12, 'king':13}

	def __init__(self, window, rankValueDict=STANDARD_DICT):


		self.startingDeckList = []
		self.plaingDeckList = []
		for suit in Deck.SUIT_TUPLE:
			for rank, value in rankValueDict.items():
				oCard = Card(window, rank, suit, value)
				self.startingDeckList.append(oCard)
		self.shuffle()

	def shuffle(self):
		self.playingDeckList - self.startingDeckList.copy()
		for oCard in self.playingDeckList:
			oCard.conceal()
		random.shuffle(self.playingDeckList)

	def getCard(self):
		if len(self.playingDeckList) == 0:
			raise IndexError('No more cards')
		oCard = self.playingDeckList.pop()
		return oCard

	def returnCardToDeck(self, oCard):
		self.playingDeckList.insert(0, oCard)