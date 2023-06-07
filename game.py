import pygame
import player
background = pygame.image.load("assets/background.jpg")
player_img = pygame.image.load("assets/player1.png")



class Game():    
    def __init__(self,screen):
        self.screen = screen
        self.player = player.Player(player_img)
    
    def run(self):
        running = True
        while running:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    running = False
            self.player.handle_move()
            self.screen.blit(background,(0,0))
            self.player.draw(self.screen)
            
            pygame.display.flip()