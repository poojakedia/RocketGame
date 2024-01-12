
import pygame
from pygame.locals import *
import worlddata

tile_size = 50
game_over = 1
# Creating enemy
class Enemy(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        # Load lava.png using pygame.image.load method into img
        img = pygame.image.load("lava.png")
        self.image = pygame.transform.scale(img,(tile_size, tile_size))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
# Creating player
class Player():
    def __init__(self,x,y):
        # Load tom.png using pygame.image.load method into img
        img = pygame.image.load("tom.png")
        self.image = pygame.transform.scale(img,(40,80))
        # Load ghost.png using pygame.image.load method into self.dead_image
        self.dead_image = pygame.image.load("ghost.png")
        # Load rocket.png using pygame.image.load method into win_image
        self.win_image = pygame.image.load("Rocket.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        # Set self.width to image's width using get_width()
        self.width = self.image.get_width()
        # Set height to image's height using get_height()
        self.height = self.image.get_height()
        self.jumped = False
        self.vel_y = 0
    def update(self, game_over,screen):
      dx = 0
      dy = 0
      if game_over == 1:
        # We will accept the keypresses here
        key = pygame.key.get_pressed()
        # Get keypressed by the user and set it to key variable

        # Add conditionals: if space is pressed and jumped is False, change vel_y by -15
        if key[K_SPACE] and self.jumped == False:
          self.vel_y = -15
          self.jumped = True
          print("jumped")
          print(self.vel_y)

        if key[K_SPACE] == False:
          self.jumped = False
          print(self.vel_y)
          print("not jump")


        if key[K_LEFT]:
          dx -= 5
        if key[K_RIGHT]:
          dx += 5

        # Add conditionals: if space is pressed then set jumped to false
        
        # Add conditionals: if left is pressed then change x by -5
        
        # Add conditionals: if right is pressed then change x by +5
        

        # We have defined gravity over here
        self.vel_y +=1
        if self.vel_y>10:
            self.vel_y=10
        dy += self.vel_y
        # Checking for collison
        for tile in world.tile_list:
            # Checking for collison for X axis
            if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                dx = 0
            # Checking for collison on Y axis
            if tile[1].colliderect(self.rect.x,self.rect.y + dy,self.width,self.height):
                # Checking if below the ground (jumping)
                if self.vel_y<0:
                    dy = tile[1].bottom - self.rect.top
                    self.vel_y = 0
                # Checking if above the ground (falling)
                elif self.vel_y >= 0:
                    dy = tile[1].top - self.rect.bottom
                    self.vel_y = 0

        # Checking for collison with enemy
        if pygame.sprite.spritecollide(self, lava_group, False):
          # Set game over to 0 and print a losing message
          game_over = 0
          print("Sorry you have lost. Please try again.")
        if pygame.sprite.spritecollide(self, finish_group, False):
          # Set game over to 2 and print a winning message
          game_over = 2
          print("Congrats! You have won!!")

            

      elif game_over==0:
          self.image = self.dead_image
          self.rect.y -= 5
      elif game_over == 2:
          self.image = self.win_image
          self.rect.y -= 5
      # Update the x and y axis of image
      self.rect.x += dx
      self.rect.y += dy



      # Drawing player on screen
      screen.blit(self.image,self.rect)

     
      return game_over

class World():
    def __init__(self,data):
        self.tile_list = []

        # Loading platform images
        platform_image = pygame.image.load("platform.png")
        row_count = 0
        for row in data:
            col_count = 0
            for tile in row:
                if tile == 1:
                    img = pygame.transform.scale(platform_image,(tile_size,tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img,img_rect)
                    self.tile_list.append(tile)
                if tile == 2:
                    lava = Enemy(col_count*tile_size,row_count*tile_size)
                    lava_group.add(lava)

                if tile == 3:
                    Rocket = EndGame(col_count*tile_size,row_count*tile_size)
                    finish_group.add(Rocket)

                col_count +=1
            row_count += 1
    def draw(self,screen):
        for tile in self.tile_list:
            screen.blit(tile[0],tile[1])
            

#----------------End game portal class--------------------------
class EndGame(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        # Load rocket.png using pygame.load.image to img
        img = pygame.image.load("Rocket.png")
        self.image = pygame.transform.scale(img,(tile_size, tile_size))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

# We will use the sprite group method to group all the sprites of same type like an array of sprites
lava_group = pygame.sprite.Group()

# Set the finish_group as sprite.group
finish_group = pygame.sprite.Group()

world = World(worlddata.world_data)