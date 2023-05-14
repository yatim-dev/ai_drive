import sys

import pygame
import neat
import views.draw_car as dc


class GameWindow:
    def __init__(self, window, map, config_path):
        self.window = window
        self.map = map
        self.setup_NEAT(config_path)

    def game(self, window, map):
        run = True
        while run:
            # Выйти по крестику
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # отрисовка карты
            window.blit(map, (0, 0))
            if len(cars) == 0:
                break

            self.car_handler()
            self.turn()

            dc.update_car(cars, window)


    def setup_NEAT(self, config_path):
        config = neat.config.Config(
            neat.DefaultGenome,
            neat.DefaultReproduction,
            neat.DefaultSpeciesSet,
            neat.DefaultStagnation,
            config_path
        )

        pop = neat.Population(config)

        pop.add_reporter(neat.StdOutReporter(True))
        stats = neat.StatisticsReporter()
        pop.add_reporter(stats)

        pop.run(self.eval_genomes, 50)

    def eval_genomes(self, genomes, config):
        global cars, ge, nets

        cars = []
        ge = []
        nets = []

        for genome_id, genome in genomes:
            cars.append(dc.spawn_car(self.window))
            ge.append(genome)
            net = neat.nn.FeedForwardNetwork.create(genome, config)
            nets.append(net)
            genome.fitness = 0

        self.game(self.window, self.map)

    def car_handler(self):
        for i, car in enumerate(cars):
            ge[i].fitness += 1
            if not car.sprite.alive:
                self.remove(i)

    def turn(self):
        for i, car in enumerate(cars):
            output = nets[i].activate(car.sprite.data())
            if output[0] > 0.7:
                car.sprite.direction = 1
            if output[1] > 0.7:
                car.sprite.direction = -1
            if output[0] <= 0.7 and output[1] <= 0.7:
                car.sprite.direction = 0

    def remove(self, index):
        cars.pop(index)
        ge.pop(index)
        nets.pop(index)
