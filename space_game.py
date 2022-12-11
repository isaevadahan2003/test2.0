import pygame, controls
from gun import Gun
from pygame.sprite import Group
from stats import Stats
from scores import Scores

def run():
    pygame.init()
    screen = pygame.display.set_mode((700, 800))
    pygame.display.set_caption('Космические защитники✈')
    gun = Gun(screen)
    bullets = Group()
    inos = Group()
    controls.create_army(screen, inos)
    stats = Stats()
    sc = Scores(screen, stats)


    while True:
        controls.events(screen, gun, bullets)
        if stats.run_game:
            gun.opdate_gun()
            controls.update(screen, stats, sc, gun, inos, bullets)
            controls.update_bullets(screen, stats, sc, inos, bullets)
            controls.update_inos(stats, screen, sc, gun, inos, bullets)
run()