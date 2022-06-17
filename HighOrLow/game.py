import pygwidgets
from card import Card
from deck import Deck 
from main import *
class Game():
	card_offset = 110 
	cards_top = 300 
	cards_left = 75 
	ncards = 8 
	points_correct = 15 
	points_incorrect = 10 

	def __init__(self, window):
		self.window = window
		self.oDeck = Deck(self.window)
		self.score = 100 
		self.scoreText = pygwidgets.DisplayText(window, (450, 164), 
			'Score: ' + str(self.score), fontSize=36, textColor=WHITE, justified='right')
		self.messageText = pywidgets.DisplayText(window, (50, 460), '', width=900, justified='center', fontSize=36, textColor=WHITE)
		#self.loserSound = pygame.mixer.Sound()
		self.cardPositionList = []
		thisLeft = Game.CARDS_LEFT
		for cardNum in range(Game.ncards):
			self.cardXPositionList.append(thisLeft)
			thisLeft = thisLeft + Game.CARDS_OFFSET
			self.reset()

		def reset(self):

			self.cardShuffleSound.play()
			self.CardList = []
			self.oDeck.shuffle()
			for cardIndex in range(0, Game.ncards):
				oCard = self.oDeck.getCard()
				self.CardList.append(oCard)
				thisXPosition = self.cardXPositionList[cardIndex]
				oCard.setLoc((thisXPosition, Game.cards_top))

			self.showCard(0)
			self.cardNumber = 0
			self.currentCardName, self.currentCardValue = self.getCardNameAndValue(self.cardNumber)
			self.messageText.setValue('Starting card is ' + self.currentCardName + 'Will the next card be higher or lower?')

		def getCardNameAndValue(self, index):
			oCard = self.cardList[index]
			theName = oCard.getName()
			theValue = oCard.getValue()
			return theName, theValue

		def showCard(self, index):
			oCard = self.cardList[index]
			theName = oCard.getName()
			theValue = oCard.getValue()
			return theName, theValue

		def hitHigherOrLower(self, higherOrLower):
			self.cardNumber = self.cardNumber + 1
			self.showCard(self.cardNumber)
			nextCardName, nextCardValue = self.getCardNameAndValue(self.cardNumber)

			if higherOrLower == HIGHER:
				if nextCardValue > self.currentCardValue:
					self.score = self.score + GAME.points_correct
					self.messageText.setValue('Yes, the' + nextCardName + 'was higher')
					self.winnerSound.play()
				else:
					self.score = self.score - Game.points_incorrect
					self.messageText.setValue('No, the ' + nextCardName + 'was not higher')

					if nextCardValue < self.currentCardValue:
						self.score = self.score + GAME.points_correct
						self.messageText.setValue('Yes, the' + nextCardName + 'was lower')
					else:
						self.score = self.score - Game.points_incorrect
						self.messageText.setValue('No, the' + nextCardName + 'was not lower')

				self.scoreText.setValue('Score: ' + str(self.score))
				self.currentCardValue = nextCardValue
				done = (self.cardNumber == (Game.ncards -1))
				return done

			def draw(self):
				for oCard in self.cardList:
					oCard.draw()

				self.scoreText.draw()
				self.messageText.draw()
				