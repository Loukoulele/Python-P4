import pygame

from pygame.locals import *
from map import *

pygame.init()

black = (0,0,0)
white = (255, 255, 255)
BLUE =  (0,0,255)

font = pygame.font.SysFont(None, 45)

j1 = "Ilan"
j2 = "Jordan"

gamedisplay = pygame.display.set_mode((800,750))
pygame.display.set_caption('Puissance 4')

gameExit = False

while not gameExit:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameExit = True

	gamedisplay.fill(white)

	def message_to_screen(msg,color,x,y):
		screen_text = font.render(msg, True, color)
		gamedisplay.blit(screen_text, (x, y))

	message_to_screen("Joueur 1 : " + j1, black, 70, 680)
	message_to_screen("Joueur 2 : " + j2, black, 450, 680)

	## PASSAGE DE COULEUR
	# turn_j1 = False
	# turn_j2 = True
	#
	# while turn_j1 == False:
	# 	print ("Turn J1")
	#
	#
	#
	# while turn_j2 == False:



	##

	## MATRICE

    colonne = 5
    ligne = 5

    j = 5
    i = 5

    plateau = [[" " for j in range(colonne)] for i in range(ligne)]

	print (tableau)

	##

	## IA

	##


	init_map(gamedisplay, black)

	pygame.display.update()

pygame.quit()
quit()
