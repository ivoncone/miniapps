import random

suit_tuple = ('spades', 'hearts', 'clubs', 'diamonds')
rank_tuple = ('ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king')
ncards = 8

def getCard(deckListIn):
	thisCard = deckListIn.pop()
	return thisCard

def shuffle(deckListIn):
	deckListOut = deckListIn.copy()
	random.shuffle(deckListOut)
	return deckListOut

print('Welcome to high or low')
print('you have to choose will be higher or lower than the curet card.')
print('right choice adds 20 points, wrong choice loose 15 points')
print('you have 50 points to starts')
print()

startingDeckList = []

for suit in suit_tuple:
	for thisValue, rank in enumerate(rank_tuple):
		cardDict = {'rank':rank, 'suit':suit, 'value':thisValue + 1}
		startingDeckList.append(cardDict)

score = 50

while True:
	print()
	gameDeckList = shuffle(startingDeckList)
	currentCardDict = getCard(gameDeckList)
	currentCardRank = currentCardDict['rank']
	currentCardValue = currentCardDict['value']
	currentCardSuit = currentCardDict['suit']
	print('Starting card is:', currentCardRank + ' of ' + currentCardSuit)
	print()

	for cardNumber in range(0, ncards):
		answer = input('Will the next card be higher or lower than the ' + currentCardRank + ' of ' + currentCardSuit + '? (enter h or l): ')
		answer = answer.casefold()

		nextCardDict = getCard(gameDeckList)
		nextCardRank = nextCardDict['rank']
		nextCardSuit = nextCardDict['suit']
		nextCardValue = nextCardDict['value']
		print('Next card is:', nextCardRank + ' of ' + nextCardSuit)

		if answer == 'h':
			if nextCardValue > currentCardValue:
				print('You got it right, it was higher')
				score = score + 20
			else:
				print('sorry, it was not higher')
				score = score - 15
		elif answer == 'l':
			if nextCardValue < currentCardValue:
				score = score + 20
				print('You got it right. It was lower')
				score = score + 20
				print('You got it right, it was lower')
			else:
				score = score - 15
				print('sorry, it was not lower')

		print('your score is: ', score)
		print()
		currentCardRank = nextCardRank
		currentCardValue = nextCardValue

	goAgain = input('To play again, press ENTER, or "q" t quit: ')
	if goAgain == 'q':
		break
		print('ok bye')