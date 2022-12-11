import pygame
from pygame.sprite import Sprite

class Gun(Sprite):
    def __init__(self, screen):
        """пушка"""
        super(Gun, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images/tank.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery + 300
        self.center = float(self.rect.centerx)
        self.centerl = float(self.rect.centery)
        self.rect.bottom = self.screen_rect.bottom - 40
        self.mrignt = False
        self.mleft = False
        self.mtop = False
        self.mdown = False

    def output(self):
        ''''рисование танка'''
        self.screen.blit(self.image, self.rect)

    def opdate_gun(self):
        '''движение танка'''
        if self.mrignt and self.rect.right < self.screen_rect.right - 55:
            self.center += 1.1
        elif self.mleft and self.rect.left > 55:
            self.center -= 1.1
        elif self.mtop and self.rect.top > self.screen_rect.height - 500:
            self.centerl -= 1.1
        elif self.mdown and self.rect.bottom < 800:
            self.centerl += 1.1

        self.rect.centerx = self.center
        self.rect.centery = self.centerl
    def create_gun(self):
        '''размещает пушку по центру внизу'''
        self.center = self.screen_rect.centerx

