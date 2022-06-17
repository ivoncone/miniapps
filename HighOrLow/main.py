import pygwidgets
import pygame
from pygwidgets import window

background = pygwidgets.Image(window, (0, 0),
	'card/background.png')
newGameButton = pygwidgets.TextButton(window, (20, 530),
	'New Game', width=100, height=55)
higherButton = pygwidgets.TextButton(window, (540, 520),
	'Lower', width=120, height=55)
lowerButton = pygwidgets.TextButton(window, (340, 520),
	'Lower', width=120, height=55)
quitButton = pygwidgets.TextButton(window, (880, 530),
	'Quit', width=100, height=45)

oGame = Game(window)

while True:

	for event in pygame.event.get():
		if((event.type == QUIT) or ((event.type == KEYDOWN) and (event.key == K_ESCAPE))
			(quitButton.handleEvent(event))):
			pygame.quit()
			sys.exit()

	if newGameButton.handleEvent(event):
		oGame.reset()
		lowerButton.enable()
		higherButton.enable()

	if higherButton.handleEvent(event):
		gameOver = oGame.hitHigherOrLower(HIGHER)
		if gameOver:
			higherButton.disable()
			lowerButton.disable()

	if lowerButton.handleEvent(event):
		gameOver = oGame.hitHigherOrLower(LOWER)
		if gameOver:
			higherButton.disable()
			lowerButton.disable()

	background.draw()

	oGame.draw()
	newGameButton.draw()
	higherButton.draw()
	lowerButton.draw()
	quitButton.draw()

	pygame.display.update()