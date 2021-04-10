# Warmp-up exercise for simulated annealing

import random

animals = dict()

def main():

    global animals
    rnd = random.random()
    favourite = "dogs" if rnd < 0.8 else "cats" if rnd < 0.9 else "bats"
    print("I love " + favourite)
    animals[favourite] = animals.get(favourite, 0) + 1


for i in range(100):
  main()

print(animals)