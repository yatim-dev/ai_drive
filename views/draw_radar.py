import math

import pygame


class DrawRadar:

    def scanner(self, screen, rect, angle, x, y, radar_angle, length):
        """Метод по отрисовке радара, линии и зеленых точек

        :parameters
        screen : pygame.display
            окно, в котором происходит отрисовка
        rect : image.get_rect
            фигура машины
        angle : int
            угол машины
        x : int
            координата x радара
        y : int
            координата y радара
        radar_angle : int
            угол радара
        length : int
            длина линии сканера

        :returns
        length : int
            новая длина линии сканера
        x : int
            новая координата x радара
        y : int
            новая координата y радара
        """
        while not screen.get_at((x, y)) == pygame.Color(2, 105, 31, 255) and length < 200:
            length += 1
            x = int(rect.center[0] + math.cos(math.radians(angle + radar_angle)) * length)
            y = int(rect.center[1] - math.sin(math.radians(angle + radar_angle)) * length)
        return length, x, y

    def draw(self, screen, rect, x, y):
        """Метод по отрисовке радара, линии и зеленых точек

        :parameters
        screen : pygame.display
            окно, в котором происходит отрисовка
        rect : image.get_rect
            фигура машины
        x : int
            координата x радара
        y : int
            координата y радара
        """
        pygame.draw.line(screen, (255, 255, 255, 255), rect.center, (x, y), 1)
        pygame.draw.circle(screen, (0, 255, 0, 0), (x, y), 3)

    def draw_col_points(self, screen, collision_point_right, collision_point_left):
        """Метод по отрисовке точек коллизий

        :parameter
        screen : pygame.display
            окно, в котором происходит отрисовка
        collision_point_right : list[int]
            позиция левой точки коллизии
        collision_point_left : list[int]
            позиция левой точки коллизии
        """
        pygame.draw.circle(screen, (0, 255, 255, 0), collision_point_right, 4)
        pygame.draw.circle(screen, (0, 255, 255, 0), collision_point_left, 4)
