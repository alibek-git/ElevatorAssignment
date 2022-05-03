from classes import *
import random
from time import sleep

power_on = True
storeys = random.randint(5, 10)  # Randomizing the number of floors our building object will have

#  Creating instances of Building and Passengers
new_building = Building(storeys)  # Initialize Building instance
print(new_building)
sleep(1)
for floor in range(storeys):
    new_floor = Building.Floor(floor)
    new_building.floors_list.append(new_floor)
    for _ in range(random.randint(0, 5)):
        new_passenger = Passenger(_, floor, random.randint(1, storeys))
        new_building.floors_list[floor].passengers_list.append(new_passenger)
    print(new_floor)
    sleep(1)
    for y in new_floor.passengers_list:
        sleep(1)
        print(y)

# while power_on:
#
