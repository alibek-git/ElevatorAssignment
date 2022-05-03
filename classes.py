class Building:

    def __init__(self, storeys):
        self.storeys = storeys
        self.floors_list = []

    def __str__(self):
        return f'The building is {self.storeys} floors tall'

    class Floor:  # Floor will be an inner class of the

        def __init__(self, floor_id):
            self.floor_id = floor_id + 1
            self.passengers_list = []

        def __repr__(self):
            return f'Floor #{self.floor_id} has {len(self.passengers_list)} passengers'


class Elevator:

    def __init__(self, max_floor, current_floor=1, max_capacity=5):
        self.current_floor = current_floor
        self.max_capacity = max_capacity
        self.max_floor = max_floor
        self.passengers_in_the_elevator = []


class Passenger:

    def __init__(self, passenger_id, current_floor, desired_floor, is_on_desired_floor=False):
        self.passenger_id = passenger_id + 1
        self.current_floor = current_floor + 1
        self.desired_floor = desired_floor
        self.is_on_desired_floor = is_on_desired_floor
        self.direction = 'Up' if self.current_floor < self.desired_floor else 'Down'

    def __repr__(self):
        return f'Passenger {self.passenger_id} is currently on floor {self.current_floor} and is going to floor ' \
               f'{self.desired_floor}. Direction: {self.direction} '
