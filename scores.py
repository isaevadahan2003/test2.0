import pygame.font
from gun import Gun
from pygame.sprite import Group

class Scores():
    '''вывод иговой имформации'''
    def __init__(self, screen, stats):
        '''подчет очков'''
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats
        self.text_color = (205, 85, 207)
        self.font = pygame.font.SysFont(None, 32)
        self.image_score()
        self.image_high_score()
        self.text_record()
        self.text_chet()
        self.image_guns()


    def image_high_score(self):
        '''приобразует рекорд в изображение'''
        self.high_score_image = self.font.render(str(self.stats.high_score), True, self.text_color, (0, 0, 0))
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx + 40
        self.high_score_rect.top = self.screen_rect.top + 20

    def text_record(self):
        '''вывод слово рекорд на экран'''
        self.text_record = self.font.render(str(self.stats.textrecord), True, self.text_color,  (0, 0, 0))
        self.text_record_rect = self.text_record.get_rect()
        self.text_record_rect.centerx = self.screen_rect.centerx - 30
        self.text_record_rect.top = self.screen_rect.top + 20

    def text_chet(self):
        '''вывод слово счет на экран'''
        self.text_chet = self.font.render(str(self.stats.textchet), True, self.text_color,  (0, 0, 0))
        self.text_chet_rect = self.text_chet.get_rect()
        self.text_chet_rect.centerx = self.screen_rect.centerx + 230
        self.text_chet_rect.top = self.screen_rect.top + 20

    def image_score(self):
        '''преобразывает текст счета в изображение'''
        self.score_img = self.font.render(str(self.stats.score), True, self.text_color, (0, 0, 0))
        self.score_rect = self.score_img.get_rect()
        self.score_rect.right = self.screen_rect.right - 40
        self.score_rect.top = 20


    def image_guns(self):
        '''количество жизней'''
        self.guns = Group()
        for gun_number in range(self.stats.guns_left):
            gun = Gun(self.screen)
            gun.rect.x = 15 + gun_number * gun.rect.width
            gun.rect.y = 10
            self.guns.add(gun)


    def show_score(self):
        '''вывод счета на экран'''
        self.screen.blit(self.score_img, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.text_record, self.text_record_rect)
        self.screen.blit(self.text_chet, self.text_chet_rect)
        self.guns.draw(self.screen)

