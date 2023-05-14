import math

import pygame


class DrawRadar:
    def scanner(self, screen, rect, angle, x, y, radar_angle, length):
        while not screen.get_at((x, y)) == pygame.Color(2, 105, 31, 255) and length < 200:
            length += 1
            x = int(rect.center[0] + math.cos(math.radians(angle + radar_angle)) * length)
            y = int(rect.center[1] - math.sin(math.radians(angle + radar_angle)) * length)
        return length, x, y

    def draw(self, screen, rect, x, y):
        pygame.draw.line(screen, (255, 255, 255, 255), rect.center, (x, y), 1)
        pygame.draw.circle(screen, (0, 255, 0, 0), (x, y), 3)

    def draw_col_points(self, screen, collision_point_right, collision_point_left):
        pygame.draw.circle(screen, (0, 255, 255, 0), collision_point_right, 4)
        pygame.draw.circle(screen, (0, 255, 255, 0), collision_point_left, 4)
