from abc import ABC, abstractmethod


class EstateAbstract(ABC):
    def __init__(self, user, area, room_count, built_year, region, address, *args, **kwargs):
        self.user = user
        self.area = area
        self.room_count = room_count
        self.built_year = built_year
        self.region = region
        self.address = address
        super().__init__(*args, **kwargs)

    @abstractmethod
    def show_description(self):
        print(f"id: {self.id} \t area: {self.area} ")


class Apartment(EstateAbstract):
    def __init__(self, has_elevator, has_parking, floor, *args, **kwargs):
        self.has_elevator = has_elevator
        self.has_parking = has_parking
        self.floor = floor
        super().__init__(*args, **kwargs)

    def show_description(self):
        print(f"id: {self.id} \t area: {self.area} ")


class House(EstateAbstract):
    def __init__(self, has_yard, floors_count, *args, **kwargs):
        self.has_yard = has_yard
        self.floors_count = floors_count
        super().__init__(*args, **kwargs)

    def show_description(self):
        print(f"id: {self.id} \t area: {self.area} ")


class Store(EstateAbstract):
    def show_description(self):
        print(f"id: {self.id} \t area: {self.area} ")
