
# Import pygames, worlddata,player
import pygame
import worlddata
import player
from player import *
# Initilize Pygames
pygame.init()

clock = pygame.time.Clock()
fps = 60

screen_height = 700
screen_width = 1000
# Create a screen with the height and width
screen = pygame.display.set_mode((screen_width,screen_height))

pygame.display.set_caption("Space Odyssey")

run = True

background_image = pygame.image.load("spacebg.png")


tile_size = 50 
game_over = 1
# Set tile_size to 50 and game_over to 1



# Create player at 200, screen_height-110
player =  player.Player(200,screen_height- 150)


# Create a game loop using while run
while run:
  
# Set clock.tick to fps
  clock.tick(fps)
# Blit the background image to screen at(0,0)
  screen.blit(background_image,(0,0))
# Using the draw method, we will draw world to the screen
  world.draw(screen)

  lava_group.draw(screen)
  finish_group.draw(screen)


  for event in pygame.event.get():
    if event.type == pygame.quit:
      run= False
  
  game_over = player.update(game_over,screen)

  pygame.display.update()



