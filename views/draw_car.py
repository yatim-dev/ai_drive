import pygame

from models.car import Car


def spawn_car(window):
    return pygame.sprite.GroupSingle(Car(window))


def update_car(cars, screen):
    for car in cars:
        car.draw(screen)
        car.update()
    pygame.display.update()
