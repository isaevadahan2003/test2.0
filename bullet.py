import pygame

class Bullet(pygame.sprite.Sprite):

    def __init__(self, screen, gun):
        '''пуля из пушки'''
        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 2, 10)
        self.color = 255, 0, 0
        self.speed = 3.0
        self.rect.centerx = gun.rect.centerx
        self.rect.top = gun.rect.top
        self.y = float(self.rect.y)

    def update(self):
        '''перемещение пули верх'''
        self.y -= self.speed
        self.rect.y = self.y

    def draw_bullet(self):
        '''рисуем пулю на экране '''
        pygame.draw.rect(self.screen, self.color, self.rect)