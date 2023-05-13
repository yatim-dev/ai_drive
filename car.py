import os

import pygame.sprite


class Car(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.original_image = pygame.image.load(os.path.join("Assets", "car_v1.png"))
        self.image = self.original_image
        self.rect = self.image.get_rect(center=(600, 820))
        self.drive_state = False
        self.vel_vector = pygame.math.Vector2(0.8, 0)
        self.angle = 0

    def update(self):
        self.drive()
        self.rotate()

    def drive(self):
        if self.drive_state:
            self.rect.center += self.vel_vector

    def rotate(self):
        self.image = pygame.transform.rotozoom(self.original_image, self.angle, 0.1)
