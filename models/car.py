import math
import os

import pygame.sprite

from views.draw_radar import DrawRadar


class Car(pygame.sprite.Sprite):
    """Класс по созданию модели машины"""
    def __init__(self, window):
        super().__init__()
        self.original_image = pygame.image.load(os.path.join("Assets", "car.png"))
        self.image = self.original_image
        self.screen = window
        self.rect = self.image.get_rect(center=(600, 820))
        self.alive = True
        self.vel_vector = pygame.math.Vector2(0.8, 0)
        self.angle = 0
        self.rotation_vel = 5
        self.direction = 0
        self.radars = []
        self.draw_radar = DrawRadar()

    def update(self):
        """Обновление машины с радаром, углом поворота, радаром"""
        self.radars.clear()
        self.drive()
        self.rotate()
        for radar_angle in (-60, -30, 0, 30, 60):
            self.radar(radar_angle)
        self.collision()
        self.data()

    def drive(self):
        """Метод, отвественный за скорость машины"""
        self.rect.center += self.vel_vector * 6

    def rotate(self):
        """Метод для поворота машины"""
        if self.direction == 1:
            self.angle -= self.rotation_vel
            self.vel_vector.rotate_ip(self.rotation_vel)
        if self.direction == -1:
            self.angle += self.rotation_vel
            self.vel_vector.rotate_ip(-self.rotation_vel)

        self.image = pygame.transform.rotozoom(self.original_image, self.angle, 0.1)
        self.rect = self.image.get_rect(center=self.rect.center)

    def radar(self, radar_angle):
        """Метод для работы с радаром"""
        length = 0
        x = int(self.rect.center[0])
        y = int(self.rect.center[1])

        length, x, y = self.draw_radar.scanner(self.screen, self.rect, self.angle, x, y, radar_angle, length)

        self.draw_radar.draw(self.screen, self.rect, x, y)

        # Расстояние между центром машины и верхушкой радара
        dist = int(math.sqrt(math.pow(self.rect.center[0] - x, 2)
                             + math.pow(self.rect.center[1] - y, 2)))

        self.radars.append([radar_angle, dist])

    def data(self):
        """Сбор данный с радаров для NEAT"""
        data = [0 for _ in range(5)]
        for i, radar in enumerate(self.radars):
            data[i] = int(radar[1])
        return data

    def collision(self):
        """Метод для создания точек коллизии"""
        length = 40
        collision_point_right = [int(self.rect.center[0] + math.cos(math.radians(self.angle + 18)) * length),
                                 int(self.rect.center[1] - math.sin(math.radians(self.angle + 18)) * length)]
        collision_point_left = [int(self.rect.center[0] + math.cos(math.radians(self.angle - 18)) * length),
                                int(self.rect.center[1] - math.sin(math.radians(self.angle - 18)) * length)]

        # Умереть при столкновении
        if self.screen.get_at(collision_point_right) == pygame.Color(2, 105, 31, 255) \
                or self.screen.get_at(collision_point_left) == pygame.Color(2, 105, 31, 255):
            self.alive = False

        # Рисуем точки столкновения
        self.draw_radar.draw_col_points(self.screen, collision_point_right, collision_point_left)
