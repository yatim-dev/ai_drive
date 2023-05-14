import neat
import views.draw_car as dc


def setup_NEAT(config_path):
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

    pop.run(eval_genomes, 50)


def eval_genomes(genomes, config):
    global cars, ge, nets

    cars = []
    ge = []
    nets = []

    for genome_id, genome in genomes:
        cars.append(dc.spawn_car(self.window))  # TODO
        ge.append(genome)
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        nets.append(net)
        genome.fitness = 0

    game(window, map_)  # TODO


def car_handler(self):
    for i, car in enumerate(cars):
        ge[i].fitness += 1
        if not car.sprite.alive:
            self.remove(i)


def turn():
    for i, car in enumerate(cars):
        output = nets[i].activate(car.sprite.data())
        if output[0] > 0.7:
            car.sprite.direction = 1
        if output[1] > 0.7:
            car.sprite.direction = -1
        if output[0] <= 0.7 and output[1] <= 0.7:
            car.sprite.direction = 0


def remove(index):
    cars.pop(index)
    ge.pop(index)
    nets.pop(index)