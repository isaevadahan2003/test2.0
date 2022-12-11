import pygame

class Animation(pygame.sprite.Sprite):
    '''анимация уничтожение прищельцев'''

    def __init__(self, screen):
        '''создание изображение'''
        super(Animation, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images/ino_3.0.png')
        self.rect = self.image.get_rect()

    def draw_animation(self):
        '''создание анимацию на экран'''
        self.screen.blit(self.image, self.rect)

