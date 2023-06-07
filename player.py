import pygame

class Player():
    def __init__(self,img):
        self.img = img
        self.img = pygame.transform.scale_by(self.img,4.8)
        self.rect = img.get_rect()
        self.rect.top = 500
        self.rect.left = 500
        self.velocity = 1.7
        self.jump = 10
        self.jumped = False

    def handle_move(self):
        keys=pygame.key.get_pressed()
        
        if keys[pygame.K_RIGHT]:
            self.rect.left += self.velocity
        
        if keys[pygame.K_LEFT]:
            self.rect.left -= self.velocity    

        if keys[pygame.K_SPACE] and self.jumped == False:
            self.rect.top -= self.jump
            self.jumped = True



    def draw(self,screen):
        screen.blit(self.img,(self.rect.left,self.rect.top))
        