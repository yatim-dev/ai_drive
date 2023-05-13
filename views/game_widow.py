import sys

import pygame

from models.car import Car


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

            self.user_input_handler(car)

            car.draw(window)
            car.update()
            pygame.display.update()

    def user_input_handler(self, car):
        user_input = pygame.key.get_pressed()
        if user_input[pygame.K_w]:
            car.sprite.drive_state = False

        if user_input[pygame.K_s]:
            car.sprite.drive_state = True
