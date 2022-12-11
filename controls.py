import pygame
import sys
from bullet import Bullet
from ino import Ino
import time
from text import text
from pygame.color import THECOLORS

def events(screen, gun, bullets):
    '''движение'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            #направо
            if event.key == pygame.K_d:
                gun.mrignt = True
            #налево
            elif event.key == pygame.K_a:
                gun.mleft = True
            #наверх
            elif event.key == pygame.K_w:
                gun.mtop = True
            #вниз
            elif event.key == pygame.K_s:
                gun.mdown = True
            #пуля наверх
            elif event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen, gun)
                bullets.add(new_bullet)
        elif event.type == pygame.KEYUP:
            #направо
            if event.key == pygame.K_d:
                gun.mrignt = False
            #налево
            elif event.key == pygame.K_a:
                gun.mleft = False
            #наверх
            elif event.key == pygame.K_w:
                gun.mtop = False
                # вниз
            elif event.key == pygame.K_s:
                gun.mdown = False

def update(screen, sc, gun, inos, bullets):
    '''Обнавление экрана'''
    screen.fill(THECOLORS['black'])
    sc.show_score()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    gun.output()
    inos.draw(screen)
    pygame.display.flip()

def update_bullets(screen, stats, sc, inos, bullets):
    #обнавление позиции пуль
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    collisions = pygame.sprite.groupcollide(bullets, inos, True, True)
    if collisions:
        for inos in collisions.values():
            stats.score += 1 * len(inos)
            '''вывод анимацию на экран'''
            """пока что нечего нет"""

        sc.image_score()
        check_high_score(stats, sc)
        sc.image_guns()
    if len(inos) == 0:
        bullets.empty()
        create_army(screen, inos)

def gun_kill(stats, screen, sc, gun, inos, bullets):
    '''столкновение пушки и армии'''
    if stats.guns_left > 0:
        stats.guns_left -= 1
        sc.image_guns()
        inos.empty()
        bullets.empty()
        create_army(screen, inos)
        gun.create_gun()
        time.sleep(0.3)
    else:
        stats.run_game = False
        text()

def update_inos(stats, screen, sc, gun, inos, bullets):
    '''обнавляет позицию инопришельцев'''
    inos.update()
    if pygame.sprite.spritecollideany(gun, inos):
        gun_kill(stats, screen, sc, gun, inos, bullets)
    inos_check(stats, screen, sc, gun, inos, bullets)

def inos_check(stats, screen, sc, gun, inos, bullets):
    '''проверка, добралась ли армия до края экрна'''
    screen_rect = screen.get_rect()
    for ino in inos.sprites():
        if ino.rect.bottom >= screen_rect.bottom:
            gun_kill(stats, screen, sc, gun, inos, bullets)
            break

def create_army(screen, inos):
    '''создание армии пришельцев'''
    ino = Ino(screen)
    ino_width = ino.rect.width
    number_ino_x = int((700 - 2 * ino_width) / ino_width)
    ino_height = ino.rect.height
    number_ino_y = int((800 - 100 - 4 * ino_height) / ino_height)


    for row_number in range(number_ino_y - 8):
        for ino_number in range(number_ino_x):
            ino = Ino(screen)
            ino.x = ino_width + (ino_width * ino_number)
            ino.y = ino_height + (ino_height * row_number)
            ino.rect.x = ino.x
            ino.rect.y = ino.rect.height + (ino.rect.height * row_number)
            inos.add(ino)

def check_high_score(stats, sc):
    '''проверка новых рекордов'''
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sc.image_high_score()
        with open('highscore.txt', 'w') as f:
            f.write(str(stats.high_score))


