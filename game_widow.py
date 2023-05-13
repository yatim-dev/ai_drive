import sys

import pygame

import car
from car import Car


class GameWindow():

    def game(self, window, map):
        car = pygame.sprite.GroupSingle(Car())
        run = True
        while run:
            # Выйти по крестику
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # отрисовка карты
            window.blit(map, (0, 0))

            user_input = pygame.key.get_pressed()
            if user_input[pygame.K_w]:
                car.sprite.drive_state = False

            if user_input[pygame.K_s]:
                car.sprite.drive_state = True


            car.draw(window)
            car.update()
            pygame.display.update()


