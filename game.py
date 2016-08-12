import pygame
#import time
from random import randint
from pygame.locals import *

pygame.init()
diceroll = 0
# width, height = 640, 480
width = 200#640
height = 200#320
screen=pygame.display.set_mode((width, height))

# Load Images:
dice1 = pygame.image.load("img/1.png")
dice2 = pygame.image.load("img/2.png")
dice3 = pygame.image.load("img/3.png")
dice4 = pygame.image.load("img/4.png")
dice5 = pygame.image.load("img/5.png")
dice6 = pygame.image.load("img/6.png")
butt1 = pygame.image.load("img/button.png")

butt1x = width / 2 - 28 
butt1y = height /2 + 30

dicex = width / 2 - 9
dicey = height / 2 -9

# Main Loop Starts Here!!!
zumba = 0
while 1:
	# clear the screen and draw it again
	screen.fill(0)
	# draw screen elements
	# draw roll button
	screen.blit(butt1, (butt1x,butt1y))
	# draw dice
	if diceroll == 1:
		screen.blit(dice1, (dicex, dicey))
	elif diceroll == 2:
		screen.blit(dice2, (dicex, dicey))
	elif diceroll == 3:
		screen.blit(dice3, (dicex, dicey))
	elif diceroll == 4:
		screen.blit(dice4, (dicex, dicey))
	elif diceroll == 5:
		screen.blit(dice5, (dicex, dicey))
	elif diceroll == 6:
		screen.blit(dice6, (dicex, dicey))
	# update screen
	#test...
	zumba = zumba + 1
	print (zumba)	
	# ../test
	pygame.display.flip()
	# loop trough events
	for event in pygame.event.get():
		# check if event is X button


		if event.type==pygame.QUIT:
			# if yes, quit
			pygame.quit()
			exit(0)
		
		if event.type==pygame.MOUSEBUTTONDOWN:
			mouse = pygame.mouse.get_pos()
			#print ("x: " + str(mouse[0]))
			#print ("y: " + str(mouse[1]))
			butt1endx = butt1x + 56 
			butt1endy = butt1y + 27
			if mouse[0]>=butt1x and mouse[0]<=butt1endx:
				if mouse[1]>=butt1y and mouse[1]<=butt1endy:
					diceroll = randint(1,6)
