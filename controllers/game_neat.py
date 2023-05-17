import sys

import pygame
import neat
import views.draw_car as dc


class GameWindow:
    """Класс для управления машиной алгоритмом NEAT"""

    def __init__(self, window, map, config_path):
        self.window = window
        self.map = map
        self.config_path = config_path
        self.setup_NEAT(config_path)

    def game(self):
        """Управление машиной и отрисовкой"""
        run = True
        while run:
            # Выйти по крестику
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # отрисовка карты
            self.window.blit(self.map, (0, 0))

            # конец поколения если все машины мертвы
            if len(cars) == 0:
                break

            self.car_handler()
            self.turn()

            dc.update_car(cars, self.window)

    def setup_NEAT(self, config_path):
        """Настройка NEAT"""
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

        winner = pop.run(self.eval_genomes, 50)
        print(winner)
        self.visualize_neural_net(winner, config)
        pygame.image.save(self.window, "neural_network.png")

    def eval_genomes(self, genomes, config):
        """Метод создания коллекций"""
        global cars, ge, nets

        cars = []
        ge = []
        nets = []

        # Заполняем списки
        for genome_id, genome in genomes:
            cars.append(dc.spawn_car(self.window))
            ge.append(genome)
            net = neat.nn.FeedForwardNetwork.create(genome, config)
            nets.append(net)
            # начальное значение
            genome.fitness = 0

        self.game()

    def car_handler(self):
        """Обработчик fitness каждого автомобиля"""
        # Увеличиваем fitness каждого автомобиля, если тот еще жив
        for i, car in enumerate(cars):
            ge[i].fitness += 1
            # Удаляем автомобиль, если он въехал в траву
            if not car.sprite.alive:
                self.remove(i)

    def turn(self):
        """Определяем поведение(поворот) каждого автомобиля"""
        for i, car in enumerate(cars):
            # Получаем выходные данные нейронной сети
            output = nets[i].activate(car.sprite.data())
            # Поворот направо
            if output[0] > 0.7:
                car.sprite.direction = 1
            # Поворот налево
            if output[1] > 0.7:
                car.sprite.direction = -1
            # Не поворачиваем
            if output[0] <= 0.7 and output[1] <= 0.7:
                car.sprite.direction = 0

    def remove(self, index):
        """Удаление автомобиля, коротый выехал на траву
        :parameter
        index : int
            индекс автомобиля, коротый выехал на траву
        """
        # удаляем машину
        cars.pop(index)
        # удаляем геном
        ge.pop(index)
        # удаляем нейронную сеть
        nets.pop(index)

    def visualize_neural_net(self, winner, config):
        surface = pygame.surfarray.make_surface(winner.visualize(config))
        self.window.blit(surface, (0, 0))
        pygame.display.update()
