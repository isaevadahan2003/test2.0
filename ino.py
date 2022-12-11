import pygame


class Ino(pygame.sprite.Sprite):
    '''класс одного прищельца'''

    def __init__(self, screen):
        '''началное позиция'''
        super(Ino, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images/ino.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.x = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def draw(self):
        '''ввывод пришельца на экран'''
        self.screen.blit(self.image, self.rect)

    def update(self):
        '''перемещение прищельцев'''
        self.y += 0.09
        self.rect.y = self.y
