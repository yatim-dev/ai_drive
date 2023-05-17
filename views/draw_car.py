import pygame

from models.car import Car


def spawn_car(screen):
    """Метод по созданию машин

    :parameter
    screen : pygame.display
        окно, в котором происходит отрисовка

    :return
    GroupSingle
        группа спрайтов
    """
    return pygame.sprite.GroupSingle(Car(screen))


def update_car(cars, screen):
    """Метод по отрисовки машины на карте

    :parameter
    cars : list
        коллекция машин
    screen : pygame.display
        окно, в котором происходит отрисовка
    """
    for car in cars:
        car.draw(screen)
        car.update()
    pygame.display.update()
