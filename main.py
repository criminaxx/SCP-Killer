import pygame
import game
pygame.init()

HEIGHT = 1080
WIDTH = 720

screen = pygame.display.set_mode((HEIGHT,WIDTH))

pygame.display.set_caption('scp killer')

game = game.Game(screen)

game.run()

pygame.display.flip()